from fastapi import APIRouter
from app.api.routes import repos, branches, deploy

router = APIRouter()
router.include_router(repos.router)
router.include_router(branches.router)
router.include_router(deploy.router)
