def test_locators_list(page):
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").fill("default")
    page.get_by_label("Password:").fill("QADqwerty")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Test Cases").click()

    rows = page.locator("tbody tr")
    row_count = rows.count()
    print("row count:", row_count)                                                              # count

    first_row = rows.first                                                                      # first
    last_row = rows.last                                                                        # last
    second_row = rows.nth(1)                                                                    # nth
    print("first row:", first_row.locator("td").first.text_content())
    print("last row:", last_row.locator("td").first.text_content())
    print("second row:", second_row.locator("td").first.text_content())

    failed_rows = rows.filter(has=page.locator(".FAIL"))
    for row in failed_rows.all():                                                               # all
        print("failed row:", row.locator("td").first.text_content())

    not_failed_rows = page.locator("tbody tr").filter(has_not=page.locator(".FAIL"))
    print("not failed rows:", not_failed_rows.locator("td:first-of-type").all_text_contents())  # all_text_contents
    page.pause()