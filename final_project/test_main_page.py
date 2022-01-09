from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import PageObject
import pytest



@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        page_login = LoginPage(browser, browser.current_url)
        page_login.open()
        page_login.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page_main = MainPage(browser, link)
    page_main.open()
    page_main.should_be_basket_button()
    page_main.go_to_basket()
    page_basket = BasketPage(browser, browser.current_url)
    page_basket.should_be_an_empty_basket()
    page_basket.should_be_the_text_basket_is_empty()
