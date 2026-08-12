# LangChain - Developing AI Agents with LangChain & LangGraph

This repository takes you through 5 real-world AI agent projects, from simple hello-world applications to advanced agentic systems:

| Project | Branch | Description |
|---------|------|-------------|
| 👋 [LangChain Hello World](https://github.com/evastevanovic/langchain/tree/project/hello-world) | `project/hello-world` | Your first AI agent - basic structure and LLM integration |
| 🔎 [Modern Search Agent](https://github.com/evastevanovic/langchain/tree/project/search-agent) | `project/search-agent` | Build search agents using custom tools, search integrations, and structured outputs |
| 🧠 [Agents Under The Hood](https://github.com/evastevanovic/langchain/tree/project/agents-under-the-hood) | `project/agents-under-the-hood` | Understanding reasoning and acting patterns in AI agents |
| 📄 [RAG Gist](https://github.com/evastevanovic/langchain/tree/project/rag-gist) | `project/rag-gist` | The gist of retrieval-augmented generation (RAG) |
| 🛠️ [ReAct & Function Calling](https://github.com/evastevanovic/langchain/tree/project/react-function-calling) | `project/react-function-calling` | Implement ReAct logic and tool/function calling capabilities in LangChain |

## 📚 Project Highlights 

- **5 Complete Projects** - Ranging from beginner concepts to advanced agent workflows.
- **Real-World Applications** - Build agents that solve actual problems with live APIs.
- **Modern Tech Stack** - LangChain v0.3+, LangGraph, and Vector Databases.
- **Practical Skills** - Learn RAG, prompt engineering, tool calling, and agentic workflows.
- **Interactive Learning** - Follow the branches chronologically to build out your understanding step-by-step.

### Phase 1: Foundations
1. **Hello World** - Basic agent structure and LLM integration.
2. **Agents Under The Hood** - Learn the fundamental mechanics of how AI agents reason and act.

### Phase 2: RAG & Tools
3. **RAG Gist** - Introduction to Retrieval-Augmented Generation and vector data handling.
4. **Search Agent** - Equipping agents with search tools to retrieve real-time information.

### Phase 3: Advanced Concepts
5. **ReAct & Function Calling** - Mastering the ReAct framework and giving LLMs the ability to execute functional code and APIs.

## ▶️ Getting Started 

### 🛠️ Prerequisites 
- Python 3.10+
- Any Python package manager (uv, poetry, pipenv) - but NOT conda!
- Access to an LLM API (can be open source via Ollama, or cloud providers like OpenAI, Anthropic, Gemini).

### ⚙️ Setup Instructions 

1. **Clone the repository**
   ```bash
   git clone https://github.com/evastevanovic/langchain.git
   cd langchain
   ```
   
2. **For branch-based projects:**
   ```bash
   # Start with Hello World
   git checkout project/hello-world
   uv sync
   uv run python main.py
   ```
   
   **Configure Environment Variables** - Create a .env file in the project root:

   ```
   TAVILY_API_KEY=your_tavily_api_key
   
    # Optional: LangSmith Tracing
    LANGSMITH_TRACING=true
    LANGSMITH_API_KEY=your_langsmith_api_key
   ```
