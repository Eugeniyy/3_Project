#login_page.py - модуль со страницей логина

from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"login is not present in {self.browser.current_url}"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not present"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL)
        email_field.send_keys(str(email))

        password1_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD1)
        password1_field.send_keys(str(password))

        password2_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD2)
        password2_field.send_keys(str(password))

        button =  self.browser.find_element(*LoginPageLocators.REGISTRATION_BUTTON)
        button.click()