import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='firefox',
                     help="Choose browser: edge or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser = None
    if browser_name == "edge":
        print("\nstart edge browser for test..")
        browser = webdriver.Edge()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be edge or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
