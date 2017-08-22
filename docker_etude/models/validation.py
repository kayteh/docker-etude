"""
Validation as a defined model
This will have a list of validations that a service needs to check
before being added to the composition.

These validations will support multiple items, currently implemented is "file"

"""

from abc import ABC, abstractclassmethod, abstractmethod
from docker_etude.models.base import Model
from pathlib import Path

class Validation(ABC):
    @abstractmethod
    def is_valid():
        """
        Return a boolean whether this specific validation is passing or not

        """
        pass

class FileExistValidation(Validation):
    def __init__(self, filepath):
        self.filepath = filepath

    def is_valid(self):
        valid_file = Path(self.filepath)
        return valid_file.is_file()


class ServiceValiation(Model):
    def __init(self, service_name):
        self.service_name = service_name
