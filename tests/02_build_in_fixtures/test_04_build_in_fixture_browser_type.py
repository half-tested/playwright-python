def test_browser_type(browser_type):  # provides object of selected browser by argument --browser
    browser = browser_type.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.google.com/")
    context.close()
    browser.close()
