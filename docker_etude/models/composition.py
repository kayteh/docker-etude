"""
A docker composition.

"""
from collections import OrderedDict

from docker_etude.models.base import Model
from docker_etude.models.service import Service


class Composition(Model):
    """
    The top-level model for a docker composition.

    Maps to/from a docker-compose.yml file.

    """
    def __init__(self,
                 networks=None,
                 services=None,
                 version="3",
                 volumes=None):
        self.version = version
        self.networks = networks or {}
        self.services = services or {}
        self.volumes = volumes or {}

    def to_dict(self):
        return OrderedDict(
            version=self.version,
            networks=self.networks,
            services={
                name: service.to_safe_dict()
                for name, service in self.services.items()
            },
            volumes=self.volumes,
        )

    @classmethod
    def from_dict(cls, dct):
        return cls(
            version=dct["version"],
            networks=dct.get("networks"),
            services={
                name: Service.from_dict(dict(
                    name=name,
                    **service
                ))
                for name, service in dct.get("services", []).items()
            },
            volumes=dct.get("volumes"),
        )
