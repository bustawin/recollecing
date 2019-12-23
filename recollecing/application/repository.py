import abc
from datetime import datetime
from typing import Iterator

from recollecing.domain import model as m


class AbstractDbRepository(abc.ABC):
    @abc.abstractmethod
    def create_if_not_exists(self, *update: m.Update):
        """Creates the object(s) in the DB if it does not exist yet,
        otherwise update the values of the existing one.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_one(self, station_id: int, updated: datetime) -> m.Update:
        raise NotImplementedError


class AbstractBicingRepository(abc.ABC):
    @abc.abstractmethod
    def get(self) -> Iterator[m.Update]:
        raise NotImplementedError
