from pages.login_page import LoginPage

def test_login_field_exists(page):
    login = LoginPage(page)
    login.open()

    assert login.username.count() > 0
    print("✅Login field exists")
    assert login.password.count() > 0
    print("✅Password field exists")
    login.login_button_color()
    print("✅Login button is green")



