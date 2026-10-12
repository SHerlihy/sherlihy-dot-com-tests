import pytest
import json
from playwright.sync_api import Playwright, expect, Page

from pageAction.home import Home

QUERY_URL = "https://om9v93ll69.execute-api.eu-west-2.amazonaws.com/prod/query"
TEST_API_KEY = "Zl5b1apCdZ9uGXszn1uaA2GUIwj6TDKW6CyowYZL"

def test_ChatNoAPIKey(playwright: Playwright):
    req_context = playwright.request.new_context(
        base_url=QUERY_URL
    )
    response = req_context.post(
            "/",
            data="hello"
            )

    expect(response).not_to_be_ok()
    assert response.status == 403

def test_ChatWithApiKey(playwright: Playwright):
    req_context = playwright.request.new_context(
        base_url=QUERY_URL,
        extra_http_headers={"x-api-key": TEST_API_KEY}
    )
    response = req_context.post(
        "/",
        data="hello"
    )

    expect(response).to_be_ok()
    assert response.status == 200
