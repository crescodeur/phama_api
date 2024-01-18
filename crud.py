from . import models, schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str):
    return pwd_context.hash(password)

#CRUD client=================================
def get_client(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.id == client_id).first()

def get_client_by_email(db: Session, email: str):
    return db.query(models.Client).filter(models.Client.email == email).first()

def get_client_by_username(db: Session, username: str):
    return db.query(models.Client).filter(models.Client.username == username).first()

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def create_client(db: Session, client: schemas.ClientCreate):
    hashed_password = get_password_hash(client.password)
    db_client = models.Client(username=client.username, email=client.email, password= hashed_password)
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client


#CRUD Produit=================================
def get_produit(db: Session, prod_id: int):
    return db.query(models.Produit).filter(models.Produit.id == prod_id).first()

def get_produit(db: Session, prod_nom: str):
    return db.query(models.Produit).filter(models.Produit.nom == prod_nom).first()

def create_produit(db: Session, produit: schemas.ProduitCreate):
    db_prod = models.Produit(nom= produit.nom, qtestock= produit.qtestock, prix= produit.prix)
    db.add(db_prod)
    db.commit()
    db.refresh(db_prod)
    return db_prod
