# app/api/routes/deploy.py

from fastapi import APIRouter
from app.services.deploy_service import trigger_deploy

router = APIRouter()

@router.post("/deploy")
def deploy(owner: str, repo: str):
    return trigger_deploy(owner, repo)
