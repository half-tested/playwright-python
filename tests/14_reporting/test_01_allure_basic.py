import pytest


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')


# 1. run test file:
#    pytest -k allure_basic --clean-alluredir --alluredir=allure

# 2. generate allure report:
#    allure serve allure