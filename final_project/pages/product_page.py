from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageObject(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), "add to basket button not found"

    def should_be_a_message(self):
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        product_has_been_added_to_basket = WebDriverWait(self.browser, 5).until(EC.presence_of_element_located(ProductPageLocators.SUCCESS_MESSAGE))
        assert product_title == product_has_been_added_to_basket.text, "No message that the product has been added to basket"

    def is_product_in_basket(self):
        basket_cost_message = self.browser.find_element(*ProductPageLocators.BASKET_COST_MESSAGE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == basket_cost_message, "The cost of the basket is not the same as the price of the product."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Element is present on the page but should disappear"
