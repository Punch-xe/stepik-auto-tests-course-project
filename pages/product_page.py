from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_LINK)
        add_to_cart.click()

    def should_be_product_page(self):
        self.should_be_correct_url()
        self.should_be_add_to_cart_button()

    def should_be_correct_url(self):
        assert "/?promo=newYear" in self.browser.current_url, "Not a promo page"
        return True

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_LINK), "No 'add to cart' button"
        return True

    def should_be_success_message(self):
        product_name_text = self.browser.find_element_by_css_selector(".col-sm-6.product_main>h1").text
        first_part_of_success_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div:nth-child(1).alert.alert-safe.alert-noicon.alert-success>div>strong"))).text
        second_part_of_success_text = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, "div:nth-child(1).alert.alert-safe.alert-noicon.alert-success>div"))).text
        assert product_name_text == first_part_of_success_text, "incorrect product name in success message"
        assert " has been added to your basket." in second_part_of_success_text, \
            "incorrect success message"
        return True

    def should_be_correct_price_in_basket(self):
        price_in_basket_in_success_message = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR,
                "#messages .alert.alert-safe.alert-noicon.alert-info.fade.in>.alertinner >p>strong"))).text
        # commented out next check since the text in price_in_basket2 contains extra characters " "
        price_in_basket_in_header = WebDriverWait(self.browser, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR, ".basket-mini.pull-right.hidden-xs"))).text
        price = self.browser.find_element_by_css_selector("#content_inner .price_color").text
        assert price == price_in_basket_in_success_message, "incorrect price in basket in success message"
        assert price in price_in_basket_in_header, "incorrect price in basket in header"
        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        return True

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        return True
