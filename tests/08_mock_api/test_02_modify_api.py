import pytest
from playwright.sync_api import Page, Route, expect


@pytest.fixture(params=['0', '99', '999', '9999'])
def updated_total_stat(page: Page, request):
    link = "**/getstat/"

    def handle(route: Route):
        response = route.fetch()
        stats = response.json()
        stats["total"] = request.param
        route.fulfill(response=response, json=stats)

    page.route(link, handle)
    yield request.param
    page.unroute(link)


def test_update_api(page: Page, login, updated_total_stat):
    page.goto("/")
    expect(page.locator(".total span")).to_have_text(updated_total_stat)
