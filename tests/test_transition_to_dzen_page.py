from pages.home_page import HomePage
from conftest import driver
import allure

class TestTransitionToDzenPage:
    @allure.title('Переход в dzen.ru, по клику на логотип Яндекс')
    def test_jump_after_click_yandex_logo_in_header(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        home_page.jump_after_click_to_yandex_logo()
        home_page.switch_window()
        home_page.find_dzen_logo()
        assert "https://dzen.ru/" in home_page.current_url()
