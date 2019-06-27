from selenium.webdriver.common.by import By

class MainPageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class LoginPageLocators(object):
    LOGIN_FORM = (By.ID, "login_form")    
    REGISTRATION_FORM = (By.ID, "registration_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD = (By.ID, "id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD = (By.ID, "id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form button")

class CartPageLocators(object):
    GOODS_NAME = (By.CSS_SELECTOR, ".alert-success div.alertinner strong")
    GOODS_PRICE = (By.CSS_SELECTOR, ".alert-info div.alertinner strong")
    BASKET_EMPTY_LABEL = (By.ID, "content_inner")

class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    GOODS_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    GOODS_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")