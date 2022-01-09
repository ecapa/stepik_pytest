from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner>p")


class BasePageLocators:
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_BUTTON = (By.CSS_SELECTOR, "span>a.btn-default")



class MainPageLocators:
    pass
    

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGSTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGSTRATION_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGSTRATION_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner>strong")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "div.product_main>h1")
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, "div.alertinner>p>strong")

