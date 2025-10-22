from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.api import routes

app = FastAPI(title="Stock Summaries Backend")

# Allow CORS
origins = [
    "http://localhost:3000",  # Frontend dev
    # Add more origins if needed, e.g., production URLs
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or ["*"] to allow all (not recommended in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(routes.router)


@app.get("/")
def root():
    return {"message": "Stock Summaries Backend is running!"}
