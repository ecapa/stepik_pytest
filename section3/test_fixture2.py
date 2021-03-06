import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def fix_browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, fix_browser):
        fix_browser.get(link)
        fix_browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, fix_browser):
        fix_browser.get(link)
        fix_browser.find_element_by_css_selector(".basket-mini .btn-group > a")
