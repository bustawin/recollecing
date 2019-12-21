import click

from recollecing.application.main import Recollecing


@click.group()
@click.option("--db-file", help="The URI of the database. By default, in memory.")
@click.pass_context
def recollecing(ctx, db_file: str):
    """Recollects periodically information from the Bicing API.

    You can pass the options environment variables using the
    "RECOLLECING_" prefix (ex. "RECOLLECING_DB_URI" substitutes
    "--db_uri".)
    """
    ctx.ensure_object(dict)
    ctx.obj["app"] = Recollecing(db_file=db_file)


@recollecing.command()
@click.pass_context
def run(ctx):
    """Starts running the app."""
    app: Recollecing = ctx.obj["app"]
    app.run()


@recollecing.command()
@click.confirmation_option(prompt="This will delete the DB. Do you want to continue?")
@click.pass_context
def drop_db(ctx):
    app: Recollecing = ctx.obj["app"]
    app.drop_db()


if __name__ == "__main__":
    recollecing(auto_envar_prefix="RECOLLECING", obj={})
