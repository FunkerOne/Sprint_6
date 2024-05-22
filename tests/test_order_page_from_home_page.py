from pages.order_page import OrderPage
from pages.home_page import HomePage
from data import DataKitTwo
from conftest import driver
import allure
import pytest


class TestOrderPageFromHomePage:
    @allure.title("Оформление самоката через кнопку Заказать на домашней странице")
    @pytest.mark.parametrize("first_name, last_name, address, subway_station, phone_number, date, comment, expected_result",
                             [(DataKitTwo.first_name, DataKitTwo.last_name, DataKitTwo.address, DataKitTwo.subway_station,
                               DataKitTwo.phone_number, DataKitTwo.date, DataKitTwo.comment, "Заказ оформлен")])
    def test_order_page_from_home_page(self, driver, first_name, last_name, address, subway_station, phone_number, date, comment,
                                   expected_result):
        page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        home_page.check_cookie()
        page.order_from_home_page()
        page.order_scooter_first_form(first_name, last_name, address, subway_station, phone_number)
        order_from_home_page_button_complete = page.order_scooter_second_form(date, comment)
        assert expected_result in order_from_home_page_button_complete
