import hashlib
import os
from typing import Dict, Callable

import allure
import pytest
from playwright.sync_api import Page, Error, Browser, BrowserContext
from slugify import slugify


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


@pytest.fixture()
@allure.step("init default user credentials")
def default_user_creds():
    username = os.environ["default_user_username"]
    password = os.environ["default_user_password"]
    return User(username, password)


@pytest.fixture(scope="session")
def default_user_browser(
        launch_browser: Callable[[], Browser]
):
    browser = launch_browser()
    yield browser
    browser.close()


@pytest.fixture
def default_user_context(
        default_user_browser: Browser,
        browser_context_args: Dict,
        request: pytest.FixtureRequest,
):
    context = default_user_browser.new_context(**browser_context_args)
    start_tracing_if_set(context, request)

    yield context


@pytest.fixture
def default_user_page(default_user_context):
    page = default_user_context.new_page()
    yield page


def start_tracing_if_set(
        new_context: BrowserContext,
        request: pytest.FixtureRequest
):
    tracing_option = request.config.getoption("--tracing")
    capture_trace = tracing_option in ["on", "retain-on-failure"]
    if capture_trace:
        new_context.tracing.start(
            title=slugify(request.node.nodeid),
            screenshots=True,
            snapshots=True,
            sources=True,
        )


def is_failed(request: pytest.FixtureRequest) -> bool:
    return request.node.rep_call.failed if hasattr(request.node, "rep_call") else True


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    result = yield
    report = result.get_result()
    failed = report.outcome == 'failed'

    if call.when == "call" and "default_user_page" in item.funcargs:
        request = item.funcargs['request']
        page: Page = item.funcargs["default_user_page"]
        capture_trace_if_set(page.context, failed, "default_user", item, request)
        capture_screenshot_if_set(page, failed, "default_user", item, request)
        page.context.close()  # make sure context closed for the video
        capture_video_if_set(page, failed, "default_user", item, request)


def capture_video_if_set(
        page: Page,
        failed,
        role: str,
        item,
        request: pytest.FixtureRequest
):
    video_option = request.config.getoption("--video")
    preserve_video = video_option == "on" or (
            failed and video_option == "retain-on-failure"
    )
    if preserve_video and page.video:
        video = page.video
        try:
            path = _build_artifact_test_folder(item, f"{role}-video.webm", request)
            video.save_as(path=path)
            allure.attach(
                open(path, 'rb').read(),
                name=f"{role}-video.webm",
                attachment_type=allure.attachment_type.WEBM,
                extension="webm"
            )
            video.delete()
        except Error:
            # Silent catch empty videos.
            pass


def capture_screenshot_if_set(
        page,
        failed,
        role: str,
        item,
        request: pytest.FixtureRequest
):
    screenshot_option = request.config.getoption("--screenshot")
    capture_screenshot = screenshot_option == "on" or (
            failed and screenshot_option == "only-on-failure"
    )
    if capture_screenshot:
        human_readable_status = "failed" if failed else "finished"
        screenshot_path = _build_artifact_test_folder(item, f"{role}-test-{human_readable_status}.png", request)
        try:
            page.screenshot(timeout=5000, path=screenshot_path)
            allure.attach(
                page.screenshot(type='png'),
                name=f"{role}-test-{human_readable_status}.png",
                attachment_type=allure.attachment_type.PNG,
                extension="png"
            )
        except Error:
            pass


def capture_trace_if_set(
        context,
        failed,
        role: str,
        item,
        request: pytest.FixtureRequest
):
    tracing_option = request.config.getoption("--tracing")
    capture_trace = tracing_option in ["on", "retain-on-failure"]
    if capture_trace:
        retain_trace = tracing_option == "on" or (
                failed and tracing_option == "retain-on-failure"
        )
        if retain_trace:
            trace_path = _build_artifact_test_folder(item, f"{role}-trace.zip", request)
            context.tracing.stop(path=trace_path)
            allure.attach(
                open(trace_path, 'rb').read(),
                name=f"{role}-trace.zip",
                extension="zip"
            )
        else:
            context.tracing.stop()


def _build_artifact_test_folder(
        item,
        folder_or_file_name: str,
        request: pytest.FixtureRequest
) -> str:
    output_dir = request.config.getoption("--output")
    return os.path.join(output_dir, slugify(item.nodeid), folder_or_file_name)


def truncate_file_name(file_name: str) -> str:
    if len(file_name) < 256:
        return file_name
    return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"
