import pytest
from playwright.sync_api import Page, expect
from config.config import Config
from tests.ui.pages.login_page import LoginPage


@pytest.mark.ui
class TestLogin:

    def test_login_page_loaded(self, saucedemo_page: Page):
        login_page = LoginPage(saucedemo_page)
        login_page.verify_login_page_loaded()
        expect(saucedemo_page).to_have_title("Swag Labs")

        print("Login page is loaded")

    def test_successful_login(self, saucedemo_page: Page):
        login_page = LoginPage(saucedemo_page)

        login_page.login(
            username=Config.SAUCEDEMO_USERS["standard"],
            password=Config.SAUCEDEMO_PASSWORD,
        )

        expect(saucedemo_page).to_have_url("https://www.saucedemo.com/inventory.html")
        expect(saucedemo_page.locator(".title")).to_have_text("Products")

        print("Login is successful, User is at the page Products")

    def test_login_with_invalid_credentials(self, saucedemo_page: Page):
        login_page = LoginPage(saucedemo_page)

        login_page.login(username="invalid_user", password="invalid password")

        expect(login_page.error_message).to_be_visible()
        error_text = login_page.get_error_message()
        assert "Epic sadface" in error_text

        print(f"Error message: {error_text}")

    def test_login_locked_user(self, saucedemo_page: Page):
        login_page = LoginPage(saucedemo_page)
        login_page.login(
            username=Config.SAUCEDEMO_USERS["locked"],
            password=Config.SAUCEDEMO_PASSWORD,
        )

        expect(login_page.error_message).to_be_visible()
        error_text = login_page.get_error_message()
        assert "locked out" in error_text.lower()

        print(f"Locked user can't login: {error_text}")
