from playwright.sync_api import Page, expect
# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def open(self):
        self.page.goto("https://www.saucedemo.com")

    def login_button_color(self):
        expect(self.login_btn).to_have_css("background-color", "rgb(61, 220, 145)")
