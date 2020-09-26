from sqlalchemy import Column, Integer, String, Boolean

from database import Base


class Champ(Base):

    __tablename__ = "champ"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    national = Column(Boolean)
