#test_main_page.py - Тестируем главную страницу

from pages.main_page import MainPage

def test_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_link()
#Пустая строка!