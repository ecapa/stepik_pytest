import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose a language: en, ru ... etc!")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    browser = webdriver.Chrome(options=options)
    '''
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", language)
    browser = webdriver.Firefox(firefox_profile=fp)
    '''
    print(f"\nstart browser for test..")
    yield browser
    # time.sleep(30)
    print("\nquit browser..")
    browser.quit()
