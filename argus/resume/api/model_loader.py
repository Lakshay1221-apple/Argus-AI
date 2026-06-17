import os
import torch
import logging
from transformers import AutoTokenizer

logger = logging.getLogger("ModelLoader")

class ModelLoader:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(ModelLoader, cls).__new__(cls)
            cls._instance.model = None
            cls._instance.tokenizer = None
            cls._instance.initialized = False
        return cls._instance

    def load_model(self, model_dir: str = "argus/resume/models/resume_adapter_v2_final"):
        if self.initialized:
            logger.info("Model already initialized.")
            return

        logger.info(f"Loading Resume Adapter V2 model from path: {model_dir}...")

        # Determine if we can use Unsloth
        try:
            from unsloth import FastLanguageModel
            logger.info("Using Unsloth FastLanguageModel for inference.")

            # Load model and tokenizer
            model, tokenizer = FastLanguageModel.from_pretrained(
                model_name=model_dir,
                max_seq_length=4096,
                dtype=None,
                load_in_4bit=True,
            )
            FastLanguageModel.for_inference(model)
            self.model = model
            self.tokenizer = tokenizer

        except ImportError as e:
            logger.warning(f"Unsloth could not be imported: {e}. Falling back to standard PEFT + Transformers.")
            from transformers import AutoModelForCausalLM
            from peft import PeftModel

            # Llama 3.2 1B base model name or path
            base_model_name = "unsloth/llama-3.2-1b-instruct-unsloth-bnb-4bit"
            logger.info(f"Loading base model {base_model_name}...")

            # Check CUDA availability
            device_map = "auto" if torch.cuda.is_available() else "cpu"
            torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

            base_model = AutoModelForCausalLM.from_pretrained(
                base_model_name,
                device_map=device_map,
                torch_dtype=torch_dtype,
            )

            logger.info(f"Loading adapter weights from {model_dir}...")
            self.model = PeftModel.from_pretrained(base_model, model_dir)
            self.tokenizer = AutoTokenizer.from_pretrained(model_dir)

        # Ensure tokenizer has pad token defined
        if self.tokenizer.pad_token_id is None:
            self.tokenizer.pad_token_id = self.tokenizer.eos_token_id

        self.initialized = True
        logger.info("Model loading completed successfully.")

    def generate_response(self, instruction: str, input_text: str, max_new_tokens: int = 150) -> str:
        if not self.initialized or self.model is None or self.tokenizer is None:
            raise ValueError("Model has not been initialized yet. Call load_model() first.")

        from argus.resume.api.prompts import format_prompt
        prompt = format_prompt(instruction, input_text)

        device = next(self.model.parameters()).device
        inputs = self.tokenizer([prompt], return_tensors="pt").to(device)

        # Stop IDs
        eos_ids = [self.tokenizer.eos_token_id]
        try:
            eot_id = self.tokenizer.convert_tokens_to_ids("<|eot_id|>")
            if isinstance(eot_id, int) and eot_id >= 0:
                eos_ids.append(eot_id)
        except Exception:
            pass

        # Generate response
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=max_new_tokens,
                do_sample=False,
                temperature=None,
                top_p=None,
                repetition_penalty=1.1,
                eos_token_id=eos_ids,
                pad_token_id=self.tokenizer.pad_token_id
            )

        # Slice output to decode only the generated parts
        input_len = inputs.input_ids.shape[1]
        generated_tokens = outputs[0][input_len:]
        response = self.tokenizer.decode(generated_tokens, skip_special_tokens=True)
        return response.strip()

# Global Singleton instance
loader = ModelLoader()
