import pytest

# Contains all code that is commonly used in all pytests, e.g. some fixtures
# It is automatically imported whenever a pytest is called.


@pytest.fixture()
def example_fixture():
    fixture = 123
    return fixture
