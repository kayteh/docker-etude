"""
A docker composition.

"""
from collections import OrderedDict

from docker_etude.models.base import Model
from docker_etude.models.network import Network
from docker_etude.models.service import Service
from docker_etude.models.volume import Volume


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
        self.networks = networks or OrderedDict()
        self.services = services or OrderedDict()
        self.volumes = volumes or OrderedDict()

    def to_dict(self):
        return OrderedDict(
            version=self.version,
            networks=self.dump_model_dict(self.networks),
            services=self.dump_model_dict(self.services),
            volumes=self.dump_model_dict(self.volumes),
        )

    def dump_model_dict(self, dct):
        if not dct:
            return None

        return {
            name: model.to_safe_dict() if model else None
            for name, model in dct.items()
        }

    @classmethod
    def from_dict(cls, dct):
        return cls(
            version=dct["version"],
            networks=cls.load_model_dict(dct.get("networks"), Network),
            services=cls.load_model_dict(dct.get("services"), Service),
            volumes=cls.load_model_dict(dct.get("volumes"), Volume),
        )

    @classmethod
    def load_model_dict(cls, dct, model_cls):
        if not dct:
            return None

        return {
            name: model_cls.from_dict(dict(
                name=name,
                **model_dct
            )) if model_dct else None
            for name, model_dct in dct.items()
        }
