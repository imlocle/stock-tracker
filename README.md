# 📈 Stock Tracker

Stock Tracker is a full-stack web application that provides real-time and historical stock market data using the [Alpha Vantage API](https://www.alphavantage.co/).  
It features a **FastAPI backend** and a **Next.js (React) frontend**, designed for speed, scalability, and a clean developer experience.

---

## 🚀 Tech Stack

**Frontend**

- Next.js (React + TypeScript)
- Framer Motion (animations)

**Backend**

- FastAPI (Python)
- Pydantic & Pydantic Settings
- Uvicorn (ASGI server)
- Requests (HTTP client)
- Alpha Vantage API (financial data source)

**Development Tools**

- Node.js + npm
- Python 3.10+ (recommended)
- `concurrently` for running backend + frontend
- `serve` for static frontend hosting

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/imlocle/stock-tracker.git
cd stock-tracker/
```

### 2. Create Python Environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Create `.env` file for backend

```bash
cd backend/
touch .env
```

### 4. Add these variables into the `.env` file:

```bash
ALPHAVANTAGE_API_KEY=<YOUR_API_KEY>
ALPHAVANTAGE_URL=https://www.alphavantage.co/query
DEBUG=True
BACKEND_URL=http://localhost:8000
FRONTEND_URL=http://localhost:3000
```

- Back to root directory

  ```bash
  cd ..
  ```

### 5. Install Dependencies

```bash
npm install
npm run setup
```

## Start Application:

```bash
npm run build
npm run start
```

This runs:

- 🧠 Backend → FastAPI at http://localhost:8000
- 💻 Frontend → Next.js at http://localhost:3000

## Development Mode

For live reloads and debugging:

```bash
npm run dev
```

## Dummy Data

- The backend includes `DUMMY_DATA` for testing without hitting the `Alpha Vantage API`.
- Currently includes symbols: `AMZN`, `AAPL`, `MSFT`, `GOOGL`, `TSLA`, `META`, `NVDA`, `NFLX`, `ADBE`, `ORCL`, `INTC`, `CSCO`, `PYPL`, `CRM`, `UBER`.
