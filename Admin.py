from fastapi import APIRouter

user_app= APIRouter(
    prefix= '/admin',
    tags=['admin']
)