from datetime import datetime
from typing import Iterator

import pytest

from recollecing.application.repository import (
    AbstractBicingRepository,
    AbstractDbRepository,
)
from recollecing.application.service import FetchUpdate
from recollecing.application.unit_of_work import AbstractUnitOfWork
from recollecing.domain import model, model as m


class FakeDbRepository(AbstractDbRepository):
    def __init__(self) -> None:
        super().__init__()
        self._updates = {}

    def create_if_not_exists(self, *update: model.Update):
        for u in update:
            self._updates[(u.station_id, u.updated)] = u

    def get_one(self, station_id: int, updated: datetime) -> m.Update:
        pass


class FakeUoW(AbstractUnitOfWork):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.commited = False

    def __enter__(self):
        self.init_repositories(FakeDbRepository())
        return super().__enter__()

    def flush(self):
        pass

    def commit(self):
        self.commited = True

    def rollback(self):
        pass


class FakeBicing(AbstractBicingRepository):
    def get(self) -> Iterator[model.Update]:
        return iter(
            [
                m.Update(
                    station_id=1,
                    updated=datetime.min,
                    bikes=1,
                    ebikes=1,
                    free=1,
                    active=False,
                )
            ]
        )


@pytest.fixture
def fake_uow():
    return FakeUoW()


@pytest.fixture
def fake_bicing():
    return FakeBicing()


def test_fetch_update(fake_uow, fake_bicing):
    fu = FetchUpdate(fake_uow, fake_bicing)
    fu()
    assert fake_uow.commited
    assert len(fake_uow.updates._updates) == 1
    assert next(iter((fake_uow.updates._updates.values()))).station_id == 1
