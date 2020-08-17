from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, '#id_registration-password1')
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, '[name = "registration_submit"]')


class ProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    BASKET_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert-success .alertinner strong')
    BASKET_TOTAL = (By.CSS_SELECTOR, '.alert-info .alertinner strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6 .price_color')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group .btn:nth-child(1)')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner>p')
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, '.basket-items')
