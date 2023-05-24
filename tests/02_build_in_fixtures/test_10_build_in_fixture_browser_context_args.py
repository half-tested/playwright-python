import pytest


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):          # override arguments of browser.new_context()
    return {**browser_context_args,                      # such as base_url, viewport,
            "base_url": "https://playwright.dev/",       # color_scheme, record_video_dir etc.
            "color_scheme": "dark",
            "viewport": {"width": 800, "height": 600}
            }


def test_browser_context_args(page):  # opens a page according to base_url,
    page.goto("/")                    # provided color_scheme and screen resolution
