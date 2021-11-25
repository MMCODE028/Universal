from fastapi import APIRouter, status
from starlette import responses
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.aeropuertos import aeropuertos
from schemas.aeropuertos import Aeropuertos

aeropuerto = APIRouter()


@aeropuerto.get("/aeropuertos",
                response_model=list[Aeropuertos],
                tags=["aeropuertos"])
def Get_aeropuertos():
    return conn.execute(aeropuertos.select()).fetchall()


@aeropuerto.post("/aeropuerto",
                 response_model=list[Aeropuertos],
                 tags=["aeropuertos"])
def create_aeropuerto(aeropuerto: Aeropuertos):
    new = {
        "nombre": aeropuerto.nombre,
        "ciudad": aeropuerto.ciudad,
    }
    result = conn.execute(aeropuertos.insert().values(new))
    return conn.execute(aeropuertos.select().where(
        aeropuertos.c.id == result.lastrowid)).first()


@aeropuerto.get("/aeropuerto/{id}", tags=["aeropuertos"])
def get_aeropuertoID(id: str):
    return conn.execute(
        aeropuertos.select().where(aeropuertos.c.id == int(id))).first()


@aeropuerto.delete("/aeropuertos/{id}",
                   status_code=status.HTTP_200_OK,
                   tags=["aeropuertos"])
def delete_pasajero_by_id(id: str):
    result = conn.execute(aeropuertos.delete().where(aeropuertos.c.id == id))
    return responses(status_code=HTTP_204_NO_CONTENT)


@aeropuerto.put("/aeropuerto/{id}",
                response_model=list[Aeropuertos],
                tags=["aeropuertos"])
def update_aeropuerto(id: str, aeropuerto: Aeropuertos):
    conn.execute(aeropuertos.update().values(
        nombre=aeropuerto.nombre,
        ciudad=aeropuerto.ciudad).where(aeropuertos.c.id == int(id)))
    return conn.execute(
        aeropuertos.select().where(aeropuertos.c.id == id)).first()