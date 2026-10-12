#only negative cases for users, user-pass pairs, expected messages
ERR_INVALID_CREDENTIALS = "Epic sadface: Username and password do not match any user in this service"
ERR_USERNAME_REQUIRED = "Epic sadface: Username is required"
ERR_LOCKED_USER = "Epic sadface: Sorry, this user has been locked out."
ERR_PASSWORD_REQUIRED = "Epic sadface: Password is required"

INVALID_LOGIN_CASES = [
    ("locked_out_user", "secret_sauce",ERR_LOCKED_USER ),
    ("nouser", "secret_sauce", ERR_INVALID_CREDENTIALS),
    ("standard_user", "wrong_password", ERR_INVALID_CREDENTIALS),
    ("", "", ERR_USERNAME_REQUIRED),
    ("standard_user", "", ERR_PASSWORD_REQUIRED),
    ("", "secret_sauce", ERR_USERNAME_REQUIRED),
    ("STANDARD_USER", "secret_sauce", ERR_INVALID_CREDENTIALS),
    (" standard_user", "secret_sauce", ERR_INVALID_CREDENTIALS),
]