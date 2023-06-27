import os
import time
from typing import Dict

import pytest
from playwright.sync_api import Browser


@pytest.fixture(scope="session", autouse=True)
def make_auth_file_state(browser: Browser, browser_context_args: Dict):
    context = browser.new_context(**browser_context_args)
    page = context.new_page()
    page.goto("/")
    page.get_by_label("Username").fill("default")
    page.get_by_label("Password").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    context.storage_state(path=".auth")
    context.close()
    yield
    if os.path.exists(".auth"):
        os.remove(".auth")


@pytest.fixture(scope="session")
def context(browser: Browser, browser_context_args: Dict):
    context = browser.new_context(**browser_context_args, storage_state=".auth")
    yield context
    context.close()


def test_first_reusing_signed_in_state(page, base_url):
    page.goto("/tests")
    time.sleep(5)
    assert page.title() == "Test Cases"


def test_second_reusing_signed_in_state(page):
    page.goto("/runs")
    time.sleep(5)
    assert page.title() == "Test Runs"