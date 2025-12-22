from playwright.sync_api import Page, expect


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

        # Locators
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.login_button = page.locator("#login-button")
        self.error_message = page.locator("[data-test='error']")
        self.logo = page.locator(".login_logo")

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def get_error_message(self) -> str:
        return self.error_message.text_content()

    def is_login_page_loaded(self) -> bool:
        return self.logo.is_visible() and self.login_button.is_visible()

    def verify_login_page_loaded(self):
        expect(self.logo).to_be_visible()
        expect(self.login_button).to_be_visible()
