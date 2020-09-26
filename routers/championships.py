from typing import List

from fastapi import APIRouter
from pydantic import BaseModel


router = APIRouter()


class Championship(BaseModel):
    id: int
    name: str
    national: bool


@router.get("/", response_model=List[Championship])
def get_championships():
    return {"id": 1, "name": "Russia", "national": True}


@router.post("/", status_code=201)
def create_championship(champ: Championship):
    return champ
