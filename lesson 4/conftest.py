import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# CHROME
# options = Options()
# options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
# browser = webdriver.Chrome(options=options)
# FIREFOX
# fp = webdriver.FirefoxProfile()
# fp.set_preference("intl.accept_languages", user_language)
# browser = webdriver.Firefox(firefox_profile=fp)

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture
def browser(request):
	options = Options()
	options.add_experimental_option('prefs', {'intl.accept_languages': request.config.getoption('--language')})
	browser = webdriver.Chrome(options=options)
	return browser
