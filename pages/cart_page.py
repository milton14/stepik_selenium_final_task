from selenium.webdriver.common.by import By
from .locators import BasePageLocators
from .base_page import BasePage

class CartPage(BasePage):
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*CartPageLocators.GOODS_NAME), \
       "Success message is presented, but should not be"

    def should_basket_is_empty(self):
        assert self.browser.find_element(*CartPageLocators.BASKET_EMPTY_LABEL).text.find("Your basket is empty") >= 0, "Label 'Your basket is empty' doesn't exist"


class CartPageLocators(object):
    GOODS_NAME = (By.CSS_SELECTOR, ".alert-success div.alertinner strong")
    GOODS_PRICE = (By.CSS_SELECTOR, ".alert-info div.alertinner strong")
    BASKET_EMPTY_LABEL = (By.ID, "content_inner")