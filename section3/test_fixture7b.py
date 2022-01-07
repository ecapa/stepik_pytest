import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    user_language = 'ru, en-US'
    fp = webdriver.FirefoxProfile()
    fp.set_preference("intl.accept_languages", user_language)
    fp.update_preferences()
    browser = webdriver.Firefox(firefox_profile=fp)
    yield browser
    print("\nquit browser..")
    browser.quit()

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")