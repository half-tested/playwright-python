import pytest
from playwright.sync_api import expect


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {**browser_context_args, "java_script_enabled": False}


def test_emulate_java_script_disabled(login, page):
    page.goto("/demoControls")
    page.get_by_placeholder("entered value appears next").type("new text")
    expect(page.locator("label.labelDemoResult")).to_have_text("")
    # Normally text in used input populated with javascript to next label.
    # However, javascript is disabled and application works differently.