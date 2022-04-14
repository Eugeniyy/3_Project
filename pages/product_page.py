#product_page - модуль с продуктом

from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import math
import time

class ProductPage(BasePage):
    def get_product_info(self):
        self.product = str(self.browser.find_element(*ProductPageLocators.PRODUCT_TXT).text)
        self.price_product = str(self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT_TXT).text)

    def add_product_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_PRODUCT_LINK)
        add_product.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_product(self):
        time.sleep(2)
        self.basket_product = str(self.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_TXT).text)
        assert self.basket_product == self.product, f'basket_product="{self.basket_product}" not equal product="{self.product}"'
    
    def check_price_product(self):
        self.basket_price_product = str(self.browser.find_element(*ProductPageLocators.BASKET_PRICE_PRODUCT_TXT).text)
        assert self.basket_price_product == self.price_product, f'basket_product="{self.basket_price_product}" not equal product="{self.price_product}"'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented"

    def should_dissapear_success_message(self):
        assert self.is_dissapeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message didn't disappear"
