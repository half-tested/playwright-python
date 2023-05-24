import os
import random
import string

import pytest
from playwright.sync_api import Page

from pages.DashboardPage import DashboardPage
from pages.LoginPage import LoginPage
from utils.db import Database


@pytest.fixture()
def home_page(page: Page) -> DashboardPage:
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("default", "QADqwerty")
    yield DashboardPage(page)


@pytest.fixture()
def db(request: pytest.FixtureRequest):
    # change db_file_path if TestApp project deployed in different location or service
    db_file_path = os.path.join(request.config.rootpath.parent, "TestApp/db.sqlite3")
    sqlite_db = Database(db_file_path)
    yield sqlite_db
    sqlite_db.close()


@pytest.fixture()
def random_test_name(db):
    random_string = ''.join(random.sample((string.ascii_uppercase + string.digits), 6))
    test_name = f"test {random_string}"
    yield test_name
    db.delete_test_case(test_name)


@pytest.fixture()
def created_test(random_test_name, db):
    db.create_test_case(random_test_name, f"description of {random_test_name}", "default")
    return random_test_name
