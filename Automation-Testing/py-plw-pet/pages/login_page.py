import allure
from playwright.sync_api import expect

# pages/login_page.py
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.login_btn = page.locator("#login-button")

    @allure.step("Open login page")
    def open(self):
        self.page.goto("https://www.saucedemo.com")

    @allure.step("Login button is green check")
    def login_button_color(self):
        expect(self.login_btn).to_have_css("background-color", "rgb(61, 220, 145)")

    @allure.step("Login with username and password")
    def login(self, username, password): #def method in class
        self.username.fill(username)
        self.password.fill(password)
        self.login_btn.click()
