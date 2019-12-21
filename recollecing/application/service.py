import logging
from dataclasses import dataclass

from recollecing.application.repository import AbstractBicingRepository
from recollecing.application.unit_of_work import AbstractUnitOfWork


@dataclass
class FetchUpdate:
    uow: AbstractUnitOfWork
    bicing: AbstractBicingRepository

    def __call__(self):
        updates = self.bicing.get()
        with self.uow:
            self.uow.updates.merge(*updates)
            self.uow.flush()
            self.uow.commit()
        logging.info('Successfully fetched updates.')
