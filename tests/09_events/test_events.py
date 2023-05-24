import csv
import os
import random
import string

import pytest
from playwright.sync_api import Page, expect, ConsoleMessage, Dialog


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "alice",
        "password": "Qamania123"
    }
    page.request.post("/api/auth/login", data=payload)


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


@pytest.mark.parametrize(
    argnames="page_name",
    # argvalues=["Dashboard", "Test Cases", "Test Runs", "Create new test", "Demo pages", "Demo controls"])
    argvalues=["/", "/tests", "/runs", "/test/new", "/demoPages", "/demoControls"])
def test_event_one_off_listener(login, page, page_name):
    page.goto("/")
    console_errors = []

    def console_has_no_errors(message: ConsoleMessage):
        # assert message.type != "error", f"page: {page.url}, console error: {message.text}"
        if message.type == "error":
            console_errors.append(message.text)

    # page.on("request", lambda request: print(">>", request.method, request.url))
    # page.on("response", lambda response: print("<<", response.status, response.url))

    page.once("console", console_has_no_errors)
    # page.get_by_role("link", name=page_name).click()
    # page.wait_for_load_state("networkidle")
    page.goto(page_name, wait_until="networkidle")
    assert len(console_errors) == 0, f"'{page_name}' generated with error {console_errors}"


def test_event_permanent(login, page):
    page.goto("/")

    def track_request(request):
        print(">>", request.method, request.url)

    def track_response(response):
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
