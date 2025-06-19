# stock-info-agent

This project is a sample implementation of a **multi-tool AI agent** built with the [Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/). It provides real-time stock information using [Yahoo Finance](https://pypi.org/project/yahoo-finance/) data via the `yfinance` Python library.

## 🚀 Features

- Get the **current stock price** of a company
- Retrieve the **company name** and **sector** info
- Keeps a simple record of recent ticker lookups (in-memory)
- Modular tool design with separate tool files
- ADK-powered agent using `gemini-2.0-flash` LLM model

## 🧱 Project Structure

```
├── agent.py
├── tools/
│ ├── init.py
│ ├── stock_info.py # Tool for company name & sector
│ └── stock_price.py # Tool for stock price with memory
├── requirements.txt
└── README.md
```

## 🔧 Setup

```bash
# Clone the repo
git clone git@github.com:zhangxijing97/stock-info-agent.git
cd stock-info-agent

# Create a virtual environment (optional but recommended)
python -m venv .venv 
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🔐 Google API Key

Before running the agent, you need to create a `.env` file and set your `GOOGLE_API_KEY`.

You can obtain your key from [Google AI Studio](https://makersuite.google.com/app).

### 📝 Create the `.env` file

Inside the `app/` directory, run the following commands in your terminal:

```bash
echo "GOOGLE_GENAI_USE_VERTEXAI=0" > app/.env
echo "GOOGLE_API_KEY=your_google_api_key_here" >> app/.env
```

## ▶️ Run the Agent

Once setup is complete and you've added your API key in .env, you can start the agent:

```
Usage: adk [OPTIONS] COMMAND [ARGS]...

  Agent Development Kit CLI tools.

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  api_server  Starts a FastAPI server for agents.
  create      Creates a new app in the current folder with prepopulated agent template.
  deploy      Deploys agent to hosted environments.
  eval        Evaluates an agent given the eval sets.
  run         Runs an interactive CLI for a certain agent.
  web         Starts a FastAPI server with Web UI for agents.
```

Example queries:

```
What is the current price of AAPL?  
Tell me about the company behind MSFT.
```

## 📜 License

MIT License. Feel free to fork and expand the agent!