"""
Test volume encoding.

"""
from hamcrest import assert_that, equal_to, is_, instance_of

from docker_etude.models.validation import FileExistValidation, Validation, EmptyValidation


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
    validation = Validation.from_dict(v)

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
    validation = Validation.from_dict(v)

    assert_that(
        validation,
        is_(instance_of(EmptyValidation)),
    )
