def test_playwright(playwright):
    print(
        playwright.devices)  # another way to list all devices, however this list includes full configuration with user agent, screen resolution etc.

    api_context = playwright.request.new_context()  # manipulate with REST API
    response = api_context.get("https://reqres.in/api/users/2")
    print(response)
    api_context.dispose()

    chromium = playwright.chromium.launch(headless=False)  # custom browser manipulations
    chromium_context = chromium.new_context()
    chromium_page = chromium_context.new_page()
    chromium_page.goto("https://www.chromium.org/Home/")
    chromium_context.close()

