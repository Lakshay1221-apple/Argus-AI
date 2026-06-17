import torch
import subprocess
import logging

logger = logging.getLogger("GPUInfo")

def get_gpu_memory_usage() -> dict:
    """
    Returns GPU memory details in MB. Falls back to nvidia-smi if torch is not reporting.
    """
    stats = {
        "allocated_mb": 0.0,
        "reserved_mb": 0.0,
        "max_allocated_mb": 0.0,
        "total_system_gpu_mb": 0.0,
        "used_system_gpu_mb": 0.0,
    }

    if not torch.cuda.is_available():
        return stats

    try:
        stats["allocated_mb"] = round(torch.cuda.memory_allocated() / (1024 ** 2), 2)
        stats["reserved_mb"] = round(torch.cuda.memory_reserved() / (1024 ** 2), 2)
        stats["max_allocated_mb"] = round(torch.cuda.max_memory_allocated() / (1024 ** 2), 2)
    except Exception as e:
        logger.warning(f"Failed to read torch cuda memory: {e}")

    # Use nvidia-smi command line to get total system GPU memory usage
    try:
        cmd = "nvidia-smi --query-gpu=memory.total,memory.used --format=csv,noheader,nounits"
        output = subprocess.check_output(cmd, shell=True).decode("utf-8").strip()
        parts = output.split(",")
        if len(parts) == 2:
            stats["total_system_gpu_mb"] = float(parts[0].strip())
            stats["used_system_gpu_mb"] = float(parts[1].strip())
    except Exception:
        # Ignore if nvidia-smi fails
        pass

    return stats
