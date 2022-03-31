from selenium import webdriver
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    print("\nrun test...")
    browser.get(link)
    time.sleep(3)
    try:
        button = browser.find_element_by_css_selector('button[type="submit"].btn.btn-lg.btn-primary.btn-add-to-basket')
    except:
        print("\nbutton not found...")
        button = None
    assert button is not None, "assert is None"