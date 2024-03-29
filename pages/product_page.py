from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators, CartPageLocators
import math

class ProductPage(BasePage):
    def add_goods_to_basket(self):
        btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        btn.click()

    def should_be_confirming_order_message(self):
        assert (self.is_element_present(*CartPageLocators.GOODS_NAME)
        and self.is_element_present(*CartPageLocators.GOODS_PRICE)
        ), "Confirming order message doesn't exist"

    def check_goods_names_are_equal(self):
        goods_name = self.browser.find_element(*ProductPageLocators.GOODS_NAME).text
        goods_name_in_basket = self.browser.find_element(
            *CartPageLocators.GOODS_NAME).text
        assert (goods_name == goods_name_in_basket), "Goods names aren't equal {}!={}".format(
        goods_name, goods_name_in_basket)

    def check_goods_prices_are_equal(self):
        goods_price = self.browser.find_element(*ProductPageLocators.GOODS_PRICE).text
        goods_price_in_basket = self.browser.find_element(
            *CartPageLocators.GOODS_PRICE).text
        assert (goods_price == goods_price_in_basket), "Goods names aren't equal {}!={}".format(
        goods_price, goods_price_in_basket)

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            print("Your code: {}".format(alert.text))
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
