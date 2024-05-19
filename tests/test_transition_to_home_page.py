from pages.order_page import OrderPage
from pages.home_page import HomePage
from conftest import driver
import allure


class TestTransitionToHomePage:
    @allure.title('Переход на домашнюю страницу, через логотип Самокат (из формы оформления заказа в хедере)')
    def test_jump_after_click_to_scooter_logo_in_header(self, driver):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        order_button = OrderPage(driver)
        order_button.order_from_header()
        home_page.jump_after_click_to_scooter_logo()
        url = home_page.current_url()
        assert url == "https://qa-scooter.praktikum-services.ru/"
