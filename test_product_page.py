#test_product_page.py - тестируем страницу с продуктом

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
import pytest
import faker
import time

@pytest.mark.test_product_guest
class TestLoginFromProductPage():
    @pytest.mark.parametrize("param", [*range(7), pytest.param(7, marks=pytest.mark.xfail), *range(7+1, 10)])
    def test_guest_can_add_product_to_basket(self, browser, param):
        link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{param}"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.get_product_info()
        self.page.add_product_to_basket()
        self.page.solve_quiz_and_get_code()
        self.page.check_product()
        self.page.check_price_product()

    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_be_login_link()

    def test_guest_can_go_to_login_page__from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.go_to_login_page()

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_product_to_basket()
        self.page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.should_not_be_success_message()

    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ProductPage(browser, link)
        self.page.open()
        self.page.add_product_to_basket()
        self.page.should_dissapear_success_message()

    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, browser):
        link = "https://selenium1py.pythonanywhere.com/"
        self.page = BasketPage(browser, link)
        self.page.open()
        self.page.go_to_basket()
        self.page.should_be_basket_empty()
        self.page.should_be_message_basket_empty()

@pytest.mark.test_product_user
class TestUserAddToBasketFromProductPage():

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.browser = browser
        login = LoginPage(self.browser, link)
        login.open()
        login.go_to_login_page()
        f = faker.Faker()
        email = f.email()
        password = "123asddsa321"
        login.register_new_user(email, password)
        login.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ProductPage(self.browser, link)
        self.page.open()
        self.page.get_product_info()
        self.page.add_product_to_basket()
        self.page.check_product()
        self.page.check_price_product()

    def test_user_cant_see_success_message(self):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        self.page = ProductPage(self.browser, link)
        self.page.open()
        self.page.should_not_be_success_message()
