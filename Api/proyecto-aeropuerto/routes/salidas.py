from fastapi import APIRouter, status
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.salidas import salidas
from schemas.salidas import Salidas

salida = APIRouter()


@salida.get("/salidas", response_model=list[Salidas], tags=["salidas"])
def Get_salida():
    return conn.execute(salidas.select()).fetchall()


@salida.post('/salidas', response_model=list[Salidas], tags=["salidas"])
def create_salida(salida: Salidas):
    new = {
        "idAeropuerto": salida.idAeropuerto,
        "fecha": salida.fecha,
    }
    result = conn.execute(salidas.insert().values(new))
    return conn.execute(
        salidas.select().where(salidas.c.id == result.lastrowid)).first()


@salida.get("/salidas/{id}", tags=["salidas"])
def get_salidasID(id: str):
    return conn.execute(salidas.select().where(salidas.c.id == id)).first()


@salida.delete("/salidas/{id}",
               status_code=status.HTTP_200_OK,
               tags=["salidas"])
def delete_salidas_by_id(id: str):
    result = conn.execute(salidas.delete().where(salidas.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@salida.put("/salidas/{id}", response_model=list[Salidas], tags=["salidas"])
def update_pasajero(id: str, salida: Salidas):
    conn.execute(salidas.update().values(
        idAeropuerto=salida.idAeropuerto,
        fecha=salida.fecha,
    ).where(salidas.c.id == id))
    return conn.execute(salidas.select().where(salidas.c.id == id)).first()