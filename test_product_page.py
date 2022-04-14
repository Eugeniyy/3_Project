#test_product_page.py - тестируем страницу с продуктом

from pages.product_page import ProductPage
import pytest
import time

@pytest.mark.parametrize("param", [*range(7), pytest.param(7, marks=pytest.mark.xfail), *range(7+1, 10)])
def test_guest_can_add_product_to_basket(browser, param):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
    page = ProductPage(browser, link)
    page.open()
    page.get_product_info()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.check_product()
    page.check_price_product()

def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_dissapear_success_message()

