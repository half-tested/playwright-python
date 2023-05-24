import pytest


@pytest.mark.xfail(reason='this test is expecting failure')
def test_xfail_expected_failure():
    """this test is an xfail that will be marked as expected failure"""
    assert False


@pytest.mark.xfail(reason='this test is expecting failure')
def test_xfail_unexpected_pass():
    """this test is an xfail that will be marked as unexpected success"""
    assert True