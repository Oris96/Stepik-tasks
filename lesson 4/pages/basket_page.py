from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
	def should_be_basket_page(self):
		self.should_be_login_url()

	def should_be_login_url(self):
		assert 'basket' in self.browser.current_url, "This isn't basket"

	def basket_is_empty(self):
		assert 'empty' in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET).text
