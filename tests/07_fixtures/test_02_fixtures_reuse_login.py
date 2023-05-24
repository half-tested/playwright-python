import time
from typing import Dict

import pytest


@pytest.fixture(scope="session")
def logged_in_state(browser_type, base_url):
    context = browser_type.launch(headless=True).new_context(base_url=base_url)
    page = context.new_page()
    page.goto("/")
    page.get_by_label("Username").fill("default")
    page.get_by_label("Password").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    state = context.storage_state()
    context.close()
    return state


@pytest.fixture(scope="session")
def browser_context_args(logged_in_state, browser_context_args) -> Dict:
    return {**browser_context_args, "storage_state": logged_in_state}


def test_first_reusing_signed_in_state(page):
    page.goto("/tests")
    time.sleep(4)
    assert page.title() == "Test Cases"


def test_second_reusing_signed_in_state(page):
    page.goto("/runs")
    time.sleep(4)
    assert page.title() == "Test Runs"