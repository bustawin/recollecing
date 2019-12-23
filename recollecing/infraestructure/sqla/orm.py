import sqlalchemy as s
from sqlalchemy import orm

from recollecing.domain import model

metadata = s.MetaData()

update = s.Table(
    "updates",
    metadata,
    s.Column("station_id", s.SmallInteger, nullable=False),
    s.Column("updated", s.TIMESTAMP(timezone=True), nullable=False),
    s.Column("bikes", s.SmallInteger, nullable=False),
    s.Column("ebikes", s.SmallInteger, nullable=False),
    s.Column("free", s.SmallInteger, nullable=False),
    s.Column("active", s.Boolean, nullable=False),
    # todo it should be better to use IGNORE specifically in the
    #   inserts, but sqla does not supported it <yet> for sqlite
    s.PrimaryKeyConstraint("station_id", "updated", sqlite_on_conflict="IGNORE"),
)


def init_mappers():
    orm.mapper(model.Update, update)
