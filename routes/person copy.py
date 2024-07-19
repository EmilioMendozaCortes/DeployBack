from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List

person = APIRouter()
persons = []

# Modelo de personas
class personModel(BaseModel):
    id: str
    personas: str
    contrasena: str
    created_at: datetime = datetime.now()
    estatus: bool = False

# Ruta para obtener todos los personas
@person.get('/persons', response_model=List[personModel],tags=['Personas'])
def get_personas():
    return persons

# Ruta para agregar un nuevo persona
@person.post('/persons', response_model=personModel,tags=['Personas'])
def save_persons(insert_persons: personModel):
    persons.append(insert_persons)
    return insert_persons

# Ruta para buscar un persona por ID
@person.get('/persons/{person_id}', response_model=personModel,tags=['Personas'])
def get_persona_por_id(person_id: str):
    for person in persons:
        if person.id == person_id:
            return person
    return {"error": "Persona no encontrado"}

# Ruta para modificar un persona por ID
@person.put('/persons/{person_id}', response_model=personModel,tags=['Personas'])
def update_persona(person_id: str, updated_person: personModel):
    for i, person in enumerate(persons):
        if person.id == person_id:
            persons[i] = updated_person
            return updated_person
    return {"error": "Persona no encontrado para modificar"}

# Ruta para eliminar un persona por ID
@person.delete('/persons/{person_id}', response_model=personModel,tags=['Personas'])
def delete_persona(person_id: str):
    for i, person in enumerate(persons):
        if person.id == person_id:
            deleted_person = persons.pop(i)
            return deleted_person
    return {"error": "Persona no encontrado"}
