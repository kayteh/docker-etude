"""
Test volume encoding.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.models.volume import Volume


def test_encoding():
    volume = dict(
        driver="local",
    )

    assert_that(
        Volume.from_dict(volume).to_safe_dict(),
        is_(equal_to(volume)),
    )
