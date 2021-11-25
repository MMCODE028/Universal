from fastapi import APIRouter, status
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.vuelos import vuelos
from schemas.vuelo import Vuelos

vuelo = APIRouter()


@vuelo.get("/vuelo", response_model=list[Vuelos], tags=["vuelos"])
def Get_vuelo():
    return conn.execute(vuelos.select()).fetchall()


@vuelo.post('/vuelos', response_model=list[Vuelos], tags=["vuelos"])
def create_vuelo(vuelo: Vuelos):
    new = {
        "idLlegada": vuelo.idLlegada,
        "idSalida": vuelo.idSalida,
        "idAvion": vuelo.idAvion
    }
    result = conn.execute(vuelos.insert().values(new))
    return conn.execute(
        vuelos.select().where(vuelos.c.id == result.lastrowid)).first()


@vuelo.get("/vuelos/{id}", tags=["vuelos"])
def get_vuelosID(id: str):
    return conn.execute(vuelos.select().where(vuelos.c.id == id)).first()


@vuelo.delete("/vuelos/{id}", status_code=status.HTTP_200_OK, tags=["vuelos"])
def delete_vuelos_by_id(id: str):
    result = conn.execute(vuelos.delete().where(vuelos.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@vuelo.put("/salidas/{id}", response_model=list[Vuelos], tags=["vuelos"])
def update_pasajero(id: str, vuelo: Vuelos):
    conn.execute(vuelos.update().values(
        idLlegada=vuelo.idLlegada,
        idSalida=vuelo.idSalida,
        idAvion=vuelo.idAvion).where(vuelos.c.id == id))
    return conn.execute(vuelos.select().where(vuelos.c.id == id)).first()