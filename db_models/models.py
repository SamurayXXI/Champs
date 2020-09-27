from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date

from database import Base


class Champ(Base):

    __tablename__ = "champ"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    national = Column(Boolean)


class Season(Base):

    __tablename__ = "season"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    champ_id = Column(Integer, ForeignKey("champ.id"))


class Country(Base):

    __tablename__ = "country"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)


class Club(Base):

    __tablename__ = "club"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    city = Column(String)
    country_id = Column(Integer, ForeignKey("country.id"))


class Match(Base):

    __tablename__ = "match"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    home_team_id = Column(Integer, ForeignKey("club.id"))
    away_team_id = Column(Integer, ForeignKey("club.id"))
    home_team_score = Column(Integer)
    away_team_score = Column(Integer)
    season_id = Column(Integer, ForeignKey("season.id"), index=True)
    match_day = Column(Integer)


class Table(Base):

    __tablename__ = "table"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    season_id = Column(Integer, ForeignKey("season.id"), index=True)
    club_id = Column(Integer, ForeignKey("club.id"))
    games = Column(Integer)
    wins = Column(Integer)
    draw = Column(Integer)
    lose = Column(Integer)
    goal_for = Column(Integer)
    goal_against = Column(Integer)
    points = Column(Integer, index=True)


class Footballer(Base):

    __tablename__ = "footballer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    birth_day = Column(Date)
    country_id = Column(Integer, ForeignKey("country.id"))
    club_id = Column(Integer, ForeignKey("club.id"))


class Goal(Base):

    __tablename__ = "goal"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    footballer_id = Column(Integer, ForeignKey("footballer.id"), index=True)
    match_id = Column(Integer, ForeignKey("match.id"), index=True)
    club_id = Column(Integer, ForeignKey("club.id"))
    minute = Column(Integer)
    is_penalty = Column(Boolean)
    is_autogoal = Column(Boolean)
    assist_footballer_id = Column(Integer, ForeignKey("footballer.id"), index=True)
