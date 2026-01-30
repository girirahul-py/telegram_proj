
# app/api/routes/repos.py

from fastapi import APIRouter
from app.services.repo_service import list_repos

router = APIRouter()

@router.get("/repos")
def get_repos():
    return list_repos()
