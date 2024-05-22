from pages.order_page import OrderPage
from pages.home_page import HomePage
from data import DataKitOne
from conftest import driver
import allure
import pytest


class TestOrderPageFromHeader:
    @allure.title("Оформление самоката через кнопку Заказать в хедере")
    @pytest.mark.parametrize("first_name, last_name, address, subway_station, phone_number, date, comment, expected_result",
                             [(DataKitOne.first_name, DataKitOne.last_name, DataKitOne.address, DataKitOne.subway_station,
                               DataKitOne.phone_number, DataKitOne.date, DataKitOne.comment, "Заказ оформлен")])
    def test_order_page_from_header(self, driver, first_name, last_name, address, subway_station, phone_number, date, comment,
                                   expected_result):
        page = OrderPage(driver)
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        page.order_from_header()
        page.order_scooter_first_form(first_name, last_name, address, subway_station, phone_number)
        order_from_header_button_complete = page.order_scooter_second_form(date, comment)
        assert expected_result in order_from_header_button_complete
