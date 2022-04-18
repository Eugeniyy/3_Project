#basket_page.py - содержит методы работы со страницей корзины

from .locators import BasketPageLocators
from .base_page import BasePage

class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Basket items is presented"
    
    def should_be_basket_empty_invalid(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_INVALID), "Basket items is presented"

    def should_be_message_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY), "Basket message is not presented"
    
    def should_be_message_basket_empty_invalid(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_BASKET_EMPTY_INVALID), "Basket message is not presented" 
