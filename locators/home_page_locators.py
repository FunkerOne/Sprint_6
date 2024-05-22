from selenium.webdriver.common.by import By


class HomePageLocators:
    yandex_logo = (By.XPATH, ".//a[@class='Header_LogoYandex__3TSOI']")
    dzen_page = (By.ID, "__SVG_SPRITE_NODE__")
    scooter_logo = (By.XPATH, ".//a[@class='Header_LogoScooter__3lsAR']")
    cookie_button = (By.ID, 'rcc-confirm-button')
    first_question_button = (By.ID, "accordion__heading-0")
    first_question_text = (By.ID, "accordion__panel-0")
    second_question_button = (By.ID, "accordion__heading-1")
    second_question_text = (By.ID, "accordion__panel-1")
    third_question_button = (By.ID, "accordion__heading-2")
    third_question_text = (By.ID, "accordion__panel-2")
    fourth_question_button = (By.ID, "accordion__heading-3")
    fourth_question_text = (By.ID, "accordion__panel-3")
    fifth_question_button = (By.ID, "accordion__heading-4")
    fifth_question_text = (By.ID, "accordion__panel-4")
    sixth_question_button = (By.ID, "accordion__heading-5")
    sixth_question_text = (By.ID, "accordion__panel-5")
    seventh_question_button = (By.ID, "accordion__heading-6")
    seventh_question_text = (By.ID, "accordion__panel-6")
    eighth_question_button = (By.ID, "accordion__heading-7")
    eighth_question_text = (By.ID, "accordion__panel-7")
