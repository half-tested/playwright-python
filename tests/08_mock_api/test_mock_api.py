import re

import pytest
import json
from playwright.sync_api import Page, Route, Request


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "alice",
        "password": "Qamania123"
    }
    page.request.post("/api/auth/login", data=payload)
    # page.goto("/")


# mocked data for '/getstat' endpoint that fetch data
# {"total": 11, "passed": 7, "failed": 1, "norun": 3}
total = 99
passed = 99
failed = 99
norun = 99


@pytest.fixture()
def mock_stats(page):
    link = "**/getstat/"
    payload = json.dumps({"total": f"{total}", "passed": f"{passed}", "failed": f"{failed}", "norun": f"{norun}"})

    print('payload', payload)

    def handle(route: Route):
        route.fulfill(status=200, body=payload)

    page.route(link, handle)
    yield
    page.unroute(link)


@pytest.fixture()
def no_images(page):
    page.route("**/*", lambda route: route.abort() if route.request.resource_type == "image" else route.continue_())
    yield
    page.unroute("**/*")


@pytest.fixture()
def changed_welcome(page):
    def handle_route(route: Route) -> None:
        # Fetch original response.
        response = route.fetch()
        # Add a prefix to the title.
        body = response.text()
        body = body.replace("Hello", "Greetings")
        route.fulfill(
            # Pass all fields from the response.
            response=response,
            # Override response body.
            body=body,
        )

    page.route("**/", handle_route)
    yield
    page.unroute("**/")


def test_mock_api(login, mock_stats, no_images, changed_welcome, page):
    page.goto("/")
    print('No Run:', page.locator(".noRun span").text_content())
    print('Passed:', page.locator(".passed span").text_content())
    print('Failed:', page.locator(".failed span").text_content())
    print('Total:', page.locator(".total span").text_content())
    page.pause()
