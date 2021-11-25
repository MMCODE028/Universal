from sqlalchemy import Table, Column
from config.db import meta, engine
from sqlalchemy.sql.sqltypes import DATE, Integer, String

modelos = Table("modelos", meta, Column("id", String(255), primary_key=True),
                Column("nombre", String(255)), Column("marca", String(255)))
