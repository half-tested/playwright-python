import pytest
import json
from playwright.sync_api import Page, Route, expect

# mocked data for '/getstat' endpoint that fetch data
# {"total": 11, "passed": 7, "failed": 1, "norun": 3}
total = "99"
passed = "99"
failed = "99"
norun = "99"


@pytest.fixture()
def mock_stats(page: Page):
    link = "**/getstat/"
    payload = json.dumps({"total": f"{total}", "passed": f"{passed}", "failed": f"{failed}", "norun": f"{norun}"})

    def handle(route: Route):
        route.fulfill(status=200, body=payload)

    page.route(link, handle)
    yield
    page.unroute(link)


def test_mock_api(page: Page, login, mock_stats):
    page.goto("/")
    expect(page.locator(".noRun span")).to_have_text(norun)
    expect(page.locator(".passed span")).to_have_text(passed)
    expect(page.locator(".failed span")).to_have_text(failed)
    expect(page.locator(".total span")).to_have_text(total)
    page.pause()
