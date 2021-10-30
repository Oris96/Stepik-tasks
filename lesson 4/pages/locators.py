from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    LOGIN_EMAIL = (By.CSS_SELECTOR, '[name="login-username"]')
    LOGIN_PASSWORD = (By.CSS_SELECTOR, '[name="login-password"]')
    REGISTER_EMAIL = (By.CSS_SELECTOR, '[name="registration-email"]')
    REGISTER_PASSWORD = (By.CSS_SELECTOR, '[name="registration-password1"]')
    REGISTER_PASSWORD_CONFIRM = (By.CSS_SELECTOR, '[name="registration-password2"]')
    REGISTER_SUBMIT = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ProductPageLocators:
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, '[value="Add to basket"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    BASKET_PRODUCT_NAME = (By.CSS_SELECTOR, '.alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')
    BASKET_PRODUCT_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, '.basket-mini a')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    EMPTY_BASKET = (By.CSS_SELECTOR, '#content_inner p')
