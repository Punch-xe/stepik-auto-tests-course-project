from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_text_that_basket_is_empty(self):
        empty_basket_text = self.browser.find_element_by_css_selector("#content_inner>p").text
        assert len(empty_basket_text) > 0, "no empty basket text"
        assert self.is_element_present(*BasketPageLocators.CONTINUE_SHOPPING_HREF), "no continue shopping href"
        return True

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.FIRST_PRODUCT_IN_BASKET), "product in basket is present"
        return True
