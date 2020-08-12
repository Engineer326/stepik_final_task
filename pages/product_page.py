from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON), 'No add to basket button'
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_add_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_ADDED_MESSAGE), 'There is no message about adding'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'There is no product name'
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message = self.browser.find_element(*ProductPageLocators.BASKET_ADDED_MESSAGE).text
        assert product_name in message, 'Product name is not in the message'

    def should_be_basket_total(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL), 'There is no basket total price'
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), 'There is no product price'
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        total_price = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL).text
        assert product_price in total_price, 'Total price doesnt match the product price'
