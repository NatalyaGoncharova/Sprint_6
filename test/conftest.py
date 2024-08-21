import pytest
from selenium import webdriver

from data import *


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()
