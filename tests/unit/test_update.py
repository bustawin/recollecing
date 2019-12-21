from datetime import datetime

from recollecing.domain import model as m


def test_update_create():
    update = m.Update(
        station_id=1, updated=datetime.min, bikes=1, ebikes=2, free=3, active=True
    )
    assert update.station_id == 1
    assert update.updated == datetime.min
    assert update.bikes == 1
    assert update.ebikes == 2
    assert update.free == 3
    assert update.active
