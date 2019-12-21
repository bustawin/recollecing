import pytest
from click.testing import CliRunner

from recollecing.application import cli


class CustomCLIRunner(CliRunner):
    def invoke(
        self,
        *args,
        input=None,
        env=None,
        catch_exceptions=False,
        color=False,
        mix_stderr=False,
    ):
        return super().invoke(
            cli.recollecing,
            args,
            input,
            env,
            catch_exceptions,
            color,
            mix_stderr,
            obj={},
        )


@pytest.fixture
def cli_runner():
    return CustomCLIRunner()


def test_cli_recollecing(cli_runner):
    """Test the CLI calls."""
    r = cli_runner.invoke()
    assert r.exit_code == 0


def test_cli_drop_db(cli_runner):
    r = cli_runner.invoke("drop-db", "--yes")
    assert r.exit_code == 0


def test_cli_run():
    pass
    # todo
