from fastapi import APIRouter

from models.user import User
from config.db import conn
from schemas.user import serializeDict, serializeList
from bson import ObjectId
user = APIRouter()

@user.get('/')
async def find_all_users():
    return serializeList(conn.local.user.find())

@user.get('/{id}')
async def find_all_users(id,user: User):
    return serializeDict(conn.local.user.find_one({"_id":ObjectId(id)}))

@user.post('/')
async def create_user(user: User):
    conn.local.user.insert_one(dict(user))
    return serializeList(conn.local.user.find())

@user.post('/{id}')
async def update_user(id,user: User):
    conn.local.user.find_one_and_update({"_id":ObjectId(id)},{
        "$set":dict(user)
    })
    return serializeList(conn.local.user.find({"_id":ObjectId(id)}))

user.delete('/{id}')
async def delete_user(id,user: User):
    return serializeList(conn.local.user.find_one_and_delete({"_id":ObjectId(id)}))

def serializeDict(a) -> dict:
    return{**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]