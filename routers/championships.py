from typing import List

from fastapi import APIRouter, Response
from pydantic import BaseModel

from db_models.utils import create_champ, get_all_champs, delete_champ, change_champ

router = APIRouter()


class BaseORMModel(BaseModel):
    class Config:
        orm_mode = True


class ChampionshipCreate(BaseORMModel):
    name: str
    national: bool


class Championship(ChampionshipCreate):
    id: int


@router.get("/", response_model=List[Championship])
def get_championships():
    return get_all_champs()


@router.post("/", status_code=201)
def create_championship(champ: ChampionshipCreate):
    return create_champ(name=champ.name, national=champ.national)


@router.delete("/{champ_id}",
    response_class=Response,
    responses={
        200: {"description": "Topic successfully deleted"},
        404: {"description": "Topic not found"},
    })
def delete_championship(champ_id: int):
    delete_champ(champ_id)
    return Response(status_code=200)


@router.put("/{champ_id}")
def change_championship(champ_id: int, new_champ: ChampionshipCreate):
    change_champ(champ_id, new_champ.dict())
