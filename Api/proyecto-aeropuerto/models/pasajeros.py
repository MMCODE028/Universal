from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import DATE, Integer, String
from config.db import meta, engine

pasajeros = Table("pasajeros", meta, Column("id", Integer, primary_key=True),
                  Column("nombre", String(255)),
                  Column("apellido", String(255)),
                  Column("nacionalidad", String(255)),
                  Column("fechaDeNacimiento", DATE))

meta.create_all(engine)
