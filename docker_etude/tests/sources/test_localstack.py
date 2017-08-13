"""
Test LocalStack source.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.sources.localstack import LocalStackSource


def test_source():
    LOCALSTACK = {
        "networks": {
            "localstack": {
                "driver": "bridge",
            },
        },
        "services": {
            "localstack": {
                "container_name": "localstack",
                "environment": {
                    "DATA_DIR": "/tmp/localstack/data",
                    "DEFAULT_REGION": "us-east-1",
                    "HOSTNAME": "localstack",
                    "SERVICES": "sns,sqs",
                },
                "image": "localstack/localstack",
                "networks": {
                    "localstack": None,
                },
                "ports": [
                    "4575:4575",
                    "4576:4576",
                ],
                "volumes": [
                    "localstack-data:/tmp/localstack/data",
                ],
            },
        },
        "version": "3",
        "volumes": {
            "localstack-data": None,
        },
    }

    assert_that(
        LocalStackSource().load().to_dict(),
        is_(equal_to(LOCALSTACK)),
    )
