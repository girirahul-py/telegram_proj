# app/services/deploy_service.py
from app.core.github_client import post

def trigger_deploy(owner: str, repo: str):
    return post(
        f"/repos/{owner}/{repo}/dispatches",
        {
            "event_type": "deploy"
        }
    ).json()
