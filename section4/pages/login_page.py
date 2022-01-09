from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'No word "login" in current url'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.EMAIL_IMPUT_SIGN_IN), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_IN), 'No password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_IN_BTN), 'No submit button'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.EMAIL_INPUT_SIGN_UP), 'No email field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_INPUT_SIGN_UP), 'No password field'
        assert self.is_element_present(*LoginPageLocators.PASSWORD_CONFIRMED_INPUT), 'No confirmed password field'
        assert self.is_element_present(*LoginPageLocators.SIGN_UP_BTN), 'No submit button'
