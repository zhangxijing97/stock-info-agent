# stock-info-agent

This project is a sample implementation of a **multi-tool AI agent** built with the [Google Agent Development Kit (ADK)](https://github.com/google/adk). It provides real-time stock information using [Yahoo Finance](https://www.yahoofinance.com/) data via the `yfinance` Python library.

---

## 🚀 Features

- Get the **current stock price** of a company
- Retrieve the **company name** and **sector** info
- Keeps a simple record of recent ticker lookups (in-memory)
- Modular tool design with separate tool files
- ADK-powered agent using `gemini-2.0-flash` LLM model

---

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

---

## 🔧 Setup

```bash
# Clone the repo
git clone https://github.com/your-username/stock-info-agent.git
cd stock-info-agent

# Create a virtual environment (optional but recommended)
python -m venv .venv 
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🔐 Google API Key

Set your `GOOGLE_API_KEY` in a `.env` file before using the agent.  
You can obtain the key from [Google AI Studio](https://makersuite.google.com/app).

---

## 📜 License

MIT License. Feel free to fork and expand the agent!

---

## ✨ Future Ideas

- Add historical chart tool  
- Predict future prices using LLM  
- Integrate with a web frontend or API