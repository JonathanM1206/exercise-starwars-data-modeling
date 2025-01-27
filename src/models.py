import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String,Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True) 
    email = Column(String(25), nullable=False) 
    password = Column(String(30), nullable=False) 
    suscripcion_date=Column(Date,nullable=False) 
    name=Column(String(25),nullable=False) 
    last_name=Column(String(25),nullable=False) 
    def to_dict(self):
        return {}

class Planet(Base): 
    __tablename__ = 'planet' 
    id = Column(Integer, primary_key=True)  
    planet_name=Column(String(15),nullable=False) 
    planet_climate=Column(String(15),nullable=False) 
    orbital_period=Column(Integer,nullable=False) 
    planet_terrain=Column(String(15),nullable=False) 
    surface_water=Column(Integer,nullable=False)
    planet_residents=Column(Integer,nullable=False) 


    def to_dict(self):
        return {}
class Character(Base): 
    __tablename__ = 'character' 
    id = Column(Integer, primary_key=True)  
    birth_year=Column(String(25),nullable=False) 
    eye_color=Column(String(25), nullable=False) 
    character_name=Column(String(25),nullable=False) 
    species=Column(String(25),nullable=False) 
    hair_color=Column(String(10),nullable=False) 
    height=Column(Integer,nullable=False)
    
    def to_dict(self):
        return {}  

class Favorite(Base):  
    __tablename__ = 'favorite' 
    id = Column(Integer, primary_key=True) 
    planet_id=Column(Integer,ForeignKey('planet.id')) 
    character_id=Column(Integer,ForeignKey('character.id')) 
    user_id=Column(Integer,ForeignKey('user.id'))
     
    def to_dict(self):
        return {}  
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
