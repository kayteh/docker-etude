"""
Validation as a defined model
This will have a list of validations that a service needs to check
before being added to the composition.

These validations will support multiple items, currently implemented is "file"

"""
from abc import ABC, abstractclassmethod, abstractmethod
from os import getenv
from pathlib import Path

from docker_etude.models.base import Model


class Validation(ABC):
    def __init__(self, **kwargs):
        pass

    @classmethod
    def all_validations(self):
        return [
            FileExistValidation,
            EnvVarExistValidation,
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


class EnvVarExistValidation(Validation):
    @classmethod
    def name(cls):
        return "env"

    def __init__(self, **kwargs):
        self.envvar = kwargs.get("var")

    def validate(self):
        value = getenv(self.envvar)
        return bool(value)


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
