from database import db
from db_models.models import Champ


def get_all_champs():
    return db.query(Champ).all()


def create_champ(name: str, national: bool):
    champ = Champ(name=name, national=national)
    db.add(champ)
    db.commit()


def delete_champ(champ_id: int):
    champ = db.query(Champ).get(champ_id)
    db.delete(champ)
    db.commit()


def change_champ(champ_id: int, new_champ: dict):
    db.query(Champ).filter_by(id=champ_id).update(new_champ)
    db.commit()
