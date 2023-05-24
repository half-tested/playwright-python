import pytest
from playwright.sync_api import Page


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "alice",
        "password": "Qamania123"
    }
    page.request.post("/api/auth/login", data=payload)
#
#
# import hashlib
# import os
# import random
# import string
#
# from _pytest.fixtures import FixtureRequest
#
# import allure
# import pytest
# from playwright.sync_api import Page, Error
# from slugify import slugify
#
#
# # class User:
# #     def __init__(self, username: str, password: str):
# #         self.username = username
# #         self.password = password
# #
# #
# # class Test:
# #     __test__ = False
# #
# #     def __init__(self, name: str, description: str):
# #         self.name = name
# #         self.description = description
# #
# #
# # @pytest.fixture()
# # @allure.step("init default user credentials")
# # def default_user():
# #     username = os.environ["default_user_username"]
# #     password = os.environ["default_user_password"]
# #     return User(username, password)
#
#
# # @pytest.fixture()
# # def random_string():
# #     return ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
# #
# #
# # @pytest.fixture()
# # def new_test_unique_data(random_string, page):
# #     name = f"test {random_string}"
# #     description = f"description from {name}"
# #     test = Test(name, description)
# #
# #     yield test
# #
# #     token = page.context.cookies()[0].get("value")
# #     headers = {"X-CSRFToken": f"{token}"}
# #     response = page.request.get("/api/tests?size=100500", headers=headers)
# #     tests = response.json()["tests"]
# #     for test_on_backend in tests:
# #         if test.name == test_on_backend["name"]:
# #             page.request.delete(f"/api/tests/{test_on_backend['id']}", headers=headers)
#
#
# # @pytest.fixture()
# # def teardown_clean_test_by_name(page):
# #     tests_to_delete = list()
# #
# #     def add_to_cleanup(test_name: str):
# #         tests_to_delete.append(test_name)
# #
# #     yield add_to_cleanup
# #
# #     token = page.context.cookies()[0].get("value")
# #     headers = {"X-CSRFToken": f"{token}"}
# #     response = page.request.get("/api/tests?size=100500", headers=headers)
# #     tests = response.json()["tests"]
# #     for test_to_delete in tests_to_delete:
# #         for test_on_backend in tests:
# #             if test_to_delete == test_on_backend["name"]:
# #                 page.request.delete(f"/api/tests/{test_on_backend['id']}", headers=headers)
#
# @pytest.fixture(scope='function', autouse=True)
# def add_artifacts_to_allure_teardown(request):
#     yield
#     attach_to_allure_report(request)
#     # failed = request.node.rep_call.failed
#     # if "page" in request.node.funcargs:
#     #     page: Page = request.node.funcargs["page"]
#     #     # todo change to add screenshot from result dir
#     #     capture_screenshot_if_set(page, failed, request)
#     #     capture_video_if_set(page, failed, request)
#
#
# # @pytest.hookimpl(hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     result = yield
# #     report = result.get_result()
# #     failed = report.outcome == 'failed'
# #     request = item.funcargs['request']
# #
# #     if call.when == "call" and "page" in item.funcargs:
# #         page: Page = item.funcargs["page"]
# #         #     capture_trace_if_set(page.context, failed, "sr", item)
# #         capture_screenshot_if_set(page, failed, request)
# #         # page.context.close()
# #         # capture_video_if_set(page, failed, item)
# #     # if call.when == "call" and "sm" in item.funcargs:
# #     #     page: Page = item.funcargs["sm"].page
# #     #     capture_trace_if_set(page.context, failed, "sm", item)
# #     #     capture_screenshot_if_set(page, failed, "sm", item)
# #     #     page.context.close()
# #     #     capture_video_if_set(page, failed, "sm", item)
#
#
# # def capture_screenshot_if_set(page, failed, request):
# #     screenshot_option = request.config.getoption("--screenshot")
# #     capture_screenshot = screenshot_option == "on" or (
# #             failed and screenshot_option == "only-on-failure"
# #     )
# #     if capture_screenshot:
# #         human_readable_status = "failed" if failed else "finished"
# #         try:
# #             page.screenshot(timeout=5000)
# #             allure.attach(
# #                 page.screenshot(type='png'),
# #                 name=f"test-{human_readable_status}.png",
# #                 attachment_type=allure.attachment_type.PNG
# #             )
# #         except Error:
# #             pass
# #
# #
# # def capture_video_if_set(page: Page, failed, request):
# #     video_option = request.config.getoption("--video")
# #     preserve_video = video_option == "on" or (
# #             failed and video_option == "retain-on-failure"
# #     )
# #     if preserve_video and page.video:
# #         video = page.video
# #         try:
# #             path = video.path()
# #             allure.attach(
# #                 open(path, 'rb').read(),
# #                 name="video.webm",
# #                 attachment_type=allure.attachment_type.WEBM
# #             )
# #             video.delete()
# #         except Error:
# #             # Silent catch empty videos.
# #             pass
# #
# #
# # def attach_video(request):
# #     path = artifact_test_folder(request)
# #     for file in os.listdir(path):
# #         if file.endswith(".webm"):
# #             allure.attach(
# #                 open(file, 'rb').read(),
# #                 name=f"trace.zip"
# #             )
#
#
# def attach_to_allure_report(request):
#     ext = (".png", ".webm", ".zip")
#     path = artifact_test_folder(request)
#     if not os.path.exists(path):
#         return
#     for file in os.listdir(path):
#         if file.endswith(ext):
#             allure.attach(
#                 open(os.path.join(path, file), 'rb').read(),
#                 name=f"{file}"
#             )
#
#
# def artifact_test_folder(request) -> str:
#     output_dir = request.config.getoption("--output")
#     return os.path.join(output_dir, truncate_file_name(slugify(request.node.nodeid)))
#
#
# def truncate_file_name(file_name: str) -> str:
#     if len(file_name) < 256:
#         return file_name
#     return f"{file_name[:100]}-{hashlib.sha256(file_name.encode()).hexdigest()[:7]}-{file_name[-100:]}"
