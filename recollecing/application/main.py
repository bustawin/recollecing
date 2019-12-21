import logging
from time import sleep
from typing import Type

from recollecing.application.repository import AbstractBicingRepository
from recollecing.application.service import FetchUpdate
from recollecing.application.unit_of_work import AbstractUnitOfWork
from recollecing.infraestructure.bicing.repository import BicingRepo
from recollecing.infraestructure.log import setup_log
from recollecing.infraestructure.sqla.orm import init_mappers, metadata
from recollecing.infraestructure.sqla.repository import engine
from recollecing.infraestructure.sqla.unit_of_work import SQLAlchemyUnitOfWork


class Recollecing:
    def __init__(
        self,
        db_file: str = None,
        UnitOfWork: Type[AbstractUnitOfWork] = SQLAlchemyUnitOfWork,
        Bicing: Type[AbstractBicingRepository] = BicingRepo,
        log_setup: callable = setup_log,
    ) -> None:
        log_setup()
        super().__init__()
        self.db_file = db_file
        self.uow = UnitOfWork(db_uri=db_file)
        self.bicing = Bicing()
        init_mappers()
        self.init_db()

    def run(self):
        fetch_update = FetchUpdate(self.uow, self.bicing)
        while True:
            logging.info("New fetching iteration.")
            fetch_update()
            sleep(0.5)

    def init_db(self):
        """Creates a database (does nothing if the database existed)."""
        e = engine(self.db_file)
        metadata.create_all(e)
        return e

    def drop_db(self):
        e = engine(self.db_file)
        metadata.drop_all(e)
        return e
