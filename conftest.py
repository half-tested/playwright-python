import pytest
from playwright.sync_api import Page


@pytest.fixture()
def login(page: Page):
    payload = {
        "username": "default",
        "password": "QADqwerty"
    }
    page.request.post("/api/auth/login", data=payload)
