import csv
import os
import random
import string

import pytest
from playwright.sync_api import expect, Page, Frame


def test_event_download(login, page):
    page.goto("/tests")
    with page.expect_download() as download_info:
        page.get_by_role("button", name="Download tests").click()
    download = download_info.value
    path = download.path()
    with open(path, newline='') as csvfile:
        total = sum(1 for _ in csv.reader(csvfile)) - 1  # -1 removes header
    expect(page.locator(".tableTitle span"), "Downloaded csv file should contain all test cases") \
        .to_have_text(f"(Total {total})")


@pytest.fixture()
def csv_file(page: Page):
    file_name = "new_tests.csv"
    random_suffix = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
    data = [
        ["summary", "description"],
        [f"{random_suffix} first test case", f"{random_suffix} first description"],
        [f"{random_suffix} second test case", f"{random_suffix} second description"]
    ]
    with open(file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)
    yield file_name
    os.remove(file_name)
    token = page.context.storage_state()["cookies"][0].get("value")
    headers = {"X-CSRFToken": f"{token}"}
    response = page.request.get("/api/tests?size=500", headers=headers)
    tests = response.json()["tests"]
    for test in tests:
        if random_suffix in test["name"]:
            page.request.delete(f"/api/tests/{test['id']}", headers=headers)


def test_event_file_chooser(login, csv_file, page):
    page.goto("/tests")
    with page.expect_file_chooser() as fc_info:
        page.get_by_role("link", name="UPLOAD TESTS").click()
    file_chooser = fc_info.value
    file_chooser.set_files(csv_file)
    page.pause()


def test_event_expect_request(login, page):
    page.set_default_timeout(5_000)  # change the default maximum time for all the methods accepting `timeout` option
    with page.expect_request("**/getstat/") as request:
        page.goto("/")
    assert request.value.method == "GET"
    assert request.value.url == "http://127.0.0.1:8000/getstat/"


def test_event_expect_page(login, page, context):
    context.set_default_timeout(5_000)  # change the default maximum time for all the methods accepting `timeout` option
    page.goto("/demoPages")
    # get page after a specific action (e.g. clicking a button, link etc.)
    with context.expect_page() as new_page_info:
        page.get_by_role("button", name="new page").click(modifiers=["Shift"])
    new_page = new_page_info.value
    assert len(context.pages) == 2


def test_event_expect_frame_attached(login, page):
    with page.expect_event("frameattached") as event_info:
        page.goto("/demoControls")
    frame: Frame = event_info.value
    frame.get_by_role("textbox").type("text")
    page.pause()
