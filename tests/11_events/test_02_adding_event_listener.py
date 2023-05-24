from playwright.sync_api import Request, Response


def test_event_permanent(login, page):
    page.goto("/")

    def track_request(request: Request):
        print(">>", request.method, request.url)

    def track_response(response: Response):
        print("<<", response.status, response.url)

    page.on("request", track_request)
    page.on("response", track_response)
    page.get_by_role("button", name="Refresh Stats").click()
    page.remove_listener("request", track_request)
    page.remove_listener("response", track_response)
    print("------------------------------------------")
    print("no tracked request/response going forward")
    print("------------------------------------------")
    page.get_by_role("button", name="Refresh Stats").click()
