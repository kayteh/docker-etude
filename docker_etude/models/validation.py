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
    def __init__(self, **kwargs):
        pass

    @classmethod
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

    @classmethod
    def from_dict(cls, dct):
        name = dct.get("name")
        return cls.get(name)(**dct)

    @classmethod
    def iter_matching_validations(self, name):
        for validation in Validation.all_validations():
            if validation.name() == name:
                 yield validation

    @abstractmethod
    def name(cls):
        pass

    @classmethod
    def get(self, name):
        """Gets all the validations for the name

        :name: name of a validation
        :returns: list of validations that match the name

        """
        matching = list(Validation.iter_matching_validations(name))

        if matching:
            return matching[0]

        return EmptyValidation


class FileExistValidation(Validation):
    @classmethod
    def name(cls):
        return "file"

    def __init__(self, **kwargs):
        self.filepath = kwargs.get("filepath")

    def validate(self):
        valid_file = Path(self.filepath)
        return valid_file.is_file()


class EmptyValidation(Validation):
    @classmethod
    def name(cls):
        return "empty"

    def validate(self, arg1):
        return True
