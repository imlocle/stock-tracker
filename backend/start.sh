#!/bin/bash
# Start FastAPI in production mode

echo "🚀 Starting FastAPI backend..."
uvicorn main:app --host 0.0.0.0 --port 8000
