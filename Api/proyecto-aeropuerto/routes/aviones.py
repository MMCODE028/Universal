from fastapi import APIRouter, status
from starlette import responses
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.aviones import aviones
from schemas.aviones import Aviones

avione = APIRouter()


@avione.get("/aviones", response_model=list[Aviones], tags=["aviones"])
def Get_aviones():
    return conn.execute(aviones.select()).fetchall()


@avione.post('/aviones', response_model=list[Aviones], tags=["aviones"])
def create_avione(avione: Aviones):
    new = {
        "nombre": avione.nombre,
        "idModelo": avione.idModelo,
        "idAerolinea": avione.idAerolinea,
        "aforoTotal": avione.aforoTotal
    }
    result = conn.execute(aviones.insert().values(new))
    return conn.execute(
        aviones.select().where(aviones.c.id == result.lastrowid)).first()


@avione.get("/aviones/{id}", tags=["aviones"])
def get_pasajeroID(id: str):
    return conn.execute(aviones.select().where(aviones.c.id == id)).first()


@avione.delete("/aviones/{id}",
               status_code=status.HTTP_200_OK,
               tags=["aviones"])
def delete_pasajero_by_id(id: str):
    result = conn.execute(aviones.delete().where(aviones.c.id == id))
    return responses(status_code=HTTP_204_NO_CONTENT)


@avione.put("/aviones/{id}", response_model=list[Aviones], tags=["aviones"])
def update_pasajero(id: str, avione: Aviones):
    conn.execute(aviones.update().values(
        nombre=avione.nombre,
        idModelo=avione.idModelo,
        idAerolinea=avione.idAerolinea,
        aforoTotal=avione.aforoTotal).where(aviones.c.id == id))
    return conn.execute(aviones.select().where(aviones.c.id == id)).first()
