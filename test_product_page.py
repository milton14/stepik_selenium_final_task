from .pages.product_page import ProductPage
from .pages.cart_page import CartPage
from .pages.login_page import LoginPage
from .pages.base_page import BasePage
from .pages.locators import ProductPageLocators, CartPageLocators
import time, pytest, uuid

#task 4.3.6
'''
def test_guest_cant_see_success_message_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_not_element_present("Confirm message is presented", *CartPageLocators.GOODS_NAME)

def test_message_dissapeared_after_adding_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_is_disappeared("Confirm message isn't disappeared", *CartPageLocators.GOODS_NAME)
'''

#task 4.3.7
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

#step 4.3.10
@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = CartPage(browser, link)
    page.open()
    basket_link = page.browser.find_element(*ProductPageLocators.BASKET_LINK)
    basket_link.click()
    page.should_not_be_success_message()
    page.should_basket_is_empty()   

@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):    
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_goods_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3)
    page.should_be_confirming_order_message()
    page.check_goods_names_are_equal()
    page.check_goods_prices_are_equal()


def get_uuid():
    return str(uuid.uuid4()).replace("-","") 

@pytest.mark.registration
class TestUserAddToCartFromProductPage(object):
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_not_element_present("Confirm message is presented", *CartPageLocators.GOODS_NAME)

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):    
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_goods_to_basket()
        page.solve_quiz_and_get_code()
        time.sleep(3)
        page.should_be_confirming_order_message()
        page.check_goods_names_are_equal()
        page.check_goods_prices_are_equal()

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = "{}@fakemail.com".format(get_uuid())
        pwd = get_uuid()
        url = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        login_page = LoginPage(browser, url)
        login_page.open()
        login_page.register_new_user(email, pwd)
        login_page.should_be_authorized_user()
