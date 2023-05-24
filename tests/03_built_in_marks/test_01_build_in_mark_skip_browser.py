import pytest


@pytest.mark.skip_browser("firefox")  # skip test for browser firefox
def test_skip_browser(page):
    page.goto("/")

# pytest -k test_skip_browser --browser chromium --browser firefox
# outputs: 1 passed, 1 skipped
