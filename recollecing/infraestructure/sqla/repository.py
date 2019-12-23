import logging
from datetime import datetime

from sqlalchemy import create_engine, orm

from recollecing.application import repository
from recollecing.domain import model, model as m


def engine(uri=None):
    sqlite = "sqlite://"
    uri = f"{sqlite}/{uri}" if uri else sqlite
    logging.info(f"Using DB in {uri}")
    return create_engine(uri)


class SQLARepository(repository.AbstractDbRepository):
    def __init__(self, session: orm.Session) -> None:
        super().__init__()
        self.session: orm.Session = session

    def create_if_not_exists(self, *update: model.Update):
        self.session.bulk_insert_mappings(m.Update, (vars(u) for u in update))

    def get_one(self, station_id: int, updated: datetime) -> m.Update:
        return (
            self.session.query(m.Update)
            .filter_by(station_id=station_id, updated=updated)
            .one()
        )
