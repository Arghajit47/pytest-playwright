class LoginPageLocators:
    COMPANY_LOGO = "img[alt='company-branding']"
    USERNAME_LOCATOR = ".orangehrm-login-error .oxd-text:nth-of-type(1)"
    PASSWORD_LOCATOR = ".orangehrm-login-error .oxd-text:nth-of-type(2)" #Hardcode Password Locator
    USER_DROPDOWN = ".oxd-userdropdown-tab"
    LOGOUT_BUTTON = '//a[@class="oxd-userdropdown-link"][contains(@href, "logout")]'
