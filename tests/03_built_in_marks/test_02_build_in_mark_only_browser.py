import pytest


@pytest.mark.only_browser("chromium")  # executes only for chromium
def test_only_browser(page):
    page.goto("/")

# pytest -k test_only_browser --browser chromium --browser firefox --browser webkit
# outputs: 1 passed, 2 skipped
