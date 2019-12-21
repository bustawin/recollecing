import tempfile

import pytest
from sqlalchemy.orm import clear_mappers

from recollecing.infraestructure.sqla.orm import init_mappers, metadata
from recollecing.infraestructure.sqla.repository import engine


@pytest.fixture
def db() -> callable:
    with tempfile.NamedTemporaryFile() as f:
        e = engine(f.name)
        metadata.create_all(e)
        clear_mappers()
        init_mappers()
        yield f.name
        clear_mappers()
