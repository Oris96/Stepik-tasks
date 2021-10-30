from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    # LOGIN_PAGE_TITLE = (By.TAG_NAME, 'title')
    # LOGIN_SUBMIT = (By.CSS_SELECTOR, '[name="login_submit"]')
    # REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

