from enum import Enum

from fastapi import APIRouter

router = APIRouter(prefix="/s1", tags=["S1"])


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


@router.get("/medical_staff")
def index(q):
    return "medical_staff"
