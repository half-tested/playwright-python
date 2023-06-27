import re

from playwright.sync_api import expect


def test_assertions(page):
    # API responses validation
    payload = {
        "username": "default",
        "password": "wrong_password"
    }
    api_response = page.request.post("/api/auth/login", data=payload)
    expect(api_response).not_to_be_ok()

    payload = {
        "username": "default",
        "password": "QADqwerty"
    }
    api_response = page.request.post("/api/auth/login", data=payload)
    expect(api_response).to_be_ok()
    expect(api_response, "API response status code is not in `200..299` range").to_be_ok()

    page.goto("/")
    # Page validation
    expect(page, "Assertion message may be set up").to_have_url("http://127.0.0.1:8000/", timeout=3000)
    expect(page).to_have_title("Simple Test management")
    expect(page).to_have_title(re.compile(r".*Test management"))
    expect(page).not_to_have_title("Not this title")
    expect(page).not_to_have_url("http://127.0.0.1:8000/bad_endpoint")

    # Locator validation
    expect(page.locator(".logOut"), "Logout icon is not displayed").to_be_visible()
    menu_items = ["Dashboard", "Test Cases", "Test Runs", "Create new test", "Demo pages", "Demo controls"]
    expect(page.locator("div.menuBox").get_by_role("listitem")).to_have_count(6, timeout=1000)
    expect(page.locator("div.menuBox").get_by_role("listitem")).to_have_text(menu_items)
    expect(page.locator("div.account")).to_contain_text("default")
    expect(page.get_by_role("button", name="Refresh Stats")).to_have_attribute("onclick", "refreshStats()")