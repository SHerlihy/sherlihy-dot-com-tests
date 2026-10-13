import os
import json

import pytest
from playwright.sync_api import Playwright, expect, Page

from page_action.home import Home

CHAT_URL = os.environ["CHAT_URL"] 
CHAT_API_KEY = os.environ["CHAT_API_KEY"]

def test_ChatNoAPIKey(playwright: Playwright):
    req_context = playwright.request.new_context(
        base_url=CHAT_URL
    )
    response = req_context.post(
            "/",
            data="hello"
            )

    expect(response).not_to_be_ok()
    assert response.status == 403

def test_ChatWithApiKey(playwright: Playwright):
    req_context = playwright.request.new_context(
        base_url=CHAT_URL,
        extra_http_headers={"x-api-key": CHAT_API_KEY}
    )
    response = req_context.post(
        "/",
        data="hello"
    )

    expect(response).to_be_ok()
    assert response.status == 200
