# Emilio Mendoza Cortes 9B IDGS
import models.rols
import schemas.rols
from sqlalchemy.orm import Session
import models, schemas

# Busqueda por id
def get_rol(db:Session, id: int):
    return db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()

# Busqueda por USUARIO
def get_rol_by_nombre(db:Session, nombre: str):
    return db.query(models.rols.Rol).filter(models.rols.Rol.Nombre == nombre).first()

# Buscar todos los nombres
def get_rols(db:Session, skip: int=0, limit:int=10):
    return db.query(models.rols.Rol).offset(skip).limit(limit).all()

# Crear nuevo nombre
def create_rol(db:Session, rol: schemas.rols.RolCreate):
    db_rol = models.rols.Rol(Nombre=rol.Nombre, 
                            Descripcion=rol.Descripcion,
                            # Contrasena=rol.Contrasena, 
                            Estatus=rol.Estatus, 
                            Fecha_Registro=rol.Fecha_Registro, 
                            Fecha_Actualizacion=rol.Fecha_Actualizacion)
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

# Actualizar un nombre por id
def update_rol(db:Session, id:int, rol:schemas.rols.RolUpdate):
    db_rol = db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()
    if db_rol:
        for var, value in vars(rol).items():
            setattr(db_rol, var, value) if value else None
        db.commit()
        db.refresh(db_rol)
    return db_rol

# Eliminar un nombre por id
def delete_rol(db:Session, id:int):
    db_rol = db.query(models.rols.Rol).filter(models.rols.Rol.ID == id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
    return db_rol