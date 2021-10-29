from selenium.webdriver.common.by import By


def test_add_to_basket(browser):
	browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
	browser.find_element(By.CSS_SELECTOR, 'form#add_to_basket_form [type="submit"]')
