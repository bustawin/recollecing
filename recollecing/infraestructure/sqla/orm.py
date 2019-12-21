import sqlalchemy as s
from sqlalchemy import orm

from recollecing.domain import model

metadata = s.MetaData()

update = s.Table(
    "updates",
    metadata,
    s.Column("station_id", s.SmallInteger, primary_key=True, nullable=False),
    s.Column("updated", s.TIMESTAMP(timezone=True), primary_key=True, nullable=False),
    s.Column("bikes", s.SmallInteger, nullable=False),
    s.Column("ebikes", s.SmallInteger, nullable=False),
    s.Column("free", s.SmallInteger, nullable=False),
    s.Column("active", s.Boolean, nullable=False),
)


def init_mappers():
    orm.mapper(model.Update, update)
