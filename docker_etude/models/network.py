"""
A docker compose network.

"""
from collections import OrderedDict

from docker_etude.models.base import Model


class Network(Model):
    """
    A single docker compose netork.

    """
    def __init__(self, driver=None, name=None):
        self.driver = driver
        self.name = name

    def to_dict(self):
        return OrderedDict(
            driver=self.driver
        )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            driver=dct.get("driver"),
            name=dct.get("name"),
        )