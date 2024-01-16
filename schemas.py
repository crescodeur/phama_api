from pydantic import BaseModel

class ClientBase(BaseModel):
    username: str
    email: str
    password: str
      

class ClientCreate(ClientBase):
    pass


class Client(ClientBase):
    id: int
    is_active: bool
    is_staff: bool

    class Config:
        orm_mode= True



class CommandeBase(BaseModel):
    quantite:int
    

class CommandeCreate(CommandeBase):
    pass

class Commande(CommandeBase):
    id: int
    user_id: int

    class Config:
        orm_mode= True

class ProduitBase(BaseModel):
    nom: str
    qtestock: int
    prix: float

class ProduitCreate(ProduitBase):
    pass

class Produit(ProduitBase):
    id: int

    class Config:
        orm_mode = True