import pytest


@pytest.fixture(scope="session")
def browser_type_launch_args(browser_type_launch_args, playwright):  # override arguments of browser_type.launch()
    return {**browser_type_launch_args,                              # such as slow_mo, headless etc.
            "headless": False,
            "slow_mo": 2_000
            }


def test_browser_type_launch_args(page):  # opens a page in headed mode
    page.goto("https://www.google.com/")  # with slow down operations to 2 sec
    page.reload()


