"""
Fixture for UI tests (Playwright)
"""

import pytest
from config.config import Config
from playwright.sync_api import Page, Browser, BrowserContext


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": Config.HEADLESS, "slow_mo": 500 if not Config.HEADLESS else 0}


@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "viewport": Config.VIEWPORT,
        "locale": "uk-UA",
        "timezone_id": "Europe/Kyiv",
    }


@pytest.fixture
def page(page: Page) -> Page:
    page.set_default_timeout(Config.DEFAULT_TIMEOUT)
    yield page


@pytest.fixture
def saucedemo_page(page: Page) -> Page:
    page.goto(Config.SAUCEDEMO_BASE_URL)
    yield page
