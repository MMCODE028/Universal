from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import DATE, Integer, String

vuelos = Table("vuelos", meta, Column("id", Integer, primary_key=True),
               Column("idLlegada", String(255)),
               Column("idSalida", String(255)), Column("idAvion", String(255)))

meta.create_all(engine)
