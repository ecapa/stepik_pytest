import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Firefox()
    browser.implicitly_wait(5)
    yield browser
    browser.quit()


@pytest.mark.parametrize('url', ['895', '896', '897', '898', '899', '903', '904', '905'])
def test_guest_should_see_link(browser, url):
    link = f'https://stepik.org/lesson/236{url}/step/1'
    txt = 'Correct!'
    # открыть страницу
    browser.get(link)
    # найти поле ввода ответа и ввести вычисленное значение
    browser.find_element(By.CSS_SELECTOR, 'textarea').send_keys(math.log(int(time.time()) + 0.2))
    # нажать кнопку "Отправить"
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    # получить ответ сервера
    result = browser.find_element(By.CSS_SELECTOR, '.smart-hints__hint').text
    # сравнить полученный ответ с ожидаемым
    assert result == txt, f'message is not {txt}'
