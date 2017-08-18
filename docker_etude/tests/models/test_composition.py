"""
Test composition encoding.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.models.composition import Composition


def test_encoding():
    COMPOSITION = dict(
        version="3",
        services=dict(
            db=dict(
                image="postgres",
                volumes=[
                    "data:/var/lib/postgresql/data",
                ],
            ),
        ),
        networks=dict(
            etude=None,
        ),
        volumes={
            "postgres-data": None,
        },
    )

    assert_that(
        Composition.from_dict(COMPOSITION).to_safe_dict(),
        is_(equal_to(COMPOSITION)),
    )
