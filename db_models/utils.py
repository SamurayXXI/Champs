from database import db
from db_models.models import Champ


def get_all_champs():
    return db.query(Champ).all()


def create_champ(name: str, national: bool):
    champ = Champ(name=name, national=national)
    db.add(champ)
    db.commit()
