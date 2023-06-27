import pytest
from playwright.sync_api import ConsoleMessage


@pytest.mark.parametrize(
    argnames="page_name",
    argvalues=["/", "/tests", "/runs", "/test/new", "/demoPages", "/demoControls"])
def test_event_one_off_listener(login, page, page_name):
    page.goto("/")
    console_errors = []

    def console_has_no_errors(message: ConsoleMessage):
        if message.type == "error":
            console_errors.append(message.text)

    page.once("console", console_has_no_errors)
    page.goto(page_name, wait_until="networkidle")
    assert len(console_errors) == 0, f"'{page_name}' generated with error {console_errors}"
