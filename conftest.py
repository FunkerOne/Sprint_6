import pytest
from selenium import webdriver
from data import MAIN_URL

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(MAIN_URL)
    yield driver
    driver.quit()
