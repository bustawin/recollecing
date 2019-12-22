import sqlite3
import subprocess
import tempfile
from time import sleep


def test_fetch_update():
    """Testes the whole ``recollecing.run`` with its only one use case.

    This requires Internet and this package to be installed as
    pip install...
    """
    with tempfile.NamedTemporaryFile() as f:
        conn = subprocess.Popen(
            f"reco --db-file '{f.name}' run",
            shell=True,
            universal_newlines=True,
            stderr=subprocess.PIPE,
            stdout=subprocess.PIPE,
        )
        sleep(3)  # Time for recollecing to process a few updates
        conn.kill()  # Recollecing keeps forever running otherwise
        assert not conn.stderr.readlines()

        # Check database for an update
        c = sqlite3.connect(f.name).cursor()
        update_row = c.execute("SELECT * FROM updates").fetchone()
        assert update_row[0] == 1  # The first station
