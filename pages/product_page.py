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
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
            *ProductPageLocators.FIRST_PART_OF_SUCCESS_TEXT).text, \
            "incorrect product name in success message"
        assert " has been added to your basket." in self.browser.find_element(
            *ProductPageLocators.SECOND_PART_OF_SUCCESS_TEXT).text, "incorrect success message"
        return True

    def should_be_correct_price_in_basket(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET_IN_SUCCESS_MESSAGE).text, \
            "incorrect price in basket in success message"
        assert self.browser.find_element(*ProductPageLocators.PRICE).text in self.browser.find_element(
            *ProductPageLocators.PRICE_IN_BASKET_IN_HEADER).text, "incorrect price in basket in header"
        return True

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        return True

    def should_success_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
        return True
