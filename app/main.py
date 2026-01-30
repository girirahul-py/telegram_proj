#app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.router import router
from app.core.config import GITHUB_TOKEN

## --- Initialize FastAPI Application ---

app = FastAPI(
    title="GitHub Repository Control",
    description="Permission-Aware Multi-Repo Deployment Automation Platform",
    version="1.0.0",
)

## --- Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## --- Include API Router ---

app.include_router(router, prefix="/api/v1")


## --- Root Endpoint ---
# @app.get("/")
# def root():
#     return {"message": "Welcome to the GitHub Repository Control API"}