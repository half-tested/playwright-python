def test_browser(browser):  # provides browser instance
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    context.close()

