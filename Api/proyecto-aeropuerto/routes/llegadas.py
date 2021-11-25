from fastapi import APIRouter, status
from starlette import responses
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.llegadas import llegadas
from schemas.llegadas import Llegadas

llegada = APIRouter()


@llegada.get("/llegadas", response_model=list[Llegadas], tags=["llegadas"])
def Get_llegadas():
    return conn.execute(llegadas.select()).fetchall()


@llegada.post('/llegadas', response_model=list[Llegadas], tags=["llegadas"])
def create_llegada(llegada: Llegadas):
    new = {
        "idAeropuerto": llegada.idAeropuerto,
        "fecha": llegada.fecha,
    }
    result = conn.execute(llegadas.insert().values(new))
    return conn.execute(
        llegadas.select().where(llegadas.c.id == result.lastrowid)).first()


@llegada.get("/llegadas/{id}", tags=["llegadas"])
def get_llegadasID(id: str):
    return conn.execute(llegadas.select().where(llegadas.c.id == id)).first()


@llegada.delete("/llegadas/{id}",
                status_code=status.HTTP_200_OK,
                tags=["llegadas"])
def delete_llegada_by_id(id: str):
    result = conn.execute(llegadas.delete().where(llegadas.c.id == id))
    return responses(status_code=HTTP_204_NO_CONTENT)


@llegada.put("/llegadas/{id}",
             response_model=list[Llegadas],
             tags=["llegadas"])
def update_pasajero(id: str, llegada: Llegadas):
    conn.execute(llegadas.update().values(
        idAeropuerto=llegada.idAeropuerto,
        fecha=llegada.fecha,
    ).where(llegadas.c.id == id))
    return conn.execute(llegadas.select().where(llegadas.c.id == id)).first()