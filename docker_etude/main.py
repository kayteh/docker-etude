"""
CLI entry point.

"""
from click import echo, group, option

from docker_etude.sources import LocalStackSource


@group()
def etude():
    """
    Generate a composition.

    """
    pass


@etude.command(name="localstack")
@option("--region", default="us-east-1")
def localstack(region):
    source = LocalStackSource(
        region=region,
    )
    composition = source.load()
    echo(composition.to_yaml())
