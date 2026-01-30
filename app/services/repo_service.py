# app/services/repo_service.py

from app.core.github_client import get, post
from app.services.permission import can_push

def list_repos():
    response = get("/user/repos")
    repos = []

    for repo in response.json():
        repos.append({
            "name": repo["name"],
            "owner": repo["owner"]["login"],
            "permissions": repo["permissions"]
        })

    return repos

def create_branch(owner: str, repo: str, branch: str):
    repo_data = get(f"/repos/{owner}/{repo}").json()

    if not can_push(repo_data["permissions"]):
        return {"error": "Permission denied"}

    ref = get(f"/repos/{owner}/{repo}/git/ref/heads/main").json()
    sha = ref["object"]["sha"]

    return post(
        f"/repos/{owner}/{repo}/git/refs",
        {
            "ref": f"refs/heads/{branch}",
            "sha": sha
        }
    ).json()

def merge_branch(owner: str, repo: str, source: str, target: str):
    repo_data = get(f"/repos/{owner}/{repo}").json()

    if not can_push(repo_data["permissions"]):
        return {"error": "Permission denied"}

    return post(
        f"/repos/{owner}/{repo}/merges",
        {
            "base": target,
            "head": source
        }
    ).json()
