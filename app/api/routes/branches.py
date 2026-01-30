# app/api/routes/branches.py


from fastapi import APIRouter
from app.services.repo_service import create_branch, merge_branch

router = APIRouter()

@router.post("/branch/create")
def create(owner: str, repo: str, branch: str):
    return create_branch(owner, repo, branch)

@router.post("/branch/merge")
def merge(owner: str, repo: str, source: str, target: str):
    return merge_branch(owner, repo, source, target)
