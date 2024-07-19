from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List

user = APIRouter()
users = []

# Modelo de usuarios
class UserModel(BaseModel):
    id: str
    usuarios: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus: bool = False

# Ruta de bienvenida
@user.get('/')
def bienvenido():
    return 'Bienvenido al sistema de APIs'

# Ruta para obtener todos los usuarios
@user.get('/users', response_model=List[UserModel],tags=['Usuarios'])
def get_usuarios():
    return users

# Ruta para agregar un nuevo usuario
@user.post('/users', response_model=UserModel,tags=['Usuarios'])
def save_users(insert_users: UserModel):
    users.append(insert_users)
    return insert_users

# Ruta para buscar un usuario por ID
@user.get('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
def get_usuario_por_id(user_id: str):
    for user in users:
        if user.id == user_id:
            return user
    return {"error": "Usuario no encontrado"}

# Ruta para modificar un usuario por ID
@user.put('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
def update_usuario(user_id: str, updated_user: UserModel):
    for i, user in enumerate(users):
        if user.id == user_id:
            users[i] = updated_user
            return updated_user
    return {"error": "Usuario no encontrado para modificar"}

# Ruta para eliminar un usuario por ID
@user.delete('/users/{user_id}', response_model=UserModel,tags=['Usuarios'])
def delete_usuario(user_id: str):
    for i, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(i)
            return deleted_user
    return {"error": "Usuario no encontrado"}
