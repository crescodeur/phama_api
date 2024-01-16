from database import Base, engine, SessionLocal
from sqlalchemy import  Boolean, Column, ForeignKey, Integer, String, Text, Float
# from sqlalchemy_utils import ChoiceType
from sqlalchemy.orm import relationship

class Client(Base):
    __tablename__='client'
    id= Column(Integer, primary_key=True)
    username= Column(String(25),unique=True)
    email=Column(String(25),unique=True)
    password= Column(Text(),nullable=False)
    is_staff= Column(Boolean,default=False)
    is_active= Column(Boolean,default=True)

    order = relationship('commande',back_populates='users')


class Commande(Base):
    __tablename__ = 'commande'
    id = Column(Integer, primary_key=True)
    quantite = Column(Integer, nullable=False)
    
    user_id = Column(Integer, ForeignKey('users.id', nullable=False))
    users = relationship('client', back_populates='order')

class Produit(Base):
    __tablename__= 'Produit'
    id = Column(Integer, primary_key=True)
    nom= Column(String(30),unique=True)
    qtestock= Column(Integer, nullable=False)
    prix = Column(Float,nullable=False)