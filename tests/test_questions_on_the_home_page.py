from pages.home_page import HomePage
from locators.home_page_locators import HomePageLocators
from conftest import driver
import allure
import pytest


class TestHomeQuestions:
    @allure.title('Проверка списка вопросов и ответов на домашней странице')
    @pytest.mark.parametrize('button, answer, expected_result',
                             [(HomePageLocators.first_question_button, HomePageLocators.first_question_text,
                               'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
                              (HomePageLocators.second_question_button, HomePageLocators.second_question_text,
                               'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
                              (HomePageLocators.third_question_button, HomePageLocators.third_question_text,
                               'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
                              (HomePageLocators.fourth_question_button, HomePageLocators.fourth_question_text,
                               'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
                              (HomePageLocators.fifth_question_button, HomePageLocators.fifth_question_text,
                               'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
                              (HomePageLocators.sixth_question_button, HomePageLocators.sixth_question_text,
                               'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
                              (HomePageLocators.seventh_question_button, HomePageLocators.seventh_question_text,
                               'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
                              (HomePageLocators.eighth_question_button, HomePageLocators.eighth_question_text,
                               'Да, обязательно. Всем самокатов! И Москве, и Московской области.')])
    def test_questions(self, button, answer, expected_result, driver):
        home_page = HomePage(driver)
        home_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        get_answer = home_page.home_page_questions(button, answer)
        assert get_answer == expected_result
