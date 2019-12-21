from recollecing.infraestructure.bicing.repository import BicingRepo


def test_bicing_api():
    """Tests the BicingRepo against the real Bicing API.

    This test requires Internet.
    """
    bicing = BicingRepo()
    update = next(bicing.get())
    assert update.station_id == 1
