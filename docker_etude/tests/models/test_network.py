"""
Test network encoding.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.models.network import Network


def test_encoding():
    NETWORK = dict(
        driver="bridge",
    )

    assert_that(
        Network.from_dict(NETWORK).to_safe_dict(),
        is_(equal_to(NETWORK)),
    )
