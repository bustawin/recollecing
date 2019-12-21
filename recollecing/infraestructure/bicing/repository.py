from datetime import datetime
from time import sleep
from typing import Optional, Set, Iterator

from furl import furl
from retry_requests import RSession, retry

from recollecing.application.repository import AbstractBicingRepository
from recollecing.domain import model
from recollecing.infraestructure.bicing import schema


class BicingRepo(AbstractBicingRepository):
    URL = furl(
        "https://opendata-ajuntament.barcelona.cat/data/dataset/"
        "6aa3416d-ce1a-494d-861b-7bd07f069600/resource/"
        "b20e711d-c3bf-4fe5-9cde-4de94c5f588f/download"
    )
    SLEEP_SECS = 2

    def __init__(self) -> None:
        super().__init__()
        self.next_update: datetime = datetime.now()
        self._session: Optional[RSession] = None

    def get(self) -> Iterator[model.Update]:
        now = datetime.now()
        while now < self.next_update:
            sleep((self.next_update - now).seconds)
        return self._get()

    def _get(self) -> Iterator[model.Update]:
        r = self.session.get(self.URL)
        response = schema.Response(**r.json())
        self.next_update = datetime.now() + response.next_update
        return (model.Update(**u) for u in response.dict()["updates"])

    @property
    def session(self) -> RSession:
        self._session = self._session or retry(RSession())
        return self._session
