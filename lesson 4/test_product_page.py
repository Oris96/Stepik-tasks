import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.locators import ProductPageLocators


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
								  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
	page = ProductPage(browser, link)
	page.open()
	page.should_be_product_page()
	page.add_to_basket()
	assert \
		page.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == page.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_NAME).text and \
		page.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == page.browser.find_element(*ProductPageLocators.BASKET_PRODUCT_PRICE).text, \
		"Product's name or price are different"

@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
	page = ProductPage(browser, link)
	page.open()
	assert page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE)

@pytest.mark.go_to_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
	page = ProductPage(browser, link)
	page.open()
	page.go_to_basket_page()
	basket_page = BasketPage(browser, browser.current_url)
	basket_page.basket_is_empty()

@pytest.mark.login_page
def test_guest_should_see_login_link_on_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
	page = ProductPage(browser, link)
	page.open()
	page.should_be_login_link()

@pytest.mark.login_page
def test_guest_can_go_to_login_page_from_product_page(browser):
	link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
	page = ProductPage(browser, link)
	page.open()
	page.go_to_login_page()
	login_page = LoginPage(browser, browser.current_url)
	login_page.should_be_login_page()

@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(browser):
	link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
	page = ProductPage(browser, link)
	page.open()
	page.add_to_basket()
	assert page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE)
