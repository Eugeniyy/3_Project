#test_main_page.py - тестируем главную страницу

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
import pytest

@pytest.mark.login_guest
class TestLOginFromMainPage():
        
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        self.page = MainPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.should_be_login_link()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        self.page = BasketPage(browser, link)
        self.page.open()
        self.page.go_to_basket()
        self.page.should_be_basket_empty()
        self.page.should_be_message_basket_empty()
        
#Пустая строка!