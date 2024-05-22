from locators.home_page_locators import HomePageLocators
from pages.base_page import BasePage
import allure


class HomePage(BasePage):
    @allure.step('Клик по логотипу Самокат')
    def jump_after_click_to_scooter_logo(self):
        self.find_element_located_click(HomePageLocators.scooter_logo)

    @allure.step('Клик по логотипу Яндекс')
    def jump_after_click_to_yandex_logo(self):
        self.find_element_located_click(HomePageLocators.yandex_logo)

    @allure.step('Клик по кнопке куки')
    def check_cookie(self):
        cookie = self.find_element_located(HomePageLocators.cookie_button)
        if cookie:
            cookie.click()
        else:
            pass

    @allure.step('Возвращаем значение ответа от требуемого вопроса')
    def home_page_questions(self, button, answer):
        search_field = self.find_element_located(button)
        self.execute_script(search_field)
        self.find_element_to_be_clickable(button)
        search_field.click()
        return self.find_element_located(answer).text

    @allure.step('Поиск логотипа "Дзен"')
    def find_dzen_logo(self):
        self.find_element_located(HomePageLocators.dzen_page)
