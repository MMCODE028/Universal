from fastapi import APIRouter, status
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from config.db import conn
from models.ticket import tickets
from schemas.tickets import Tickets

ticket = APIRouter()


@ticket.get("/tickets", response_model=list[Tickets], tags=["tickets"])
def Get_tickets():
    return conn.execute(tickets.select()).fetchall()


@ticket.post('/tickets', response_model=list[Tickets], tags=["tickets"])
def create_ticket(ticket: Tickets):
    new = {
        "idPasajero": ticket.idPasajero,
        "idVuelo": ticket.idVuelo,
    }
    result = conn.execute(tickets.insert().values(new))
    return conn.execute(
        tickets.select().where(tickets.c.id == result.lastrowid)).first()


@ticket.get("/tickets/{id}", tags=["tickets"])
def get_ticketID(id: str):
    return conn.execute(tickets.select().where(tickets.c.id == id)).first()


@ticket.delete("/tickets/{id}",
               status_code=status.HTTP_200_OK,
               tags=["tickets"])
def delete_ticket_by_id(id: str):
    result = conn.execute(tickets.delete().where(tickets.c.id == id))
    return Response(status_code=HTTP_204_NO_CONTENT)


@ticket.put("/tickets/{id}", response_model=list[Tickets], tags=["tickets"])
def update_ticket(id: str, ticket: Tickets):
    conn.execute(tickets.update().values(
        idPasajero=ticket.idPasajero,
        idVuelo=ticket.idVuelo,
    ).where(tickets.c.id == id))
    return conn.execute(tickets.select().where(tickets.c.id == id)).first()
