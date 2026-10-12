import pytest
from playwright.sync_api import Page

ALLOWED_BROWSERS = {"chromium", "firefox"}

def pytest_configure(config: pytest.Config) -> None:
    selected_browsers = config.getoption("browser") or ALLOWED_BROWSERS
    unsupported_browsers = set(selected_browsers) - ALLOWED_BROWSERS
    if unsupported_browsers:
        unsupported = ", ".join(sorted(unsupported_browsers))
        allowed = ", ".join(sorted(ALLOWED_BROWSERS))
        raise pytest.UsageError(
            f"Unsupported browser: {unsupported}. Allowed browsers: {allowed}"
        )

    config.addinivalue_line(
        "markers", "url(url): navigate the browser_page fixture to this URL"
    )


@pytest.fixture
def browser_page(page: Page, request: pytest.FixtureRequest) -> Page:
    marker = request.node.get_closest_marker("url")
    if marker is None or len(marker.args) != 1 or not isinstance(marker.args[0], str):
        pytest.fail("browser_page requires exactly one URL in a @pytest.mark.url marker")

    page.goto(marker.args[0])
    return page
