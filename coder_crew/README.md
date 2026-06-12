# 🤖 Coder Crew

An AI-powered coding agent built with **CrewAI** that automatically writes, executes, and validates Python code in a sandboxed Docker environment.

## 📋 Overview

**Coder Crew** is a multi-agent system that leverages large language models (LLMs) to solve programming tasks autonomously. The `Senior Software Developer` agent analyzes your requirements, writes optimized Python code, executes it safely in Docker, and returns the results—all without manual intervention.

### Key Features

✅ **Autonomous Code Generation** - LLM writes production-ready Python code  
✅ **Safe Execution** - Sandboxed Docker environment prevents system damage  
✅ **Real Code Execution** - Actually runs code and returns live output  
✅ **Error Handling** - Automatic retries and timeout management  
✅ **Traceable Execution** - Full audit trail of agent decisions and tool usage  

---

## 🎯 Use Cases

### Development & Prototyping
- Generate boilerplate code quickly
- Prototype algorithms and data structures
- Create utility scripts without writing them manually

### Data Analysis
- Write data processing pipelines
- Generate statistical calculations
- Process CSV/JSON files programmatically

### Mathematical Computations
- Calculate numerical approximations (e.g., Leibniz series for π)
- Solve differential equations
- Run Monte Carlo simulations

### Education & Learning
- Generate example code for programming concepts
- Verify algorithm implementations
- Test mathematical formulas

### Automation Tasks
- Create deployment scripts
- Generate data transformation workflows
- Build utility tools for DevOps

---

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- Docker (running and accessible)
- An LLM API key (OpenAI, Claude, etc.)

### Basic Usage

```bash
uv run run_crew
```

---

## 💻 Example: Calculating π using Leibniz Series

### Input Task
```
Assignmant- Write a program to calculate the first 10,000 terms of this series, multiplying the total by 4: 1 - 1/3 + 1/5 - 1/7 + ... (Mathamatical formula to calculate pi)
Code_language- Python
```

### Generated Code
```python
def leibniz_pi(num_terms):
    total = 0.0
    for k in range(num_terms):
        denominator = 2 * k + 1
        term = ((-1) ** k) / denominator
        total += term
    return 4 * total

if __name__ == "__main__":
    terms = 10000
    approx_pi = leibniz_pi(terms)
    print(f"Approximation of pi using {terms} terms: {approx_pi:.15f}")
```

### Output
```
Approximation of pi using 10000 terms: 3.141492653590034
```

---

## 🔍 How It Works

```
User Input
    ↓
Crew Receives Task
    ↓
Senior Developer Agent Analyzes Requirements
    ↓
Agent Writes Python Code
    ↓
CodeInterpreterTool Executes in Docker
    ↓
Docker Container Runs Code Safely
    ↓
Output Returned to Agent
    ↓
Agent Formats Final Response
    ↓
Results Delivered to User
```

### Agent Execution Flow

1. **Task Reception** - Crew receives the coding task
2. **Analysis** - Agent understands requirements and constraints
3. **Code Generation** - LLM writes optimized Python code
4. **Tool Invocation** - CodeInterpreterTool prepares execution
5. **Safe Execution** - Docker container isolates code execution
6. **Result Capture** - Output, errors, and metrics collected
7. **Validation** - Agent reviews results and retries if needed
8. **Response** - Final formatted output delivered

---

## 🛠️ Advanced Features

### Enabling Tracing

Monitor agent decisions and tool usage:

```bash
# Enable tracing
crewai traces enable

# Or set in .env
CREWAI_TRACING_ENABLED=true
```

View traces at: `https://app.crewai.com/`

### Custom Tools

Add custom Python execution tools:

```python
from crewai.tools import tool

@tool
def custom_tool(input: str) -> str:
    """Description of what your tool does"""
    # Implementation
    return result
```

### Error Handling

The agent automatically:
- Retries failed code execution (up to 3 times)
- Catches runtime errors and analyzes them
- Suggests fixes based on error messages
- Enforces 30-second timeout on executions

---

## ⚙️ Environment Variables

```bash
# LLM Configuration
GROQ_API_KEY=your_openai_key

# CrewAI
CREWAI_TRACING_ENABLED=true
CREW_VERBOSE=true

```

---

## 🐛 Troubleshooting

### Docker Connection Error

**Problem:** `Error while fetching server API version`

**Solutions:**
```bash
# 1. Start Docker
sudo systemctl start docker

# 2. Fix permissions (Linux)
sudo usermod -aG docker $USER
newgrp docker

# 3. Verify socket exists
ls -l /var/run/docker.sock

# 4. Test Docker
docker ps
```
---

## 📊 Code Execution Modes

### Safe Mode (Recommended)
```python
code_execution_mode='safe'  # Runs in Docker container
```

**Pros:** Isolated, prevents system damage  
**Cons:** Requires Docker

### Local Mode (Caution)
```python
# code_execution_mode='safe'  # Comment out to use local
```

**Pros:** No Docker dependency  
**Cons:** Code runs with your permissions—use only with trusted code

---

## 🤝 Contributing

Contributions welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open Pull Request

---

**Made with ❤️ using CrewAI**