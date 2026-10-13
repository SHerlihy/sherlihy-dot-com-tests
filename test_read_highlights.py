from typing import TypedDict

import pytest
from playwright.sync_api import Page, expect
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
@pytest.mark.path("")
@scenario('features/readHighlights.feature', 'I want to read about a highlight.')
def test_read_highlight() -> None:
    pass


@given('this is the first time I am using the website')
def access_homepage(shared: Shared, browser_page: Page):
    shared["page"] = browser_page
    shared["actions"] = Navigation(browser_page)


@when('Open the navigation menu')
def click_navigate_button(shared: Shared):
    assert shared["actions"] is not None
    shared["actions"].click_navigate_button()


@when(parsers.parse('Click the {highlight_name} link'))
def click_highlight_button(shared: Shared, highlight_name: str):
    assert shared["actions"] is not None
    shared["actions"].click_link_with_text(highlight_name)


@then('An image is present')
def assert_image_present(shared: Shared):
    assert shared["page"] is not None
    an_image = shared["page"].get_by_role("img").first
    expect(an_image).to_be_visible()


@then(parsers.parse('Text is shown including {key_sentence}'))
def assert_key_sentence_shown(shared: Shared, key_sentence: str):
    assert shared["page"] is not None
    highlight_text = shared["page"].get_by_text(key_sentence).first

    expect(highlight_text).to_be_visible()
