from selenium.webdriver.common.by import By


class OrderPageLocators:
    order_button_in_header = (By.XPATH, ".//button[@class='Button_Button__ra12g']")
    order_button = (By.XPATH, ".//button[@class='Button_Button__ra12g Button_Middle__1CSJM']")
    first_name_field = (By.XPATH, "//input[@placeholder='* Имя']")
    last_name_field = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_field = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    subway_station_field = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_number_field = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, ".//button[text()='Далее']")
    when_delivery_order = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    time_rent = (By.XPATH, ".//span[@class='Dropdown-arrow']")
    today_time_rent = (By.XPATH, ".//div[text()='трое суток']")
    color_scooter_checkbox = (By.ID, "black")
    comment_field = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']")
    complete_order_button = (By.XPATH, ".//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']")
    order_info = (By.XPATH, ".//div[text()='Заказ оформлен']")
