"""
======================
Test generator
playwright codegen

1. run playwright codegen
playwright codegen http://127.0.0.1:8000 --target=python-pytest
copy/paste python code for pytest may run here with command:
pytest tests/01_tools/test_tools.py --headed

optional to discover:
    2. codegen useful option - browser storage reuse
    playwright codegen http://127.0.0.1:8000 --save-storage auth.json
    playwright codegen http://127.0.0.1:8000 --load-storage auth.json

    3. codegen useful option - run with specific window size
    playwright codegen --viewport-size=800,600 http://127.0.0.1:8000

    4. codegen useful option - emulate specific device
    playwright codegen --device="iPhone 13" http://127.0.0.1:8000

    5. codegen useful option - geolocation, language and timezone
    playwright open --timezone="Europe/Rome" --geolocation="41.890221,12.492348" --lang="it-IT" maps.google.com

    6. codegen other options
    playwright help codegen

======================
Trace viewer

1. create trace file
pytest -k test_tools.py --tracing=on

2. view trace file
playwright show-trace test-results/tests-01-tools-test-tools-py-test-example-chromium/trace.zip
"""
from typing import Dict

import pytest
from playwright.sync_api import Page, BrowserType


def test_example(page: Page) -> None:
    page.goto("http://127.0.0.1:8000/login")
    page.get_by_label("Username:").click()
    page.get_by_label("Username:").fill("alice")
    page.get_by_label("Password:").click()
    page.get_by_label("Password:").fill("Qamania123")
    page.get_by_label("Password:").press("Enter")
    page.get_by_role("link", name="Test Runs").click()



