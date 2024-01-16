from fastapi import APIRouter

prod_app= APIRouter(
    prefix= '/admin',
    tags=['admin']
)

# @prod_app.post('/')