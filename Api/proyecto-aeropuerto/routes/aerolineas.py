from fastapi import APIRouter, status
from starlette import responses
from starlette.status import *
from config.db import conn
from models.aerolineas import aerolineas
from schemas.aerolineas import Aerolineas

aerolinea = APIRouter()


@aerolinea.get("/aerolineas",
               response_model=list[Aerolineas],
               tags=["aerolineas"])
def Get_aerolineas():
    return conn.execute(aerolineas.select()).fetchall()


@aerolinea.post("/aerolinea",
                response_model=list[Aerolineas],
                tags=["aerolineas"])
def create_aerolinea(aerolinea: Aerolineas):
    new_aerolinea = {
        "nombre": aerolinea.nombre,
        "apellido": aerolinea.apellido,
    }
    result = conn.execute(aerolineas.insert().values(new_aerolinea))
    return conn.execute(aerolineas.select().where(
        aerolineas.c.id == result.lastrowid)).first()


@aerolinea.get("/aerolineas/{id}", tags=["aerolineas"])
def get_aerolineaID(id: str):
    return conn.execute(
        aerolineas.select().where(aerolineas.c.id == id)).first()


@aerolinea.delete("/aerolinea/{id}",
                  status_code=status.HTTP_200_OK,
                  tags=["aerolineas"])
def delete_aerolinea_by_id(id: str):
    result = conn.execute(aerolineas.delete().where(aerolineas.c.id == id))
    return responses(status_code=HTTP_204_NO_CONTENT)


@aerolinea.put("/aerolinea/{id}",
               response_model=list[Aerolineas],
               tags=["aerolineas"])
def update_pasajero(id: str, aerolinea: Aerolineas):
    conn.execute(aerolineas.update().values(nombre=aerolinea.nombre).where(
        aerolineas.c.id == id))
    return conn.execute(
        aerolineas.select().where(aerolinea.c.id == int(id))).first()