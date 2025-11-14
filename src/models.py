from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import String, Boolean, Integer, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from typing import List

db = SQLAlchemy() 

character_weapon = db.Table('characteres_weapons', 
    db.Column('id', db.Integer, primary_Key=True),
    db.Column('character_id', db.Integer, db.ForeignKey("characteres.id"), nullable=False),
    db.Column('weapon_id', db.Integer, db.ForeignKey("weapons.id"), nullable=False))

class User(db.Model):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(50), nullable=False)
    create_at: Mapped[datetime] = mapped_column(DateTime)

    list_world: Mapped[list["World"]] =relationship(back_populates="user")
    list_character: Mapped[list["Character"]] =relationship(back_populates="user")

class World (db.Model):
    __tablename__ = 'worlds'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    population: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String(50))
    
    user_id: Mapped[int] =mapped_column(Integer, db.ForeignKey("users.id"), nullable=False)

    user: Mapped["User"] = relationship(back_populates="List_world")
    list_character: Mapped[list["Character"]] =relationship(back_populates="world")

class Character (db.Model):
    __tablename__ = 'characteres'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    gender: Mapped[str] = mapped_column(String)
    role: Mapped[str] = mapped_column(String)
    
    world_id: Mapped[int] =mapped_column(Integer, db.ForeignKey("worlds.id"), nullable=False)
    user_id: Mapped[int] =mapped_column(Integer, db.ForeignKey("users.id"), nullable=False)

    world: Mapped["World"] = relationship(back_populates="List_character")
    user: Mapped["User"] = relationship(back_populates="List_character")

    weapons: Mapped[List["Weapon"]] = relationship (back_populates="characteres", secondary= character_weapon)
                                                    

class Weapon (db.Model):
    __tablename__ = 'weapons'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    material: Mapped[str] = mapped_column(String)
    description: Mapped[str] = mapped_column(String (50))
    owner: Mapped[str] = mapped_column(String)
    

    characteres: Mapped[List["Character"]] = relationship (back_populates= "weapons", secondary= character_weapon)










