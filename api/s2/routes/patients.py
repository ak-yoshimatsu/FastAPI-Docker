from fastapi import APIRouter

router = APIRouter(prefix="/patients", tags=["s2"])


@router.get("/{str}")
def index(str: str):
    return {"data": str}
