"""
Test volume encoding.

"""
from hamcrest import assert_that, equal_to, is_

from docker_etude.models.validation import FileExistValidation


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
