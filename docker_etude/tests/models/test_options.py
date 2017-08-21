"""
Test options.

"""
from hamcrest import assert_that, equal_to, is_, none

from docker_etude.models.options import Options


def test_null():
    options = Options()
    assert_that(options.foo, is_(none()))


def test_set():
    options = Options()
    options.foo = "bar"
    assert_that(options.foo, is_(equal_to("bar")))
