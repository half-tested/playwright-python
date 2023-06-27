import pytest
from playwright.sync_api import Page, Route, expect


@pytest.fixture()
def no_images(page: Page):
    page.route("**/*", lambda route: route.abort() if route.request.resource_type == "image" else route.fallback())
    yield
    page.unroute("**/*")


@pytest.fixture()
def changed_welcome(page, base_url):
    def handle_route(route: Route):
        response = route.fetch()
        body = response.text()
        body = body.replace("Hello,", "Greetings,")
        route.fulfill(response=response, body=body)

    page.route(f"{base_url}/**", handle_route)
    yield
    page.unroute(f"{base_url}/**")


def test_mock_api(page, login, changed_welcome, no_images):
    page.goto("/")
    expect(page.locator(".account")).to_contain_text("Greetings,")
    page.pause()
