from playwright.sync_api import Page, expect

# Test requires a HAR file. Follow steps bellow:
# 1. Recording a HAR file
#    using page.route_from_har update=True argument
#    page.route_from_har("./hars/home_page.har", url="**/getstat/", update=True)
#
# 2. Modifying a HAR file
#    check ./hars/ for json file with content like
#    {"total": 4, "passed": 3, "failed": 1, "norun": 0}
#    and modify, for example, with
#    {"total": 400, "passed": 3, "failed": 1, "norun": 0}
#
# 3. Replaying from HAR file
#    using page.route_from_har update=False argument
#    page.route_from_har("./hars/home_page.har", url="**/getstat/", update=False)


def test_mock_with_files(page: Page, login):
    page.route_from_har("./hars/home_page.har", url="**/getstat/", update=True)
    page.goto("/")
    expect(page.locator(".total span")).to_have_text("400")
