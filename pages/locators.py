#locators.py - модуль с селекторами

from selenium.webdriver.common.by import By

class MainPageLocators():
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")

class ProductPageLocators():

    PRODUCT_TXT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_PRODUCT_TXT = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    
    BASKET_PRODUCT_TXT = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    BASKET_PRICE_PRODUCT_TXT = (By.CSS_SELECTOR, ".alert:nth-child(3) >.alertinner > p > strong")
    
    ADD_PRODUCT_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")

class BasePageLocators():

    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")

    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():

    BASKET_ITEMS = (By.CSS_SELECTOR, ".basket-items")
    BASKET_ITEMS_INVALID = (By.CSS_SELECTOR, "#login_link")
    MESSAGE_BASKET_EMPTY = (By.CSS_SELECTOR, "#content_inner>p")
    MESSAGE_BASKET_EMPTY_INVALID = (By.CSS_SELECTOR, "#content_inner>p_invalid")