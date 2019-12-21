import tempfile
from datetime import datetime

from recollecing.domain import model as m
from recollecing.infraestructure.sqla.orm import metadata
from recollecing.infraestructure.sqla.repository import engine
from recollecing.infraestructure.sqla.unit_of_work import SQLAlchemyUnitOfWork


def test_sqla_psql_create_update(db):
    uow = SQLAlchemyUnitOfWork(db_uri=db)
    update = m.Update(
        station_id=1, updated=datetime.min, bikes=1, ebikes=2, free=3, active=True
    )
    with uow:
        uow.updates.merge(update)
        uow.flush()
        uow.commit()
        station_id, updated = update.station_id, update.updated

    with uow:
        new_update = uow.updates.get_one(station_id, updated)
        assert new_update.station_id == station_id
        assert new_update.updated == updated
        assert new_update.bikes == 1
        assert new_update.ebikes == 2
        assert new_update.free == 3
        assert new_update.active


def test_sqla_file():
    with tempfile.NamedTemporaryFile() as f:
        e = engine(f.name)
        metadata.create_all(e)
