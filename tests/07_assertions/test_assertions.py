from playwright.sync_api import expect


def test_assertions(page):
    payload = {
        "username": "alice",
        "password": "Qamania123"
    }
    api_response = page.request.post("/api/auth/login", data=payload)
    # API responses validation
    expect(api_response).to_be_ok()

    page.goto("/")
    # Page validation
    expect(page, "Assertion message may be set up").to_have_url("http://127.0.0.1:8000/", timeout=3000)
    expect(page).to_have_title("Simple Test management")

    # Locator validation
    expect(page.locator(".logOut"), "Logout icon is not displayed").to_be_visible()
    menu_items = ["Dashboard", "Test Cases", "Test Runs", "Create new test", "Demo pages", "Demo controls"]
    expect(page.locator("div.menuBox").get_by_role("listitem")).to_have_count(6, timeout=1000)
    expect(page.locator("div.menuBox").get_by_role("listitem")).to_have_text(menu_items)
    expect(page.locator("div.account")).to_contain_text("alice")
    expect(page.get_by_role("button", name="Refresh Stats")).to_have_attribute("onclick", "refreshStats()")