import pytest
from selenium import webdriver

def pytest_addoption(parser):
	parser.addoption('--language', action='store', default='en-gb',
                     help="Choose the language. Examples: ru, de, es, fr, etc... English (en-gb) is default")

@pytest.fixture(scope="function")
def browser():
	print("\nstart Chrome...")
	browser = webdriver.Chrome()
	yield browser
	print("\nquit Chrome..")
	browser.quit()

@pytest.fixture(scope="function")
def language(request):
	language = request.config.getoption("language")
	return language