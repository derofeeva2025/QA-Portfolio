import allure
from pages.login_page import LoginPage

@allure.feature("Login form")
@allure.title("Login page has username, password and a green button")
@allure.severity(allure.severity_level.CRITICAL)

def test_login_field_exists(page):
    login = LoginPage(page)
    login.open()

    assert login.username.count() > 0
    print("✅Login field exists")
    assert login.password.count() > 0
    print("✅Password field exists")
    login.login_button_color()
    print("✅Login button is green")



