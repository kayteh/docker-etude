"""
Test service encoding.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.models.service import Service


def test_encoding():
    POSTGRES = dict(
        image="postgres",
        volumes=[
            "data:/var/lib/postgresql/data",
        ],
    )

    assert_that(
        Service.from_dict(POSTGRES).to_safe_dict(),
        is_(equal_to(POSTGRES)),
    )
