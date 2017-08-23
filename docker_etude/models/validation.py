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
    @property
    def all_validations(self):
        return [
            FileExistValidation,
            EmptyValidation,
        ]

    @abstractmethod
    def validate(self):
        """
        Validate the specific validation
        This needs to be implemented in classes inheriting from 
        Validation

        """
        pass

    def get(self, name):
        """Gets all the validations for the name

        :name: name of a validation
        :returns: list of validations that match the name

        """
        for validation in self.all_validations:
            yield validation

        return EmptyValidation


class FileExistValidation(Validation):
    def __init__(self, **kwargs):
        self.name = "file"
        self.filepath = kwargs["filepath"]

    def validate(self):
        valid_file = Path(self.filepath)
        return valid_file.is_file()

class EmptyValidation(Validation):
    def __init__(self, **kwargs):
        self.name = "empty"

    def validate(self, arg1):
        return True
