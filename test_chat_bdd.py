import re
from typing import TypedDict

import pytest
from playwright.sync_api import Locator, Page, expect
from pytest_bdd import given, parsers, scenario, then, when

from page_action.home import Home


class Shared(TypedDict):
    page: Page | None
    actions: Home | None
    query_item: Locator | None


@pytest.fixture
def shared() -> Shared:
    return {
        "page": None,
        "actions": None,
        "query_item": None,
    }


@pytest.mark.usefixtures("browser_page")
@pytest.mark.path("")
@scenario('features/chatAI.feature', 'I want to query the AI')
def test_chat_query() -> None:
    pass


@given('this is the first time I am using the website')
def access_homepage(shared: Shared, browser_page: Page):
    shared["page"] = browser_page
    shared["actions"] = Home(browser_page)


@when(parsers.parse('I input {query} into the input box'))
def input_query(shared: Shared, query: str):
    assert shared["actions"] is not None
    shared["actions"].type_in_chat(query)


@when('I click the submit button')
def click_submit(shared: Shared):
    assert shared["actions"] is not None
    shared["actions"].click_submit_button()


@then(parsers.parse('{query} is shown in the chat section'))
def assert_query_in_chat(shared: Shared, query: str):
    assert shared["page"] is not None
    query_item = (
        shared["page"]
        .get_by_role("listitem")
        .filter(has_text=query)
        .first
    )
    shared["query_item"] = query_item

    expect(query_item).to_contain_text(query)

@then(parsers.parse('The answer is shown below {query}'))
def assert_answer_to_query(shared: Shared):
    assert shared["query_item"] is not None
    answer_item = shared["query_item"].locator(
        "xpath=following::*[self::li or @role='listitem'][1]"
    )

    expect(answer_item).to_be_visible()
    expect(answer_item).to_contain_text(re.compile(r"\S+"))
