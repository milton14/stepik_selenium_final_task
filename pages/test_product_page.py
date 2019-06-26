from .product_page import ProductPage
import time

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