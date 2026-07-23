from fastapi import APIRouter

from app.core.config import settings

router = APIRouter()

@router.get("/")
def root():
    return {
        "message": f"Welcome to {settings.app_name}",
        "version": settings.app_version,
    }


@router.get("/health")
def health():
    return {
        "status": "healthy",
        "environment": settings.environment,
    }


@router.get("/version")
def version():
    return {
        "app": settings.app_name,
        "version": settings.app_version,
    }
