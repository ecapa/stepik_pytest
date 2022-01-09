# Final Project
 Финальное задание по курсу "Автоматизация тестирования с помощью Selenium и Python"

*Внимание! Если при выполнении тестов Вы получаете следующую ошибку:*

`test_main_page.py:1: in <module>\
    from .pages.main_page import MainPage\
E   ImportError: attempted relative import with no known parent package`

*измените импорты. Вместо текущих*

**test_main_page.py**

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.product_page import PageObject

**test_product_page.py**

from .pages.locators import ProductPageLocators
from .pages.product_page import PageObject
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage

*Исправьте на следующее*

**test_main_page.py**

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.product_page import PageObject

**test_product_page.py**

from pages.locators import ProductPageLocators
from pages.product_page import PageObject
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
