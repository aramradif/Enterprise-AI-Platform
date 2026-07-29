from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def root():
    """
    Root endpoint.
    """
    return {
        "status": "healthy",
        "service": "Enterprise AI Platform API",
        "version": "2.0.0",
    }


@router.get("/health")
async def health():
    """
    Health check endpoint.
    """
    return {"status": "ok"}