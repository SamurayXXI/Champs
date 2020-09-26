from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from db_models.utils import create_champ, get_all_champs

router = APIRouter()


class Championship(BaseModel):
    name: str
    national: bool

    class Config:
        orm_mode = True


@router.get("/", response_model=List[Championship])
def get_championships():
    return get_all_champs()


@router.post("/", status_code=201)
def create_championship(champ: Championship):
    return create_champ(name=champ.name, national=champ.national)
