from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
	def should_be_product_page(self):
		self.should_be_add_to_basket_btn()
		self.should_be_product_url()
		self.should_not_be_success_message()

	def add_to_basket(self):
		btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
		btn.click()
		self.solve_quiz_and_get_code()

	def should_be_add_to_basket_btn(self):
		assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN)

	def should_be_product_url(self):
		assert 'catalogue/' in self.browser.current_url, "This isn't product page"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
			"Success message is presented, but should not be"
