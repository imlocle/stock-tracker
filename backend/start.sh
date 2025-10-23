#!/bin/bash

source ../.venv/bin/activate

# Start FastAPI in production mode
echo "🚀 Starting FastAPI backend..."
cd "$(dirname "$0")"
export PYTHONPATH=$(pwd)
uvicorn main:app --host 0.0.0.0 --port 8000
