import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import mock

import pytest

from recollecing.infraestructure.bicing import schema as s
from recollecing.infraestructure.bicing.repository import BicingRepo


def test_schema_update():
    u = {
        "station_id": 1,
        "num_bikes_available": 0,
        "num_bikes_available_types": {"mechanical": 3, "ebike": 4},
        "num_docks_available": 42,
        "is_installed": 1,
        "is_renting": 1,
        "is_returning": 1,
        "last_reported": 1576664602,
        "is_charging_station": True,
        "status": "IN_SERVICE",
    }
    update = s.Update(**u)
    assert update.station_id == 1
    assert update.updated == datetime(
        year=2019, month=12, day=18, hour=10, minute=23, second=22, tzinfo=timezone.utc
    )
    assert update.bikes == 3
    assert update.ebikes == 4
    assert update.free == 42
    assert update.active


def test_schema_response():
    r = {
        "last_updated": 1,  # timestamp
        "ttl": 1,
        "data": {
            "stations": [
                {
                    "station_id": 99,
                    "num_bikes_available": 0,
                    "num_bikes_available_types": {"mechanical": 0, "ebike": 0},
                    "status": "IN_SERVICE",
                    "last_reported": 1576664602,
                    "num_docks_available": 42,
                }
            ]
        },
    }
    response = s.Response(**r)
    assert response.next_update == timedelta(seconds=1)
    assert isinstance(response.updates, list)
    assert len(response.updates) == 1
    assert response.updates[0].station_id == 99


class FakeSession:
    def get(self, url):
        return self

    def json(self):
        with (Path(__file__).parent / "station_status.fixture.json").open() as f:
            return json.load(f)


@pytest.fixture
def bicing():
    br = BicingRepo()
    br._session = FakeSession()
    return br


def test_bicing_repo_fake(bicing):
    """Tests the repo against a fixture of the bicing API."""
    updates = list(bicing.get())
    assert len(updates) == 3
    assert updates[0].station_id == 1
    assert updates[1].station_id == 2
    assert updates[2].station_id == 3


def test_next_update(bicing):
    bicing.next_update = datetime.min + timedelta(seconds=5)
    with mock.patch(
        "recollecing.infraestructure.bicing.repository.sleep"
    ) as sleep, mock.patch(
        "recollecing.infraestructure.bicing.repository.datetime"
    ) as dt:
        dt.now = mock.MagicMock(return_value=datetime.min + timedelta(microseconds=24))
        bicing.get()
        sleep.assert_called_once_with(6)
