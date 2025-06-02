# LangChainGraphGenUI

building generative UI applications with LangChain & LangGraph.

## Building a Gen UI App with Langchain Python

- Architecture diagram of chatbot we will be building:
  ![alt text](PythonGenUILangchain\PythonGenUILangchain.png)
- Frontend: Next.js
- Backend: Python/Langchain

- backend: commands
  - [Reference](https://docs.astral.sh/uv/guides/projects/#creating-a-new-project)
  - In addition to the files created by `uv init`, uv will create a virtual environment and uv.lock file in the root of your project the first time you run a project command, i.e., uv run, uv sync, or uv lock.
  - You can add dependencies to your pyproject.toml with the `uv add` command. This will also update the lockfile and project environment

```bash
uv init backend
cd backend
--- ran
$ uv sync
Using CPython 3.12.0
Creating virtual environment at: .venv
Resolved 1 package in 24ms
Audited in 0.05ms
---
$ uv add fastapi uvicorn pydantic
---
 uv add langchain-core langchain langgraph python-dotenv
--- upTO-Now-added-7-dependencies we needed.
uv add typer langgraph-cli
# https://github.com/fastapi/typer
$ uv add langchain-community
---
abhis@Tinku MINGW64 ~/Desktop/Langgraph/LangChainGraphGenUI/PythonGenUILangchain/backend (main)
$ source .venv/Scripts/activate
(backend)
abhis@Tinku MINGW64 ~/Desktop/Langgraph/LangChainGraphGenUI/PythonGenUILangchain/backend (main)
# $ activate the venv
```

- create a `gen_ui_backend` folder : where we will write our langchain/graph code and server code ..etc
  - `chain.py`: this is file where we implement langgraph chain.
    - define the state of the chain(`GenerativeUIState`), which can be passed through to each of the nodes.
    - Implement our graphFunction(`create_graph`) - which gives us an idea about different nodes and the flow our graph is going to take.
