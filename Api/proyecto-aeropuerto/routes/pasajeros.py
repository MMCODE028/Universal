from fastapi import APIRouter, status
from starlette.responses import Response
from config.db import conn
from models.pasajeros import pasajeros
from schemas.pasajeros import Pasajero
from starlette.status import *

pasajero = APIRouter()


@pasajero.get('/pasajeros', response_model=list[Pasajero], tags=["pasajeros"])
def Get_pasajeros():
    return conn.execute(pasajeros.select()).fetchall()


@pasajero.post('/pasajeros', response_model=list[Pasajero], tags=["pasajeros"])
def create_pasajeros(pasajero: Pasajero):
    new_pasajero = {
        "nombre": pasajero.nombre,
        "apellido": pasajero.apellido,
        "nacionalidad": pasajero.nacionalidad,
        "fechaDeNacimiento": pasajero.fechaDeNacimiento
    }
    result = conn.execute(pasajeros.insert().values(new_pasajero))
    return conn.execute(
        pasajeros.select().where(pasajeros.c.id == result.lastrowid)).first()


@pasajero.get("/pasajeros/{id}", tags=["pasajeros"])
def get_pasajeroID(id: str):
    return conn.execute(
        pasajeros.select().where(pasajeros.c.id == int(id))).first()


@pasajero.delete("/pasajeros/{id}",
                 status_code=status.HTTP_200_OK,
                 tags=["pasajeros"])
def delete_pasajero_by_id(id: str):
    result = conn.execute(pasajeros.delete().where(pasajeros.c.id == int(id)))
    return Response(status_code=HTTP_204_NO_CONTENT)


@pasajero.put("/pasajeros/{id}",
              response_model=list[Pasajero],
              tags=["pasajeros"])
def update_pasajero(id: str, pasajero: Pasajero):
    conn.execute(pasajeros.update().values(
        nombre=pasajero.nombre,
        apellido=pasajero.apellido,
        nacionalidad=pasajero.nacionalidad,
        fechaDeNacimiento=pasajero.fechaDeNacimiento).where(
            pasajeros.c.id == int(id)))
    return conn.execute(
        pasajeros.select().where(pasajeros.c.id == int(id))).first()
