from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

from db_models.utils import create_champ, get_all_champs

router = APIRouter()


class BaseORMModel(BaseModel):
    class Config:
        orm_mode = True


class Championship(BaseORMModel):
    name: str
    national: bool


@router.get("/", response_model=List[Championship])
def get_championships():
    return get_all_champs()


@router.post("/", status_code=201)
def create_championship(champ: Championship):
    return create_champ(name=champ.name, national=champ.national)
