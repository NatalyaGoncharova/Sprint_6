import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data import *

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    WebDriverWait(driver, 10).until(
        EC.url_to_be(BASE_URL)
    )
    yield driver
    driver.quit()