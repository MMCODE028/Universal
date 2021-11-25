from fastapi import APIRouter, status
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.modelos import modelos
from schemas.modelos import Modelos

modelo = APIRouter()


@modelo.get("/modelos", response_model=list[Modelos], tags=["modelos"])
def Get_modelos():
    return conn.execute(modelos.select()).fetchall()


@modelo.post('/modelos', response_model=list[Modelos], tags=["modelos"])
def create_modelo(modelo: Modelos):
    new = {
        "nombre": modelo.nombre,
        "marca": modelo.marca,
    }
    result = conn.execute(modelos.insert().values(new))
    return conn.execute(
        modelos.select().where(modelos.c.id == result.lastrowid)).first()


@modelo.get("/modelos/{id}", tags=["modelos"])
def get_modelosID(id: str):
    return conn.execute(modelos.select().where(modelos.c.id == id)).first()


@modelo.delete("/modelos/{id}",
               status_code=status.HTTP_200_OK,
               tags=["modelos"])
def delete_modelos_by_id(id: str):
    result = conn.execute(modelos.delete().where(modelos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@modelo.put("/modelos/{id}", response_model=list[Modelos], tags=["modelos"])
def update_pasajero(id: str, modelo: Modelos):
    conn.execute(modelos.update().values(
        nombre=modelo.nombre,
        marca=modelo.marca,
    ).where(modelos.c.id == id))
    return conn.execute(modelos.select().where(modelos.c.id == id)).first()