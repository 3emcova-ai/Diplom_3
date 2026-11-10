import pytest
from selenium import webdriver
from data import Urls

@pytest.fixture(scope='function', params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
    elif request.param == 'chrome':
        driver = webdriver.Chrome()
    driver.get(Urls.STELLAR_BURGERS_URL)
    yield driver
    driver.quit()
