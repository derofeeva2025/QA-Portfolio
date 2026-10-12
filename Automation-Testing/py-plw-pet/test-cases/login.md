# Test cases: Login page

**Application under test:** [Swag Labs (saucedemo.com)](https://www.saucedemo.com)
**Feature:** Login form
**Test types:** Positive, Negative, Boundary, Security, UI
**Priority:** High / Medium / Low

## Test data

Public demo credentials listed on the login page itself (not secrets).

| Alias | Username | Password |
|---|---|---|
| Valid user | `standard_user` | `secret_sauce` |
| Locked user | `locked_out_user` | `secret_sauce` |
| Unknown user | `nouser` | `secret_sauce` |
| Wrong password | `standard_user` | `wrong_password` |

## Coverage summary

Automation status: ✅ automated, ⬜ not automated yet. Update the last column as scripts are written.

| ID | Title | Type | Priority | Automated test |
|---|---|---|---|---|
| TC-LOGIN-001 | Successful login with valid credentials | Positive | High | ⬜ |
| TC-LOGIN-002 | Successful login by pressing Enter | Positive | Medium | ⬜ |
| TC-LOGIN-003 | Logout returns the user to the login page | Positive | High | ⬜ |
| TC-LOGIN-004 | Login with a wrong password | Negative | High | ⬜ |
| TC-LOGIN-005 | Login with an unknown username | Negative | High | ⬜ |
| TC-LOGIN-006 | Login with both fields empty | Negative | Medium | ⬜ |
| TC-LOGIN-007 | Login with an empty password | Negative | Medium | ⬜ |
| TC-LOGIN-008 | Login with an empty username | Negative | Medium | ⬜ |
| TC-LOGIN-009 | Login as a locked-out user | Negative | High | ⬜ |
| TC-LOGIN-010 | Username is case-sensitive | Boundary | Medium | ⬜ |
| TC-LOGIN-011 | Username with a leading space is rejected | Boundary | Low | ⬜ |
| TC-LOGIN-012 | Inventory page is not accessible without login | Security | High | ⬜ |
| TC-LOGIN-013 | Password field masks the entered characters | Security | Medium | ⬜ |
| TC-LOGIN-014 | Error message can be closed | UI | Low | ⬜ |
| TC-LOGIN-015 | Login form shows field placeholders and a green Login button | UI | Low | ✅ `test_login_field_exists` |

---

## Positive

### TC-LOGIN-001: Successful login with valid credentials
- **Priority:** High | **Type:** Positive
- **Preconditions:** User is not logged in.
- **Test data:** Valid user
- **Steps:**
  1. Open https://www.saucedemo.com
  2. Enter the valid username in the Username field.
  3. Enter the valid password in the Password field.
  4. Click **Login**.
- **Expected result:** The user is redirected to `/inventory.html`. The page title area shows **Products**. No error message is displayed.

### TC-LOGIN-002: Successful login by pressing Enter
- **Priority:** Medium | **Type:** Positive
- **Preconditions:** User is not logged in.
- **Test data:** Valid user
- **Steps:**
  1. Open the login page.
  2. Enter the valid username and password.
  3. Press **Enter** while the focus is in the Password field (do not click Login).
- **Expected result:** The user is redirected to `/inventory.html` and sees **Products**.

### TC-LOGIN-003: Logout returns the user to the login page
- **Priority:** High | **Type:** Positive
- **Preconditions:** User is logged in as the valid user.
- **Steps:**
  1. Click the menu (burger) button in the top-left corner.
  2. Click **Logout**.
- **Expected result:** The login page is displayed with an empty form and the **Login** button visible.

## Negative

### TC-LOGIN-004: Login with a wrong password
- **Priority:** High | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Test data:** Wrong password
- **Steps:**
  1. Open the login page.
  2. Enter `standard_user` in Username and `wrong_password` in Password.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Username and password do not match any user in this service`.

### TC-LOGIN-005: Login with an unknown username
- **Priority:** High | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Test data:** Unknown user
- **Steps:**
  1. Open the login page.
  2. Enter `nouser` in Username and `secret_sauce` in Password.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Username and password do not match any user in this service`.

### TC-LOGIN-006: Login with both fields empty
- **Priority:** Medium | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Steps:**
  1. Open the login page.
  2. Leave Username and Password empty.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Username is required`.

### TC-LOGIN-007: Login with an empty password
- **Priority:** Medium | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Steps:**
  1. Open the login page.
  2. Enter `standard_user` in Username; leave Password empty.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Password is required`.

### TC-LOGIN-008: Login with an empty username
- **Priority:** Medium | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Steps:**
  1. Open the login page.
  2. Leave Username empty; enter `secret_sauce` in Password.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Username is required`.

### TC-LOGIN-009: Login as a locked-out user
- **Priority:** High | **Type:** Negative
- **Preconditions:** User is not logged in.
- **Test data:** Locked user
- **Steps:**
  1. Open the login page.
  2. Enter `locked_out_user` and `secret_sauce`.
  3. Click **Login**.
- **Expected result:** The user stays on the login page. Error message is shown: `Epic sadface: Sorry, this user has been locked out.`

## Boundary

### TC-LOGIN-010: Username is case-sensitive
- **Priority:** Medium | **Type:** Boundary
- **Preconditions:** User is not logged in.
- **Steps:**
  1. Open the login page.
  2. Enter `STANDARD_USER` (upper case) in Username and `secret_sauce` in Password.
  3. Click **Login**.
- **Expected result:** Login is rejected. Error message is shown: `Epic sadface: Username and password do not match any user in this service`.

### TC-LOGIN-011: Username with a leading space is rejected
- **Priority:** Low | **Type:** Boundary
- **Preconditions:** User is not logged in.
- **Steps:**
  1. Open the login page.
  2. Enter ` standard_user` (with a space before the name) and `secret_sauce`.
  3. Click **Login**.
- **Expected result:** Login is rejected. Error message is shown: `Epic sadface: Username and password do not match any user in this service`.

## Security

### TC-LOGIN-012: Inventory page is not accessible without login
- **Priority:** High | **Type:** Security
- **Preconditions:** User is not logged in (new browser session).
- **Steps:**
  1. Open https://www.saucedemo.com/inventory.html directly.
- **Expected result:** The product list is not shown. The login form is displayed with the error: `Epic sadface: You can only access '/inventory.html' when you are logged in.`

### TC-LOGIN-013: Password field masks the entered characters
- **Priority:** Medium | **Type:** Security
- **Preconditions:** User is on the login page.
- **Steps:**
  1. Enter any text in the Password field.
  2. Inspect the field type.
- **Expected result:** The Password field has `type="password"`; the characters are displayed as dots, not as plain text.

## UI

### TC-LOGIN-014: Error message can be closed
- **Priority:** Low | **Type:** UI
- **Preconditions:** User is on the login page.
- **Steps:**
  1. Click **Login** with both fields empty (an error appears).
  2. Click the **X** button inside the error message.
- **Expected result:** The error message disappears; the login form remains displayed.

### TC-LOGIN-015: Login form shows field placeholders and a green Login button
- **Priority:** Low | **Type:** UI
- **Preconditions:** User is on the login page.
- **Steps:**
  1. Open the login page.
  2. Look at the Username field, the Password field and the Login button.
- **Expected result:** The fields show the placeholders `Username` and `Password`. The **Login** button is green (`rgb(61, 220, 145)`).


