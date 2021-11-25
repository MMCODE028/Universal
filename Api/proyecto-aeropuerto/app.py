from fastapi import FastAPI
from routes.pasajeros import pasajero
from routes.ticket import ticket
from routes.aerolineas import aerolinea
from routes.aeropuertos import aeropuerto
from routes.aviones import avione
from routes.llegadas import llegada
from routes.modelos import modelo
from routes.salidas import salida
from routes.vuelos import vuelo

app = FastAPI(title="Aeropuerto API")
app.include_router(pasajero)
app.include_router(ticket)
app.include_router(aerolinea)
app.include_router(aeropuerto)
app.include_router(avione)
app.include_router(llegada)
app.include_router(modelo)
app.include_router(salida)
app.include_router(vuelo)
