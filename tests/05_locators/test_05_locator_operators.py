def test_locator_operators(page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")

    page.get_by_role("button").or_(page.get_by_title("Login")).click()     # or_() matches one of locators

    page.get_by_role("link").and_(page.get_by_text("Test Cases")).click()  # and_() matches several locators

    load_more_buttons = page.locator(".loadMore")
    print("load_more_buttons:", load_more_buttons.count())
    load_more_visible_buttons = load_more_buttons.locator("visible=true")  # visible
    print("load_more_visible_buttons:", load_more_visible_buttons.count())
    page.pause()
