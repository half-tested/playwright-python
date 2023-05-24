import pytest


@pytest.fixture
def skip_fixture():
    pytest.skip()


@pytest.fixture
def fail_fixture():
    assert False


@pytest.fixture
def broken_fixture():
    raise Exception("Sorry, it's broken.")


def test_with_pytest_skip_in_the_fixture(skip_fixture):
    pass


def test_with_failure_in_the_fixture(fail_fixture):
    pass


def test_with_broken_fixture(broken_fixture):
    pass
