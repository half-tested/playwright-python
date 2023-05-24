def test_locators_arguments(page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()

    # locator arguments: has, has_not, has_text, has_not_text
    #   1. has, has_not
    fail_status = page.locator(".FAIL")
    fail_rows = page.locator("tbody tr", has=fail_status)                    # has child element
    print("failed tests count:", fail_rows.count())
    not_fail_rows = page.locator("tbody tr", has_not=fail_status)            # has_not child element
    print("not failed tests count:", not_fail_rows.count())
    #   2. has_text, has_not_text
    rows_with_text = page.locator("tbody tr", has_text="Login test")         # has_text for child element
    print("rows with text 'Login test':", rows_with_text.count())
    rows_without_text = page.locator("tbody tr", has_not_text="Login test")  # has_not_text for child element
    print("rows without text 'Login test':", rows_without_text.count())
