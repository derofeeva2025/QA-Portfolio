# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    def open(self):
        self.page.goto("https://www.saucedemo.com")