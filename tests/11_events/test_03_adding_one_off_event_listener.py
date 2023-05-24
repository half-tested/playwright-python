from playwright.sync_api import Request


def test_event_expect_request(login, page):
    def track_request_once(request: Request):
        print("Request sent: " + request.url)

    page.goto("/")
    page.once("request", track_request_once)
    page.get_by_role("button", name="refresh stats").click()  # page.once() tracks request
    page.reload()
    page.get_by_role("button", name="refresh stats").click()  # however second time won't work
    page.goto("/tests")
