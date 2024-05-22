from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import allure


class OrderPage(BasePage):
    @allure.step('Открытие формы заказа, через кнопку "Заказать" в хедере')
    def order_from_header(self):
        self.find_element_located_click(OrderPageLocators.order_button_in_header)

    @allure.step('Открытие формы заказа, через кнопку "Заказать" на домашней странице')
    def order_from_home_page(self):
        self.find_element_located_click(OrderPageLocators.order_button)

    @allure.step('Оформление заказа по наборам тестовых данных на первой форме')
    def order_scooter_first_form(self, first_name, last_name, address, subway_station, phone_number):
        self.find_element_located_click(OrderPageLocators.order_button_in_header)
        self.find_element_located(OrderPageLocators.first_name_field).send_keys(first_name)
        self.find_element_located(OrderPageLocators.last_name_field).send_keys(last_name)
        self.find_element_located(OrderPageLocators.address_field).send_keys(address)
        self.find_element_located_click(OrderPageLocators.subway_station_field)
        self.find_element_located(OrderPageLocators.subway_station_field).send_keys(subway_station)
        self.find_element_located(OrderPageLocators.subway_station_field).send_keys(Keys.ARROW_UP)
        self.find_element_located(OrderPageLocators.subway_station_field).send_keys(Keys.ENTER)
        self.find_element_located(OrderPageLocators.phone_number_field).send_keys(phone_number)
        self.find_element_located_click(OrderPageLocators.next_button)

    @allure.step('Оформление заказа по наборам тестовых данных на второй форме')
    def order_scooter_second_form(self, date, comment):
        self.find_element_located(OrderPageLocators.when_delivery_order).send_keys(date)
        self.find_element_located_click(OrderPageLocators.time_rent)
        self.find_element_located_click(OrderPageLocators.today_time_rent)
        self.find_element_located_click(OrderPageLocators.color_scooter_checkbox)
        self.find_element_located(OrderPageLocators.comment_field).send_keys(comment)
        self.find_element_located_click(OrderPageLocators.order_button)
        self.find_element_located_click(OrderPageLocators.complete_order_button)
        order_complete = self.find_element_located(OrderPageLocators.order_info)
        return order_complete.text
