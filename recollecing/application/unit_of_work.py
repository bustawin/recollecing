import abc
from typing import Optional

from recollecing.application import repository


class AbstractUnitOfWork(abc.ABC):
    def __init__(self, db_uri: Optional[str] = None) -> None:
        super().__init__()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def init_repositories(self, updates: repository.AbstractDbRepository):
        """Initializes all the repositories"""
        # This method should have one repository per aggregate
        # even if we end up repeating repositories
        self.updates: repository.AbstractDbRepository = updates

    @abc.abstractmethod
    def flush(self):
        raise NotImplementedError

    @abc.abstractmethod
    def commit(self):
        raise NotImplementedError

    @abc.abstractmethod
    def rollback(self):
        raise NotImplementedError
