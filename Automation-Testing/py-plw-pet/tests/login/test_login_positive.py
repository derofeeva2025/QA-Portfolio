import allure
from playwright.sync_api import expect

from pages.login_page import LoginPage

@allure.feature("Login")
@allure.title("Login with correct username and password")
@allure.severity(allure.severity_level.CRITICAL)
@allure.id("TC-LOGIN-001")
def test_successful_login(page):
    login = LoginPage(page)
    login.open()
    login.login("standard_user", "secret_sauce")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")