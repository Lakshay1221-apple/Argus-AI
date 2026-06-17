"use client";

import React, { useState, useEffect, useRef } from "react";
import {
  FileText,
  Activity,
  Grid,
  Briefcase,
  BarChart2,
  Terminal,
  Server,
  Cpu,
  Clock,
  CheckCircle,
  XCircle,
  Copy,
  Check,
  Upload,
  AlertTriangle,
  Play,
  RefreshCw,
  Info
} from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardHeader, CardTitle, CardDescription, CardContent, CardFooter } from "@/components/ui/card";
import { Textarea } from "@/components/ui/textarea";
import { Input } from "@/components/ui/input";
import { Progress } from "@/components/ui/progress";
import { Badge } from "@/components/ui/badge";
import { Table, TableHeader, TableBody, TableRow, TableHead, TableCell } from "@/components/ui/table";
import { Dialog, DialogContent, DialogHeader, DialogTitle } from "@/components/ui/dialog";

// Interface Definitions
interface GPUStats {
  allocated_mb: number;
  reserved_mb: number;
  max_allocated_mb: number;
  total_system_gpu_mb: number;
  used_system_gpu_mb: number;
}

interface LogEntry {
  id: string;
  timestamp: string;
  method: string;
  path: string;
  status: number | string;
  latency: number;
  processTime: number;
  gpuAllocated: number;
  error?: string;
}

interface ReviewData {
  ats_score: number;
  strengths: string[];
  weaknesses: string[];
  suggestions: string[];
  verdict: string;
}

interface EvalTestCase {
  task: string;
  input: any;
  expected: string;
}

interface EvalResult {
  id: string;
  task: string;
  input: string;
  expected: string;
  actual: string;
  status: "pass" | "fail";
  latency: number;
  gpuAllocated: number;
  error?: string;
}

export default function Dashboard() {
  // Navigation
  const [activeTab, setActiveTab] = useState<string>("summary");

  // API Configuration & Health
  const [apiBaseUrl, setApiBaseUrl] = useState<string>("http://localhost:8000");
  const [apiOnline, setApiOnline] = useState<boolean>(false);
  const [checkingHealth, setCheckingHealth] = useState<boolean>(false);
  const [gpuStats, setGpuStats] = useState<GPUStats>({
    allocated_mb: 0,
    reserved_mb: 0,
    max_allocated_mb: 0,
    total_system_gpu_mb: 0,
    used_system_gpu_mb: 0,
  });

  // Logging Console State
  const [logs, setLogs] = useState<LogEntry[]>([]);
  const [showLogs, setShowLogs] = useState<boolean>(true);

  // Resume Summary States
  const [summaryResumeText, setSummaryResumeText] = useState<string>("");
  const [generatedSummary, setGeneratedSummary] = useState<string>("");
  const [summaryLoading, setSummaryLoading] = useState<boolean>(false);
  const [summaryCopied, setSummaryCopied] = useState<boolean>(false);

  // ATS Review States
  const [reviewResumeText, setReviewResumeText] = useState<string>("");
  const [reviewResult, setReviewResult] = useState<ReviewData | null>(null);
  const [reviewLoading, setReviewLoading] = useState<boolean>(false);

  // Section Classification States
  const [sectionText, setSectionText] = useState<string>("");
  const [predictedSection, setPredictedSection] = useState<string>("");
  const [classificationLoading, setClassificationLoading] = useState<boolean>(false);

  // Job Fit States
  const [fitResumeText, setFitResumeText] = useState<string>("");
  const [jobDescriptionText, setJobDescriptionText] = useState<string>("");
  const [predictedFit, setPredictedFit] = useState<string>("");
  const [jobFitLoading, setJobFitLoading] = useState<boolean>(false);

  // Evaluation States
  const [evalCasesRaw, setEvalCasesRaw] = useState<string>("");
  const [evalResults, setEvalResults] = useState<EvalResult[]>([]);
  const [runningEval, setRunningEval] = useState<boolean>(false);
  const [evalProgressCurrent, setEvalProgressCurrent] = useState<number>(0);
  const [evalProgressTotal, setEvalProgressTotal] = useState<number>(0);
  const [evalSelectedTaskFilter, setEvalSelectedTaskFilter] = useState<string>("all");
  const fileInputRef = useRef<HTMLInputElement>(null);

  // Dialog Modal for Full Text View
  const [selectedInspectResult, setSelectedInspectResult] = useState<EvalResult | null>(null);

  // Check Health status
  const checkHealth = async (url = apiBaseUrl) => {
    setCheckingHealth(true);
    try {
      const res = await fetch(`${url}/health`, {
        method: "GET",
        headers: { "Accept": "application/json" }
      });
      if (res.ok) {
        const data = await res.json();
        setApiOnline(true);
        if (data.gpu_stats) {
          setGpuStats(data.gpu_stats);
        }
      } else {
        setApiOnline(false);
      }
    } catch {
      setApiOnline(false);
    } finally {
      setCheckingHealth(false);
    }
  };

  useEffect(() => {
    checkHealth();
    const interval = setInterval(() => checkHealth(), 10000);
    return () => clearInterval(interval);
  }, [apiBaseUrl]);

  // Core API call helper
  const callApi = async (path: string, body: any) => {
    const startTime = performance.now();
    try {
      const res = await fetch(`${apiBaseUrl}${path}`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "Accept": "application/json"
        },
        body: JSON.stringify(body)
      });
      const latency = performance.now() - startTime;

      const processTimeHeader = res.headers.get("X-Response-Time-Ms");
      const gpuAllocHeader = res.headers.get("X-GPU-Memory-Allocated-MB");
      const gpuTotalHeader = res.headers.get("X-GPU-Memory-Total-System-MB");

      const data = await res.json();

      const logEntry: LogEntry = {
        id: Date.now() + Math.random().toString(),
        timestamp: new Date().toLocaleTimeString(),
        method: "POST",
        path,
        status: res.status,
        latency: latency,
        processTime: processTimeHeader ? parseFloat(processTimeHeader) : latency,
        gpuAllocated: gpuAllocHeader ? parseFloat(gpuAllocHeader) : 0,
      };

      setLogs(prev => [logEntry, ...prev].slice(0, 100));

      if (gpuAllocHeader && gpuTotalHeader) {
        setGpuStats(prev => ({
          ...prev,
          allocated_mb: parseFloat(gpuAllocHeader),
          total_system_gpu_mb: parseFloat(gpuTotalHeader)
        }));
      }

      if (!res.ok) {
        throw new Error(data.detail || "API request failed");
      }

      return { data, logEntry };
    } catch (err: any) {
      const latency = performance.now() - startTime;
      const logEntry: LogEntry = {
        id: Date.now() + Math.random().toString(),
        timestamp: new Date().toLocaleTimeString(),
        method: "POST",
        path,
        status: "ERR",
        latency: latency,
        processTime: 0,
        gpuAllocated: 0,
        error: err.message || "Network error"
      };
      setLogs(prev => [logEntry, ...prev].slice(0, 100));
      throw err;
    }
  };

  // Task 1: Generate Resume Summary
  const handleGenerateSummary = async () => {
    if (!summaryResumeText.trim()) return;
    setSummaryLoading(true);
    setGeneratedSummary("");
    try {
      const { data } = await callApi("/summary", { resume_text: summaryResumeText });
      setGeneratedSummary(data.summary);
    } catch (err: any) {
      alert(`Summary Generation Failed: ${err.message}`);
    } finally {
      setSummaryLoading(false);
    }
  };

  const handleCopySummary = () => {
    navigator.clipboard.writeText(generatedSummary);
    setSummaryCopied(true);
    setTimeout(() => setSummaryCopied(false), 2000);
  };

  // Task 2: Analyze Resume ATS
  const handleAnalyzeResume = async () => {
    if (!reviewResumeText.trim()) return;
    setReviewLoading(true);
    setReviewResult(null);
    try {
      const { data } = await callApi("/review", { resume_text: reviewResumeText });
      setReviewResult(data);
    } catch (err: any) {
      alert(`ATS Review Failed: ${err.message}`);
    } finally {
      setReviewLoading(false);
    }
  };

  // Task 3: Classify Resume Section
  const handleClassifySection = async () => {
    if (!sectionText.trim()) return;
    setClassificationLoading(true);
    setPredictedSection("");
    try {
      const { data } = await callApi("/classify-section", { section_text: sectionText });
      setPredictedSection(data.label);
    } catch (err: any) {
      alert(`Classification Failed: ${err.message}`);
    } finally {
      setClassificationLoading(false);
    }
  };

  // Task 4: Determine Job Fit
  const handleDetermineFit = async () => {
    if (!fitResumeText.trim() || !jobDescriptionText.trim()) return;
    setJobFitLoading(true);
    setPredictedFit("");
    try {
      const { data } = await callApi("/job-fit", {
        resume_text: fitResumeText,
        job_description: jobDescriptionText
      });
      setPredictedFit(data.fit);
    } catch (err: any) {
      alert(`Job Fit Analysis Failed: ${err.message}`);
    } finally {
      setJobFitLoading(false);
    }
  };

  // Evaluation: Load demo dataset
  const loadDemoEvaluationCases = () => {
    const demo = [
      {
        "task": "summary",
        "input": "Experienced Senior Software Engineer with 8+ years developing scalable SaaS web products using React, TypeScript, Node.js and AWS Cloud configurations. Built modular microservices reducing latency by 45%.",
        "expected": "SaaS microservices tech lead."
      },
      {
        "task": "review",
        "input": "Lacks measurable numbers. Summary: Professional engineer. Work history: Wrote React code, handled deployments, designed relational schemas.",
        "expected": "Detailed feedback focusing on numbers."
      },
      {
        "task": "classify-section",
        "input": "Languages: Python, Go, C++, JavaScript. Cloud: GCP, AWS, Kubernetes, Terraform. Frameworks: Django, Fastapi, React.",
        "expected": "Skills"
      },
      {
        "task": "job-fit",
        "input": {
          "resume_text": "Experienced Python Software Developer with strong knowledge of FastAPI, SQLite and Docker.",
          "job_description": "We are hiring a Backend Engineer to write high-performance APIs in Python using FastAPI. Experience with relational databases and containerization is required."
        },
        "expected": "Fit"
      },
      {
        "task": "job-fit",
        "input": {
          "resume_text": "Retail store associate with 3 years managing inventory, customer checkouts, and promotional merchandising.",
          "job_description": "Wanted: Senior Systems Site Reliability Engineer with Kubernetes, Linux kernel programming, and Rust infrastructure experience."
        },
        "expected": "No Fit"
      }
    ];
    setEvalCasesRaw(JSON.stringify(demo, null, 2));
  };

  const handleFileUpload = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = (event) => {
      const text = event.target?.result as string;
      setEvalCasesRaw(text);
    };
    reader.readAsText(file);
  };

  // Execute benchmarks
  const handleRunEvaluation = async () => {
    let cases: EvalTestCase[] = [];
    try {
      cases = JSON.parse(evalCasesRaw);
      if (!Array.isArray(cases)) {
        throw new Error("Evaluation cases must be a JSON array.");
      }
    } catch (err: any) {
      alert(`Invalid JSON format: ${err.message}`);
      return;
    }

    setRunningEval(true);
    setEvalResults([]);
    setEvalProgressTotal(cases.length);
    setEvalProgressCurrent(0);

    const tempResults: EvalResult[] = [];

    for (let i = 0; i < cases.length; i++) {
      const c = cases[i];
      setEvalProgressCurrent(i + 1);

      let apiPath = "";
      let payload: any = {};
      let rawInputStr = "";

      if (c.task === "summary") {
        apiPath = "/summary";
        payload = { resume_text: c.input };
        rawInputStr = c.input;
      } else if (c.task === "review") {
        apiPath = "/review";
        payload = { resume_text: c.input };
        rawInputStr = c.input;
      } else if (c.task === "classify-section" || c.task === "section") {
        apiPath = "/classify-section";
        payload = { section_text: c.input };
        rawInputStr = c.input;
      } else if (c.task === "job-fit" || c.task === "job_fit") {
        apiPath = "/job-fit";
        let resume_text = "";
        let job_description = "";
        
        if (typeof c.input === "object" && c.input !== null) {
          resume_text = c.input.resume_text || "";
          job_description = c.input.job_description || "";
        } else {
          try {
            const parsed = JSON.parse(c.input);
            resume_text = parsed.resume_text || "";
            job_description = parsed.job_description || "";
          } catch {
            const splitText = c.input.split(/Job Description:/i);
            if (splitText.length >= 2) {
              resume_text = splitText[0].replace(/Resume:/i, "").trim();
              job_description = splitText[1].trim();
            } else {
              resume_text = c.input;
              job_description = "";
            }
          }
        }
        payload = { resume_text, job_description };
        rawInputStr = `Resume: ${resume_text.substring(0, 100)}... | Job Description: ${job_description.substring(0, 100)}...`;
      } else {
        // Skip unknown task
        continue;
      }

      try {
        const { data, logEntry } = await callApi(apiPath, payload);
        let actualVal = "";
        let isPass = false;

        if (c.task === "summary") {
          actualVal = data.summary;
          isPass = actualVal.trim().length > 0;
        } else if (c.task === "review") {
          actualVal = `Score: ${data.ats_score} | Verdict: ${data.verdict}`;
          isPass = data.ats_score > 0 && Array.isArray(data.strengths);
        } else if (c.task === "classify-section" || c.task === "section") {
          actualVal = data.label;
          isPass = actualVal.toLowerCase().trim() === c.expected.toLowerCase().trim();
        } else if (c.task === "job-fit" || c.task === "job_fit") {
          actualVal = data.fit;
          isPass = actualVal.toLowerCase().trim() === c.expected.toLowerCase().trim();
        }

        const runResult: EvalResult = {
          id: Date.now() + Math.random().toString(),
          task: c.task,
          input: rawInputStr,
          expected: typeof c.expected === "object" ? JSON.stringify(c.expected) : c.expected,
          actual: actualVal,
          status: isPass ? "pass" : "fail",
          latency: logEntry.latency,
          gpuAllocated: logEntry.gpuAllocated
        };
        tempResults.push(runResult);
        setEvalResults([...tempResults]);
      } catch (err: any) {
        const runResult: EvalResult = {
          id: Date.now() + Math.random().toString(),
          task: c.task,
          input: rawInputStr,
          expected: typeof c.expected === "object" ? JSON.stringify(c.expected) : c.expected,
          actual: "ERROR",
          status: "fail",
          latency: 0,
          gpuAllocated: 0,
          error: err.message
        };
        tempResults.push(runResult);
        setEvalResults([...tempResults]);
      }
    }
    setRunningEval(false);
  };

  // Benchmark stats
  const getBenchmarkStats = () => {
    const tasks = ["summary", "review", "classify-section", "section", "job-fit", "job_fit"];
    const stats: Record<string, { total: number; passed: number; pct: number }> = {};

    tasks.forEach(t => {
      const matches = evalResults.filter(r => r.task === t || (t === "classify-section" && r.task === "section") || (t === "job-fit" && r.task === "job_fit"));
      const passed = matches.filter(r => r.status === "pass").length;
      stats[t] = {
        total: matches.length,
        passed,
        pct: matches.length > 0 ? Math.round((passed / matches.length) * 100) : 0
      };
    });

    const passedTotal = evalResults.filter(r => r.status === "pass").length;
    const overallPct = evalResults.length > 0 ? Math.round((passedTotal / evalResults.length) * 100) : 0;

    return {
      stats,
      total: evalResults.length,
      passedTotal,
      overallPct
    };
  };

  const evalStats = getBenchmarkStats();

  const filteredEvalResults = evalResults.filter(r => {
    if (evalSelectedTaskFilter === "all") return true;
    if (evalSelectedTaskFilter === "classify-section") return r.task === "classify-section" || r.task === "section";
    if (evalSelectedTaskFilter === "job-fit") return r.task === "job-fit" || r.task === "job_fit";
    return r.task === evalSelectedTaskFilter;
  });

  return (
    <div className="flex h-screen bg-slate-950 text-slate-100 font-sans overflow-hidden">
      {/* SIDEBAR */}
      <aside className="w-80 bg-slate-900 border-r border-slate-800 flex flex-col justify-between overflow-y-auto">
        <div>
          {/* Brand header */}
          <div className="p-6 border-b border-slate-800">
            <div className="flex items-center gap-3">
              <div className="bg-indigo-600 p-2 rounded-lg text-white shadow-[0_0_15px_rgba(79,70,229,0.5)]">
                <Cpu className="h-6 w-6" />
              </div>
              <div>
                <h1 className="font-extrabold text-xl tracking-tight bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                  ARGUS AI
                </h1>
                <p className="text-[10px] text-slate-400 uppercase tracking-widest font-semibold">
                  Resume Adapter V2
                </p>
              </div>
            </div>
          </div>

          {/* Navigation Links */}
          <nav className="p-4 space-y-1">
            <button
              onClick={() => setActiveTab("summary")}
              className={`flex items-center gap-3 w-full px-4 py-3 rounded-lg text-sm font-medium transition-all ${
                activeTab === "summary"
                  ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <FileText className="h-5 w-5" />
              Resume Summary
            </button>
            <button
              onClick={() => setActiveTab("review")}
              className={`flex items-center gap-3 w-full px-4 py-3 rounded-lg text-sm font-medium transition-all ${
                activeTab === "review"
                  ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <Activity className="h-5 w-5" />
              ATS Review
            </button>
            <button
              onClick={() => setActiveTab("classification")}
              className={`flex items-center gap-3 w-full px-4 py-3 rounded-lg text-sm font-medium transition-all ${
                activeTab === "classification"
                  ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <Grid className="h-5 w-5" />
              Section Classification
            </button>
            <button
              onClick={() => setActiveTab("jobfit")}
              className={`flex items-center gap-3 w-full px-4 py-3 rounded-lg text-sm font-medium transition-all ${
                activeTab === "jobfit"
                  ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <Briefcase className="h-5 w-5" />
              Job Fit Analysis
            </button>
            <button
              onClick={() => setActiveTab("dashboard")}
              className={`flex items-center gap-3 w-full px-4 py-3 rounded-lg text-sm font-medium transition-all ${
                activeTab === "dashboard"
                  ? "bg-indigo-600 text-white shadow-lg shadow-indigo-600/20"
                  : "text-slate-400 hover:text-white hover:bg-slate-800"
              }`}
            >
              <BarChart2 className="h-5 w-5" />
              Evaluation Dashboard
            </button>
          </nav>
        </div>

        {/* API connection config & GPU metrics */}
        <div className="p-4 border-t border-slate-800 bg-slate-950/40 space-y-4">
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider">
                Connection Config
              </span>
              <span className="flex items-center gap-1.5">
                <span className={`h-2.5 w-2.5 rounded-full ${apiOnline ? "bg-emerald-500 animate-pulse" : "bg-rose-500"}`} />
                <span className="text-xs font-semibold text-slate-300">
                  {apiOnline ? "Online" : "Offline"}
                </span>
              </span>
            </div>
            <div className="flex gap-2">
              <Input
                type="text"
                value={apiBaseUrl}
                onChange={(e) => setApiBaseUrl(e.target.value)}
                placeholder="http://localhost:8000"
                className="bg-slate-900 border-slate-700 text-xs h-8 text-slate-200"
              />
              <Button
                size="sm"
                onClick={() => checkHealth()}
                disabled={checkingHealth}
                className="bg-slate-800 hover:bg-slate-700 h-8 border border-slate-700"
              >
                <RefreshCw className={`h-3 w-3 ${checkingHealth ? "animate-spin" : ""}`} />
              </Button>
            </div>
          </div>

          {/* GPU Monitor Display */}
          <div className="space-y-2.5 bg-slate-900/60 p-3 rounded-lg border border-slate-800/60">
            <div className="flex items-center gap-2 text-xs font-semibold text-slate-300">
              <Server className="h-4 w-4 text-indigo-400" />
              <span>GPU VRAM Monitor</span>
            </div>

            {apiOnline && gpuStats.total_system_gpu_mb > 0 ? (
              <div className="space-y-1">
                <div className="flex justify-between text-[10px] text-slate-400">
                  <span>Usage: {gpuStats.used_system_gpu_mb} / {gpuStats.total_system_gpu_mb} MB</span>
                  <span className="font-bold text-slate-200">
                    {Math.round((gpuStats.used_system_gpu_mb / gpuStats.total_system_gpu_mb) * 100)}%
                  </span>
                </div>
                <Progress
                  value={(gpuStats.used_system_gpu_mb / gpuStats.total_system_gpu_mb) * 100}
                  className="h-1.5 bg-slate-800"
                />
                <div className="text-[9px] text-slate-500 pt-1 flex justify-between">
                  <span>PyTorch Alloc: {gpuStats.allocated_mb} MB</span>
                  <span>Peak: {gpuStats.max_allocated_mb} MB</span>
                </div>
              </div>
            ) : (
              <div className="text-[10px] text-slate-500 italic">
                {apiOnline ? "No GPU metrics reported by backend." : "Backend disconnected."}
              </div>
            )}
          </div>
        </div>
      </aside>

      {/* MAIN CONTENT WORKSPACE */}
      <div className="flex-1 flex flex-col min-w-0 overflow-hidden">
        {/* TOP HEADER */}
        <header className="h-16 border-b border-slate-800 bg-slate-900 flex items-center justify-between px-8 z-10">
          <div className="flex items-center gap-2">
            <span className="text-slate-400 text-sm font-medium">Adapter v2 Testing</span>
            <span className="text-slate-600 text-sm font-semibold">/</span>
            <span className="text-slate-200 text-sm font-semibold capitalize">
              {activeTab === "jobfit" ? "Job Fit Analysis" : activeTab + " Task"}
            </span>
          </div>

          <div className="flex items-center gap-4">
            <Button
              size="sm"
              variant="ghost"
              onClick={() => setShowLogs(!showLogs)}
              className={`text-xs flex items-center gap-1.5 border border-slate-700/60 ${showLogs ? "bg-slate-800 text-indigo-400" : "text-slate-400"}`}
            >
              <Terminal className="h-3.5 w-3.5" />
              Dev Console {logs.length > 0 && <span className="bg-indigo-600 text-white rounded-full px-1.5 py-0.2 text-[9px]">{logs.length}</span>}
            </Button>
          </div>
        </header>

        {/* WORKSPACE VIEWPORTS */}
        <main className="flex-1 p-8 overflow-y-auto min-w-0">
          {/* TAB 1: RESUME SUMMARY */}
          {activeTab === "summary" && (
            <div className="max-w-4xl mx-auto space-y-6">
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-bold tracking-tight text-slate-100">Resume Summary Generation</h2>
                <p className="text-slate-400 text-sm">
                  Produces a high-impact professional summary optimized for candidate tracking workflows.
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <Card className="bg-slate-900 border-slate-800 flex flex-col">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">Resume Text Input</CardTitle>
                    <CardDescription className="text-xs">Paste full resume contents below.</CardDescription>
                  </CardHeader>
                  <CardContent className="flex-1 flex flex-col">
                    <Textarea
                      placeholder="Paste resume details..."
                      value={summaryResumeText}
                      onChange={(e) => setSummaryResumeText(e.target.value)}
                      className="flex-1 min-h-[300px] bg-slate-950 border-slate-800 text-sm text-slate-300 focus-visible:ring-indigo-600"
                    />
                  </CardContent>
                  <CardFooter className="border-t border-slate-800/60 p-4">
                    <Button
                      onClick={handleGenerateSummary}
                      disabled={summaryLoading || !summaryResumeText.trim() || !apiOnline}
                      className="w-full bg-indigo-600 hover:bg-indigo-500 font-semibold"
                    >
                      {summaryLoading ? (
                        <>
                          <RefreshCw className="h-4 w-4 animate-spin mr-2" />
                          Running Model Inference...
                        </>
                      ) : (
                        "Generate Summary"
                      )}
                    </Button>
                  </CardFooter>
                </Card>

                <Card className="bg-slate-900 border-slate-800 flex flex-col">
                  <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
                    <div>
                      <CardTitle className="text-sm font-semibold text-slate-300">Generated Summary Output</CardTitle>
                      <CardDescription className="text-xs">Resume Adapter V2 inference output.</CardDescription>
                    </div>
                    {generatedSummary && (
                      <Button
                        size="icon"
                        variant="ghost"
                        onClick={handleCopySummary}
                        className="text-slate-400 hover:text-white"
                      >
                        {summaryCopied ? <Check className="h-4 w-4 text-emerald-400" /> : <Copy className="h-4 w-4" />}
                      </Button>
                    )}
                  </CardHeader>
                  <CardContent className="flex-1 flex flex-col">
                    {generatedSummary ? (
                      <div className="flex-1 bg-slate-950 p-4 rounded-lg border border-slate-800 text-sm text-slate-300 leading-relaxed font-sans min-h-[300px] overflow-y-auto whitespace-pre-wrap">
                        {generatedSummary}
                      </div>
                    ) : (
                      <div className="flex-1 border border-dashed border-slate-800 rounded-lg flex items-center justify-center text-slate-600 text-sm italic min-h-[300px]">
                        {summaryLoading ? "Generating..." : "No summary generated yet. Click the button to run inference."}
                      </div>
                    )}
                  </CardContent>
                </Card>
              </div>
            </div>
          )}

          {/* TAB 2: ATS RESUME REVIEW */}
          {activeTab === "review" && (
            <div className="max-w-4xl mx-auto space-y-6">
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-bold tracking-tight text-slate-100">ATS Resume Review</h2>
                <p className="text-slate-400 text-sm">
                  Grades the resume and synthesizes structured qualitative feedback detailing strengths, weaknesses, and optimization suggestions.
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <Card className="bg-slate-900 border-slate-800 flex flex-col">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">Resume Content</CardTitle>
                    <CardDescription className="text-xs">Paste resume text to audit.</CardDescription>
                  </CardHeader>
                  <CardContent className="flex-1 flex flex-col">
                    <Textarea
                      placeholder="Paste resume details..."
                      value={reviewResumeText}
                      onChange={(e) => setReviewResumeText(e.target.value)}
                      className="flex-1 min-h-[350px] bg-slate-950 border-slate-800 text-sm text-slate-300 focus-visible:ring-indigo-600"
                    />
                  </CardContent>
                  <CardFooter className="border-t border-slate-800/60 p-4">
                    <Button
                      onClick={handleAnalyzeResume}
                      disabled={reviewLoading || !reviewResumeText.trim() || !apiOnline}
                      className="w-full bg-indigo-600 hover:bg-indigo-500 font-semibold"
                    >
                      {reviewLoading ? (
                        <>
                          <RefreshCw className="h-4 w-4 animate-spin mr-2" />
                          Analyzing and Repairing JSON...
                        </>
                      ) : (
                        "Analyze Resume"
                      )}
                    </Button>
                  </CardFooter>
                </Card>

                <Card className="bg-slate-900 border-slate-800 flex flex-col overflow-hidden">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">ATS Review Feedback</CardTitle>
                    <CardDescription className="text-xs">Audit results.</CardDescription>
                  </CardHeader>
                  <CardContent className="flex-1 overflow-y-auto max-h-[420px] space-y-4">
                    {reviewResult ? (
                      <div className="space-y-4">
                        {/* Score and Verdict Header */}
                        <div className="flex items-center gap-4 bg-slate-950 p-4 rounded-xl border border-slate-800">
                          {/* Circular Gauge */}
                          <div className="relative h-20 w-20 flex items-center justify-center">
                            <svg className="h-full w-full transform -rotate-90">
                              <circle
                                cx="40"
                                cy="40"
                                r="34"
                                className="stroke-slate-800 fill-none"
                                strokeWidth="6"
                              />
                              <circle
                                cx="40"
                                cy="40"
                                r="34"
                                className={`fill-none transition-all duration-1000 ${
                                  reviewResult.ats_score >= 80
                                    ? "stroke-emerald-500"
                                    : reviewResult.ats_score >= 50
                                    ? "stroke-amber-500"
                                    : "stroke-rose-500"
                                }`}
                                strokeWidth="6"
                                strokeDasharray={2 * Math.PI * 34}
                                strokeDashoffset={2 * Math.PI * 34 * (1 - reviewResult.ats_score / 100)}
                                strokeLinecap="round"
                              />
                            </svg>
                            <span className="absolute text-lg font-extrabold text-slate-100">
                              {reviewResult.ats_score}
                            </span>
                          </div>

                          <div>
                            <span className="text-xs text-slate-500 font-semibold uppercase tracking-wider">
                              ATS Grade
                            </span>
                            <div className="flex items-center gap-2 mt-0.5">
                              <h3 className="text-lg font-bold text-slate-200">
                                {reviewResult.verdict}
                              </h3>
                              <Badge
                                className={`text-[10px] ${
                                  reviewResult.verdict.toLowerCase().includes("strong")
                                    ? "bg-emerald-500/10 text-emerald-400 border-emerald-500/20"
                                    : reviewResult.verdict.toLowerCase().includes("potential") || reviewResult.verdict.toLowerCase().includes("partial")
                                    ? "bg-amber-500/10 text-amber-400 border-amber-500/20"
                                    : "bg-rose-500/10 text-rose-400 border-rose-500/20"
                                }`}
                                variant="outline"
                              >
                                Match Rating
                              </Badge>
                            </div>
                          </div>
                        </div>

                        {/* Accordion/Lists */}
                        <div className="space-y-3 text-xs">
                          {/* Strengths */}
                          <div className="space-y-1.5">
                            <h4 className="font-semibold text-emerald-400 flex items-center gap-1.5">
                              <CheckCircle className="h-4 w-4" /> Strengths
                            </h4>
                            <ul className="list-disc pl-5 space-y-1 text-slate-300">
                              {reviewResult.strengths?.map((item, idx) => (
                                <li key={idx}>{item}</li>
                              ))}
                            </ul>
                          </div>

                          {/* Weaknesses */}
                          <div className="space-y-1.5 pt-1.5 border-t border-slate-800/40">
                            <h4 className="font-semibold text-rose-400 flex items-center gap-1.5">
                              <XCircle className="h-4 w-4" /> Weaknesses
                            </h4>
                            <ul className="list-disc pl-5 space-y-1 text-slate-300">
                              {reviewResult.weaknesses?.map((item, idx) => (
                                <li key={idx}>{item}</li>
                              ))}
                            </ul>
                          </div>

                          {/* Suggestions */}
                          <div className="space-y-1.5 pt-1.5 border-t border-slate-800/40">
                            <h4 className="font-semibold text-indigo-400 flex items-center gap-1.5">
                              <Info className="h-4 w-4" /> Suggestions
                            </h4>
                            <ul className="list-disc pl-5 space-y-1 text-slate-300">
                              {reviewResult.suggestions?.map((item, idx) => (
                                <li key={idx}>{item}</li>
                              ))}
                            </ul>
                          </div>
                        </div>
                      </div>
                    ) : (
                      <div className="flex border border-dashed border-slate-800 rounded-lg flex-col items-center justify-center text-slate-600 text-sm italic h-60">
                        {reviewLoading ? "Inference Running..." : "No analysis. Submit resume to review."}
                      </div>
                    )}
                  </CardContent>
                </Card>
              </div>
            </div>
          )}

          {/* TAB 3: SECTION CLASSIFICATION */}
          {activeTab === "classification" && (
            <div className="max-w-4xl mx-auto space-y-6">
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-bold tracking-tight text-slate-100">Resume Section Classification</h2>
                <p className="text-slate-400 text-sm">
                  Classifies individual blocks of resume text into designated structural schemas (e.g. Work Experience, Education, Skills, Summary, etc.).
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                <Card className="bg-slate-900 border-slate-800 flex flex-col">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">Section Content Block</CardTitle>
                    <CardDescription className="text-xs">Provide a section block below.</CardDescription>
                  </CardHeader>
                  <CardContent className="flex-1 flex flex-col">
                    <Textarea
                      placeholder="e.g. September 2021 - Present: Senior Developer. Built RESTful API endpoints..."
                      value={sectionText}
                      onChange={(e) => setSectionText(e.target.value)}
                      className="flex-1 min-h-[250px] bg-slate-950 border-slate-800 text-sm text-slate-300 focus-visible:ring-indigo-600"
                    />
                  </CardContent>
                  <CardFooter className="border-t border-slate-800/60 p-4">
                    <Button
                      onClick={handleClassifySection}
                      disabled={classificationLoading || !sectionText.trim() || !apiOnline}
                      className="w-full bg-indigo-600 hover:bg-indigo-500 font-semibold"
                    >
                      {classificationLoading ? (
                        <>
                          <RefreshCw className="h-4 w-4 animate-spin mr-2" />
                          Classifying...
                        </>
                      ) : (
                        "Classify Section"
                      )}
                    </Button>
                  </CardFooter>
                </Card>

                <Card className="bg-slate-900 border-slate-800 flex flex-col justify-between">
                  <div>
                    <CardHeader>
                      <CardTitle className="text-sm font-semibold text-slate-300">Classification Result</CardTitle>
                      <CardDescription className="text-xs">Predicted Section Category.</CardDescription>
                    </CardHeader>
                    <CardContent className="flex items-center justify-center pt-8">
                      {predictedSection ? (
                        <div className="text-center space-y-4">
                          <Badge className="px-6 py-2.5 bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 text-lg font-bold rounded-lg shadow-inner">
                            {predictedSection}
                          </Badge>
                          <p className="text-xs text-slate-500">
                            Model matched with high classification confidence.
                          </p>
                        </div>
                      ) : (
                        <div className="border border-dashed border-slate-800 rounded-lg w-full flex items-center justify-center text-slate-600 text-sm italic h-44">
                          {classificationLoading ? "Analyzing..." : "Awaiting section text."}
                        </div>
                      )}
                    </CardContent>
                  </div>
                  <div className="p-6 border-t border-slate-800/60 text-xs text-slate-500 bg-slate-950/20">
                    <div className="flex gap-2">
                      <Info className="h-4 w-4 text-indigo-400 shrink-0" />
                      <span>The classification task maps to standardized labels used to map resumes to relational database schemas.</span>
                    </div>
                  </div>
                </Card>
              </div>
            </div>
          )}

          {/* TAB 4: JOB FIT ANALYSIS */}
          {activeTab === "jobfit" && (
            <div className="max-w-5xl mx-auto space-y-6">
              <div className="flex flex-col gap-2">
                <h2 className="text-2xl font-bold tracking-tight text-slate-100">Resume ↔ Job Description Fit Analysis</h2>
                <p className="text-slate-400 text-sm">
                  Evaluates alignment between a candidate's resume and a specific job posting, returning Fit, Partial Fit, or No Fit.
                </p>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
                {/* Resume text */}
                <Card className="bg-slate-900 border-slate-800 flex flex-col md:col-span-1">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">Candidate Resume</CardTitle>
                  </CardHeader>
                  <CardContent className="flex-1">
                    <Textarea
                      placeholder="Paste candidate resume text..."
                      value={fitResumeText}
                      onChange={(e) => setFitResumeText(e.target.value)}
                      className="w-full h-80 bg-slate-950 border-slate-800 text-xs text-slate-300"
                    />
                  </CardContent>
                </Card>

                {/* JD text */}
                <Card className="bg-slate-900 border-slate-800 flex flex-col md:col-span-1">
                  <CardHeader>
                    <CardTitle className="text-sm font-semibold text-slate-300">Job Description</CardTitle>
                  </CardHeader>
                  <CardContent className="flex-1">
                    <Textarea
                      placeholder="Paste target job description..."
                      value={jobDescriptionText}
                      onChange={(e) => setJobDescriptionText(e.target.value)}
                      className="w-full h-80 bg-slate-950 border-slate-800 text-xs text-slate-300"
                    />
                  </CardContent>
                </Card>

                {/* Output */}
                <Card className="bg-slate-900 border-slate-800 flex flex-col justify-between md:col-span-1">
                  <div>
                    <CardHeader>
                      <CardTitle className="text-sm font-semibold text-slate-300">Alignment Evaluation</CardTitle>
                    </CardHeader>
                    <CardContent className="flex flex-col items-center justify-center pt-8 space-y-6">
                      {predictedFit ? (
                        <div className="text-center space-y-4">
                          <span className="text-xs text-slate-500 uppercase tracking-widest font-semibold block">
                            Evaluated Fit Status
                          </span>
                          <Badge
                            className={`px-8 py-3 text-xl font-black tracking-wide rounded-xl shadow-md ${
                              predictedFit.toLowerCase() === "fit"
                                ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/30"
                                : predictedFit.toLowerCase().includes("partial")
                                ? "bg-amber-500/10 text-amber-400 border border-amber-500/30"
                                : "bg-rose-500/10 text-rose-400 border border-rose-500/30"
                            }`}
                          >
                            {predictedFit}
                          </Badge>
                        </div>
                      ) : (
                        <div className="border border-dashed border-slate-800 rounded-lg w-full flex items-center justify-center text-slate-600 text-sm italic h-44">
                          {jobFitLoading ? "Evaluating Alignment..." : "Enter details and click Evaluate."}
                        </div>
                      )}
                    </CardContent>
                  </div>
                  <CardFooter className="border-t border-slate-800/60 p-4">
                    <Button
                      onClick={handleDetermineFit}
                      disabled={jobFitLoading || !fitResumeText.trim() || !jobDescriptionText.trim() || !apiOnline}
                      className="w-full bg-indigo-600 hover:bg-indigo-500 font-semibold"
                    >
                      {jobFitLoading ? (
                        <>
                          <RefreshCw className="h-4 w-4 animate-spin mr-2" />
                          Running analysis...
                        </>
                      ) : (
                        "Evaluate Fit"
                      )}
                    </Button>
                  </CardFooter>
                </Card>
              </div>
            </div>
          )}

          {/* TAB 5: EVALUATION DASHBOARD */}
          {activeTab === "dashboard" && (
            <div className="max-w-6xl mx-auto space-y-8">
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div className="space-y-1">
                  <h2 className="text-2xl font-bold tracking-tight text-slate-100">Model Evaluation & Benchmark</h2>
                  <p className="text-slate-400 text-sm">
                    Upload evaluation datasets to grade summary quality, classification accuracy, and alignment drift.
                  </p>
                </div>
                <div className="flex items-center gap-3">
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={loadDemoEvaluationCases}
                    className="text-xs bg-slate-900 border-slate-800 hover:bg-slate-800"
                  >
                    Load Demo Dataset
                  </Button>
                  <Button
                    size="sm"
                    variant="outline"
                    onClick={() => fileInputRef.current?.click()}
                    className="text-xs bg-slate-900 border-slate-800 hover:bg-slate-800 flex items-center gap-1.5"
                  >
                    <Upload className="h-3.5 w-3.5" />
                    Upload JSON
                  </Button>
                  <input
                    type="file"
                    accept=".json"
                    ref={fileInputRef}
                    onChange={handleFileUpload}
                    className="hidden"
                  />
                  <Button
                    size="sm"
                    onClick={handleRunEvaluation}
                    disabled={runningEval || !evalCasesRaw.trim() || !apiOnline}
                    className="text-xs bg-indigo-600 hover:bg-indigo-500 font-semibold flex items-center gap-1.5"
                  >
                    <Play className={`h-3.5 w-3.5 ${runningEval ? "animate-spin" : ""}`} />
                    Run Benchmark
                  </Button>
                </div>
              </div>

              {/* JSON text field & metrics cards */}
              <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                {/* Dataset Input */}
                <Card className="bg-slate-900 border-slate-800 lg:col-span-1">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-sm font-semibold text-slate-300">Dataset JSON Configurations</CardTitle>
                    <CardDescription className="text-xs">Paste your `evaluation_cases.json` array here.</CardDescription>
                  </CardHeader>
                  <CardContent>
                    <Textarea
                      placeholder='[{"task": "classify-section", "input": "...", "expected": "Experience"}]'
                      value={evalCasesRaw}
                      onChange={(e) => setEvalCasesRaw(e.target.value)}
                      className="w-full h-80 bg-slate-950 border-slate-800 text-[11px] font-mono text-slate-300 focus-visible:ring-indigo-600"
                    />
                  </CardContent>
                </Card>

                {/* Benchmark Metrics cards */}
                <Card className="bg-slate-900 border-slate-800 lg:col-span-2 flex flex-col justify-between">
                  <CardHeader className="pb-3">
                    <CardTitle className="text-sm font-semibold text-slate-300">Task Performance Breakdown</CardTitle>
                    <CardDescription className="text-xs">Real-time metrics grading predictions against ground truths.</CardDescription>
                  </CardHeader>
                  <CardContent className="space-y-4 flex-1">
                    {/* Progress indicator */}
                    {runningEval && (
                      <div className="space-y-2 p-3 bg-slate-950 rounded-lg border border-slate-800">
                        <div className="flex justify-between text-xs font-semibold">
                          <span className="text-indigo-400 flex items-center gap-2">
                            <RefreshCw className="h-3.5 w-3.5 animate-spin" />
                            Evaluating Cases...
                          </span>
                          <span>
                            {evalProgressCurrent} / {evalProgressTotal} ({Math.round((evalProgressCurrent / evalProgressTotal) * 100)}%)
                          </span>
                        </div>
                        <Progress value={(evalProgressCurrent / evalProgressTotal) * 100} className="h-2 bg-indigo-950" />
                      </div>
                    )}

                    {/* Overall Accuracy Card */}
                    <div className="grid grid-cols-2 md:grid-cols-5 gap-3">
                      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center flex flex-col justify-center min-h-[90px] shadow-sm">
                        <span className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">
                          Accuracy
                        </span>
                        <span className={`text-2xl font-black mt-1 ${evalStats.overallPct >= 80 ? "text-emerald-400" : evalStats.overallPct >= 50 ? "text-amber-400" : "text-slate-400"}`}>
                          {evalResults.length > 0 ? `${evalStats.overallPct}%` : "--"}
                        </span>
                        <span className="text-[9px] text-slate-500">
                          {evalStats.passedTotal} / {evalStats.total} Passed
                        </span>
                      </div>

                      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center flex flex-col justify-center min-h-[90px] shadow-sm">
                        <span className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">
                          Summary Passes
                        </span>
                        <span className="text-lg font-bold text-slate-200 mt-1">
                          {evalStats.stats["summary"].total > 0 ? `${evalStats.stats["summary"].pct}%` : "--"}
                        </span>
                        <span className="text-[9px] text-slate-500">
                          {evalStats.stats["summary"].passed} / {evalStats.stats["summary"].total}
                        </span>
                      </div>

                      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center flex flex-col justify-center min-h-[90px] shadow-sm">
                        <span className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">
                          Review Passes
                        </span>
                        <span className="text-lg font-bold text-slate-200 mt-1">
                          {evalStats.stats["review"].total > 0 ? `${evalStats.stats["review"].pct}%` : "--"}
                        </span>
                        <span className="text-[9px] text-slate-500">
                          {evalStats.stats["review"].passed} / {evalStats.stats["review"].total}
                        </span>
                      </div>

                      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center flex flex-col justify-center min-h-[90px] shadow-sm">
                        <span className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">
                          Section Acc
                        </span>
                        <span className="text-lg font-bold text-slate-200 mt-1">
                          {evalStats.stats["classify-section"].total > 0 ? `${evalStats.stats["classify-section"].pct}%` : "--"}
                        </span>
                        <span className="text-[9px] text-slate-500">
                          {evalStats.stats["classify-section"].passed} / {evalStats.stats["classify-section"].total}
                        </span>
                      </div>

                      <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 text-center flex flex-col justify-center min-h-[90px] shadow-sm">
                        <span className="text-[10px] text-slate-500 uppercase tracking-widest font-semibold">
                          Job Fit Acc
                        </span>
                        <span className="text-lg font-bold text-slate-200 mt-1">
                          {evalStats.stats["job-fit"].total > 0 ? `${evalStats.stats["job-fit"].pct}%` : "--"}
                        </span>
                        <span className="text-[9px] text-slate-500">
                          {evalStats.stats["job-fit"].passed} / {evalStats.stats["job-fit"].total}
                        </span>
                      </div>
                    </div>
                  </CardContent>
                  <CardFooter className="bg-slate-950/20 border-t border-slate-800 p-4 text-[10px] text-slate-500 italic">
                    Note: Generative tasks (Summary, Review) pass if inference runs successfully without backend timeout. Classification tasks require string equivalence match.
                  </CardFooter>
                </Card>
              </div>

              {/* Benchmarking Log Table */}
              {evalResults.length > 0 && (
                <Card className="bg-slate-900 border-slate-800 overflow-hidden">
                  <CardHeader className="flex flex-row items-center justify-between pb-3 border-b border-slate-800">
                    <div>
                      <CardTitle className="text-sm font-semibold text-slate-300">Run Log</CardTitle>
                      <CardDescription className="text-xs">Detailed records for case logs.</CardDescription>
                    </div>
                    {/* Task type filter */}
                    <div className="flex gap-2">
                      {["all", "summary", "review", "classify-section", "job-fit"].map((f) => (
                        <button
                          key={f}
                          onClick={() => setEvalSelectedTaskFilter(f)}
                          className={`px-2.5 py-1 rounded text-[10px] font-semibold border capitalize transition-all ${
                            evalSelectedTaskFilter === f
                              ? "bg-indigo-600 text-white border-indigo-500"
                              : "bg-slate-950 border-slate-800 text-slate-400 hover:text-white"
                          }`}
                        >
                          {f === "classify-section" ? "Section" : f === "job-fit" ? "Job Fit" : f}
                        </button>
                      ))}
                    </div>
                  </CardHeader>
                  <CardContent className="p-0">
                    <Table>
                      <TableHeader className="bg-slate-950/60 border-b border-slate-800">
                        <TableRow className="border-b border-slate-800">
                          <TableHead className="text-[10px] font-bold text-slate-400 w-24">Task</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-44">Input Sample</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-32">Expected</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-32">Actual Response</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-16 text-center">Status</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-20 text-right">Time</TableHead>
                          <TableHead className="text-[10px] font-bold text-slate-400 w-16 text-center">Inspect</TableHead>
                        </TableRow>
                      </TableHeader>
                      <TableBody>
                        {filteredEvalResults.map((r) => (
                          <TableRow key={r.id} className="border-b border-slate-800/40 text-xs hover:bg-slate-800/30">
                            <TableCell className="font-semibold capitalize text-slate-400">{r.task === "section" ? "Section Classification" : r.task === "job_fit" ? "Job Fit" : r.task}</TableCell>
                            <TableCell className="max-w-xs truncate text-slate-300 font-mono text-[11px]">{r.input}</TableCell>
                            <TableCell className="max-w-[120px] truncate text-slate-400 font-mono text-[11px]">{r.expected}</TableCell>
                            <TableCell className="max-w-[120px] truncate text-slate-300 font-mono text-[11px]">{r.actual}</TableCell>
                            <TableCell className="text-center">
                              <span className={`px-2 py-0.5 rounded-full text-[9px] font-extrabold ${r.status === "pass" ? "bg-emerald-500/10 text-emerald-400 border border-emerald-500/20" : "bg-rose-500/10 text-rose-400 border border-rose-500/20"}`}>
                                {r.status.toUpperCase()}
                              </span>
                            </TableCell>
                            <TableCell className="text-right font-mono text-slate-400">{r.latency > 0 ? `${Math.round(r.latency)}ms` : "N/A"}</TableCell>
                            <TableCell className="text-center">
                              <Button
                                size="sm"
                                variant="ghost"
                                onClick={() => setSelectedInspectResult(r)}
                                className="h-7 w-7 p-0 hover:bg-slate-800 text-indigo-400"
                              >
                                <Info className="h-4 w-4" />
                              </Button>
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </CardContent>
                </Card>
              )}
            </div>
          )}
        </main>

        {/* BOTTOM REAL-TIME DEVELOPER CONSOLE LOG DRAWER */}
        {showLogs && (
          <footer className="h-60 bg-slate-950 border-t border-slate-800 flex flex-col overflow-hidden z-10 shadow-[0_-5px_15px_rgba(0,0,0,0.5)]">
            {/* Header */}
            <div className="h-9 bg-slate-900 border-b border-slate-800 px-6 flex items-center justify-between">
              <div className="flex items-center gap-2 text-[10px] font-extrabold uppercase tracking-widest text-slate-400">
                <Terminal className="h-3.5 w-3.5 text-indigo-500" />
                <span>Developer Server Console Logs</span>
              </div>
              <button
                onClick={() => setLogs([])}
                className="text-[9px] text-slate-500 hover:text-slate-300 font-semibold flex items-center gap-1"
              >
                Clear Console
              </button>
            </div>

            {/* Console output */}
            <div className="flex-1 p-4 font-mono text-[10px] overflow-y-auto space-y-1 bg-black/90">
              {logs.length > 0 ? (
                logs.map((l) => (
                  <div key={l.id} className="flex gap-2 leading-relaxed border-b border-slate-900/50 pb-0.5">
                    <span className="text-slate-500">[{l.timestamp}]</span>
                    <span className={`font-bold ${l.status === 200 ? "text-emerald-500" : "text-rose-500"}`}>
                      {l.method} {l.path}
                    </span>
                    <span className="text-slate-400">| Status: {l.status}</span>
                    <span className="text-slate-400">| Round-Trip: {Math.round(l.latency)}ms</span>
                    {l.processTime > 0 && <span className="text-indigo-400">| Backend: {l.processTime.toFixed(1)}ms</span>}
                    {l.gpuAllocated > 0 && <span className="text-amber-500">| GPU Alloc: {l.gpuAllocated} MB</span>}
                    {l.error && <span className="text-rose-400 font-semibold">| Error: {l.error}</span>}
                  </div>
                ))
              ) : (
                <div className="text-slate-600 italic text-center pt-8">
                  Console idle. Run inferences or benchmarks to stream logs here.
                </div>
              )}
            </div>
          </footer>
        )}
      </div>

      {/* INSPECT CASE DIALOG DETAIL MODAL */}
      <Dialog open={selectedInspectResult !== null} onOpenChange={(open) => !open && setSelectedInspectResult(null)}>
        <DialogContent className="bg-slate-900 border-slate-800 text-slate-100 max-w-2xl max-h-[85vh] overflow-y-auto">
          <DialogHeader className="border-b border-slate-800 pb-3">
            <DialogTitle className="text-sm font-bold uppercase tracking-wider text-slate-400 flex items-center gap-2">
              <Info className="h-4 w-4 text-indigo-400" /> Inspect Case Details
            </DialogTitle>
          </DialogHeader>
          {selectedInspectResult && (
            <div className="space-y-4 pt-3 text-xs">
              <div className="grid grid-cols-2 gap-4 bg-slate-950 p-3 rounded-lg border border-slate-800 font-mono text-[10px]">
                <div>
                  <span className="text-slate-500 block">Task:</span>
                  <span className="font-bold text-slate-200 capitalize">{selectedInspectResult.task}</span>
                </div>
                <div>
                  <span className="text-slate-500 block">Status:</span>
                  <span className={`font-bold uppercase ${selectedInspectResult.status === "pass" ? "text-emerald-400" : "text-rose-400"}`}>{selectedInspectResult.status}</span>
                </div>
                <div>
                  <span className="text-slate-500 block">API Round-Trip Latency:</span>
                  <span className="font-bold text-slate-200">{Math.round(selectedInspectResult.latency)} ms</span>
                </div>
                <div>
                  <span className="text-slate-500 block">VRAM Usage:</span>
                  <span className="font-bold text-slate-200">{selectedInspectResult.gpuAllocated} MB</span>
                </div>
              </div>

              <div className="space-y-1.5">
                <span className="font-semibold text-slate-400">Case Input:</span>
                <pre className="bg-slate-950 p-3 rounded-lg border border-slate-850 overflow-x-auto text-[11px] font-mono text-slate-300 leading-normal max-h-40 overflow-y-auto whitespace-pre-wrap">
                  {selectedInspectResult.input}
                </pre>
              </div>

              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div className="space-y-1.5">
                  <span className="font-semibold text-slate-400">Expected Ground Truth:</span>
                  <pre className="bg-slate-950 p-3 rounded-lg border border-slate-850 text-[11px] font-mono text-slate-400 leading-normal max-h-40 overflow-y-auto whitespace-pre-wrap">
                    {selectedInspectResult.expected}
                  </pre>
                </div>
                <div className="space-y-1.5">
                  <span className="font-semibold text-slate-400">Actual Adapter Output:</span>
                  <pre className={`bg-slate-950 p-3 rounded-lg border text-[11px] font-mono leading-normal max-h-40 overflow-y-auto whitespace-pre-wrap ${selectedInspectResult.status === "pass" ? "text-emerald-300 border-emerald-500/20" : "text-rose-300 border-rose-500/20"}`}>
                    {selectedInspectResult.actual}
                  </pre>
                </div>
              </div>

              {selectedInspectResult.error && (
                <div className="bg-rose-500/10 text-rose-400 p-3 rounded-lg border border-rose-500/20">
                  <span className="font-bold block mb-1">Execution Error:</span>
                  <p className="font-mono text-[10px]">{selectedInspectResult.error}</p>
                </div>
              )}
            </div>
          )}
        </DialogContent>
      </Dialog>
    </div>
  );
}
