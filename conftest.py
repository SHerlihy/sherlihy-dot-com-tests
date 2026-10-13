import settings
import pytest
from playwright.sync_api import Page

ALLOWED_BROWSERS = ["chromium", "firefox"]

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "base_url": settings.BASE_URL,
    }

def pytest_configure(config: pytest.Config) -> None:
    selected_browsers = config.getoption("browser")
    if not selected_browsers:
        selected_browsers = ALLOWED_BROWSERS
        config.option.browser = ALLOWED_BROWSERS

    unsupported_browsers = set(selected_browsers) - set(ALLOWED_BROWSERS)
    if unsupported_browsers:
        unsupported = ", ".join(sorted(unsupported_browsers))
        allowed = ", ".join(sorted(ALLOWED_BROWSERS))
        raise pytest.UsageError(
            f"Unsupported browser: {unsupported}. Allowed browsers: {allowed}"
        )

    config.addinivalue_line(
        "markers", "path(path): navigate the browser_page fixture to this path"
    )


@pytest.fixture
def browser_page(page: Page, request: pytest.FixtureRequest) -> Page:
    marker = request.node.get_closest_marker("path")
    if marker is None or len(marker.args) != 1 or not isinstance(marker.args[0], str):
        pytest.fail("browser_page requires exactly one path in a @pytest.mark.path marker")

    page.goto(marker.args[0])
    return page
