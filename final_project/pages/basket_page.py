from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
	def should_be_an_empty_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "there is a product in the basket"

	def should_be_the_text_basket_is_empty(self):
		assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE), "Your basket is not empty"
