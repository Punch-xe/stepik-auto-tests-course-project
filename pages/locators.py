from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")


class ProductPageLocators():
    ADD_TO_CART_LINK = (By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div:nth-child(1).alert.alert-safe.alert-noicon.alert-success>div")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-group")


class BasketPageLocators():
    CONTINUE_SHOPPING_HREF = (By.CSS_SELECTOR, "#content_inner>p>a")
    FIRST_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items>div")
