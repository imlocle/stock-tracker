# Stock Tracker API

This is the backend for the Stock Tracker application. It provides endpoints to fetch company overviews, historical stock prices, and income statements. The backend is built with **FastAPI** and can use either **Alpha Vantage API** or **dummy data** for testing purposes.

---

## Features

- Fetch **company overview** by stock symbol
- Fetch **daily historical stock prices**
- Handles **API limits** and provides fallback to dummy data
- Provides **error handling** for invalid symbols and API rate limits

---

## Tech Stack

- Python 3.11+
- FastAPI
- HTTPX (async requests)
- Pydantic (data validation)
- Uvicorn (ASGI server)

## Installation

1. Create Python Environment
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```
2. Install Dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Create Environment Varibles

1. Create a `.env` file in the project root:
   ```bash
   touch .env
   ```
2. Add these variables into `.env`
   ```bash
   ALPHAVANTAGE_API_KEY=<YOUR_API_KEY>
   ALPHAVANTAGE_URL=https://www.alphavantage.co/query
   DEBUG=True
   BACKEND_URL=http://localhost:8000
   FRONTEND_URL=http://localhost:3000
   ```

## Running the Server

Start the backend using Uvicorn:

```bash
uvicorn main:app --reload
```

## Dummy Data

- The backend includes `DUMMY_DATA` for testing without hitting the `Alpha Vantage API`.
- Currently includes symbols: `AMZN`, `AAPL`, `MSFT`, `GOOGL`, `TSLA`, `META`, `NVDA`, `NFLX`, `ADBE`, `ORCL`, `INTC`, `CSCO`, `PYPL`, `CRM`, `UBER`.
