"""
Test service encoding.

"""
from hamcrest import assert_that, equal_to, is_, instance_of

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

def test_error_instance():
    service = Service.from_dict(dict(
        image="nginx",
        name="nginx-name",
    ))
    service.add_error("some error")

    assert_that(
        service.errors[0],
        is_(instance_of(Exception)),
    )

def test_error_instance_props():
    service = Service.from_dict(dict(
        image="nginx",
        name="nginx-name",
    ))
    service.add_error("some error")

    assert_that(
        service.errors[0].normalized_message["message"],
        is_(equal_to("some error")),
    )
    assert_that(
        service.errors[0].normalized_message["service"],
        is_(equal_to("nginx-name")),
    )
