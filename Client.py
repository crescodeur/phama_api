from fastapi import APIRouter
from . import models, schemas
from sqlalchemy.orm import Session
from passlib.context import CryptContext

client_app = APIRouter(
    prefix= '/client',
    tags=['client']
)


@client_app.post('/')
async def inscriription(db: Session, client: schemas.ClientCreate):
    pass