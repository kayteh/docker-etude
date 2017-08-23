"""
Test volume encoding.

"""
from hamcrest import assert_that, equal_to, is_, instance_of
from json import loads
from os import environ

from docker_etude.models.validation import FileExistValidation, BaseValidation, EmptyValidation, ServiceValidation, Validations
from docker_etude.models import Service


def test_validation_file_exists():
    filename = "docker_etude/tests/fixtures/validations.json"
    validation = FileExistValidation(filepath=filename)

    assert_that(
        validation.validate(),
        is_(equal_to(True)),
    )

def test_validation_file_does_not_exist():
    filename = "docker_etude/tests/fixtures/validations2.json"
    validation = FileExistValidation(filepath=filename)
    assert_that(
        validation.validate(),
        is_(equal_to(False)),
    )

def test_validation_from_dict():
    filename = "docker_etude/tests/fixtures/validations2.json"
    v = dict(
        name="file",
        filepath=filename,
        some="other_string",
    )
    validation = BaseValidation.from_dict(v)

    assert_that(
        validation,
        is_(instance_of(FileExistValidation)),
    )

def test_empty_validation_from_dict():
    filename = "docker_etude/tests/fixtures/validations2.json"
    v = dict(
        name="InvalidValidationName",
        filepath=filename,
        some="other_string",
    )
    validation = BaseValidation.from_dict(v)

    assert_that(
        validation,
        is_(instance_of(EmptyValidation)),
    )

def test_envvar_validation():
    v = dict(
        name="env",
        var="SOMETHING",
    )
    validation = BaseValidation.from_dict(v)
    assert_that(
        validation.validate(),
        is_(equal_to(False)),
    )

def test_envvar_validation_exists():
    environ["SOMETHING"] = "SOME_VALUE"
    v = dict(
        name="env",
        var="SOMETHING",
    )
    validation = BaseValidation.from_dict(v)
    assert_that(
        validation.validate(),
        is_(equal_to(True)),
    )
    environ["SOMETHING"] = ""

def test_service_validations_internal_length():
    json_data = open("docker_etude/tests/fixtures/validations.json").read()
    dct = loads(json_data)
    service_validations = Validations.from_dict(dct)
    assert_that(
        len(service_validations.validations),
        is_(equal_to(3)),
    )

def test_service_validations_for_service():
    service = Service.from_dict(dict(
        image="nginx",
        name="service1",
    ))
    json_data = open("docker_etude/tests/fixtures/validations.json").read()
    dct = loads(json_data)
    service_validations = Validations.from_dict(dct)
    assert_that(
        service_validations.validate(service),
        is_(equal_to(True)),
    )

    print(service.errors)

def test_service_validations_for_service_fails():
    service = Service.from_dict(dict(
        image="nginx",
        name="service2",
    ))
    json_data = open("docker_etude/tests/fixtures/validations.json").read()
    dct = loads(json_data)
    service_validations = Validations.from_dict(dct)
    assert_that(
        service_validations.validate(service),
        is_(equal_to(False)),
    )
