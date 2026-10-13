import re
from typing import TypedDict

import pytest
from playwright.sync_api import Page, BrowserContext,  expect
from pytest_bdd import given, parsers, scenario, then, when

from page_action.navigation import Navigation


class Shared(TypedDict):
    page: Page | None
    actions: Navigation | None


@pytest.fixture
def shared() -> Shared:
    return {
        "page": None,
        "actions": None,
    }


@pytest.mark.usefixtures("browser_page")
def before_scenario(context, scenario):
    current_browser = getattr(context, "browser_name", None) or context.config.userdata.get("browser", "chromium")

    if current_browser == "firefox":
        print(f"--> Skipping scenario '{scenario.name}' on Firefox.")
        scenario.skip("Firefox is not supported for this test suite.")


@pytest.mark.path("")
@scenario('features/copyKeyInformation.feature', 'I want to copy key information')
def test_external_links() -> None:
    pass


@given('this is the first time I am using the website')
def access_homepage(shared: Shared, browser_page: Page):
    shared["page"] = browser_page
    shared["actions"] = Navigation(browser_page)


@when(parsers.parse('I click the copy button next to {key_information}'))
def click_navigate_button(context: BrowserContext, shared: Shared, key_information:str):
    assert shared["actions"] is not None
    context.grant_permissions(["clipboard-write"])
    shared["actions"].click_info_copy_button(key_information)


@then(parsers.parse('The copy button next to {key_information} turns {confirm_color}'))
def assert_image_present(shared: Shared, key_information:str, confirm_color:str):
    assert shared["page"] is not None
    key_information_element = shared["page"].get_by_text(key_information).first

    copy_button = key_information_element.locator(
        "xpath=following::*[self::button or @role='button'][1]"
    )

    svg_elements = copy_button.locator("svg").all()

    green_match = re.compile(rf"{confirm_color}")

    for svg in svg_elements:
        expect(svg).to_have_class(green_match)


@then(parsers.parse('{key_information} is added to clipboard'))
def assert_key_sentence_shown(context: BrowserContext, shared: Shared, key_information: str):
    assert shared["page"] is not None
    context.grant_permissions(["clipboard-read"])
    clipboard_text = shared["page"].evaluate("navigator.clipboard.readText()")
    assert clipboard_text == key_information
