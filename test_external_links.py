from typing import TypedDict

import pytest
from playwright.sync_api import Locator, Page, BrowserContext,  expect
from pytest_bdd import given, parsers, scenario, then, when

from page_action.home import Home


class Shared(TypedDict):
    page: Page | None
    actions: Home | None
    external_page: Page | None


@pytest.fixture
def shared() -> Shared:
    return {
        "page": None,
        "actions": None,
        "external_page": None,
    }


@pytest.mark.usefixtures("browser_page")
@pytest.mark.path("")
@scenario('features/externalLinks.feature', 'I want to visit linked websites')
def test_external_links() -> None:
    pass


@given('this is the first time I am using the website')
def access_homepage(shared: Shared, browser_page: Page):
    shared["page"] = browser_page
    shared["actions"] = Home(browser_page)


@when(parsers.parse('I click the {link_name} link'))
def click_link(context:BrowserContext, shared: Shared, link_name: str):
    assert shared["actions"] is not None
    with context.expect_page() as new_page_info:
        shared["actions"].click_link(link_name)

    shared["external_page"] = new_page_info.value

@then(parsers.parse('{link_address} is visited'))
def assert_query_in_chat(shared: Shared, link_address: str):
    assert shared["external_page"] is not None

    expect(shared["external_page"]).to_have_url(link_address)
