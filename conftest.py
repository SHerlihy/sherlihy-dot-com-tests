import pytest
import playwright
import json

from playwright.sync_api import Playwright

with open('data/supported_browsers.json') as f:
    supported_browser_list = tuple(json.load(f))

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store", 
        default="chromium", 
        choices=supported_browser_list,
        help=f"choose from {supported_browser_list}"
    )

@pytest.fixture(scope="function")
def browser_page(playwright: Playwright, request):
    browser_name = request.config.getoption("browser_name")
    marker = request.node.get_closest_marker("url")
    if marker == None:
        raise Exception(f"mark for url not present")

    url = marker.args[0]

    browser = playwright[browser_name].launch()
    context = browser.new_context()
    page = context.new_page()
    try:
        page.goto(url)
        yield page
    finally:
        context.close()
        browser.close()
