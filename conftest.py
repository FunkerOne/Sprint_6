import pytest
from selenium import webdriver
#from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="function")
def driver():
    #options = Options()
    #options.add_argument('--width=1920')
    #options.add_argument('--height=1080')
    driver = webdriver.Firefox()
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
