from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "http://selenium1py.pythonanywhere.com/ru/accounts/login/".find("loginn"), "The page doesn't contain login word"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form doesn't exist"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form doesn't exist"

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")    
    REGISTRATION_FORM = (By.ID, "registration_form")    