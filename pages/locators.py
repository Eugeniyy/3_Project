#locators.py - модуль с селекторами

from selenium.webdriver.common.by import By

class MainPageLocators():
    
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():

    PRODUCT_TXT = (By.CSS_SELECTOR, ".col-sm-6.product_main > h1")
    PRICE_PRODUCT_TXT = (By.CSS_SELECTOR, ".col-sm-6.product_main > .price_color")
    
    BASKET_PRODUCT_TXT = (By.CSS_SELECTOR, ".alert:nth-child(1) > .alertinner > strong")
    BASKET_PRICE_PRODUCT_TXT = (By.CSS_SELECTOR, ".alert:nth-child(3) >.alertinner > p > strong")
    
    ADD_PRODUCT_LINK = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group > a.btn.btn-default")

    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")