from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from selenium.webdriver.common.keys import Keys
from test.data import *
class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    def confirm_cookie(self):
        cookie_button = self.driver.find_element(*COOKIES)
        cookie_button.click()

    def open_order(self, index):
        order_button = self.driver.find_element(*ORDER_BUTTON_IN_CORNER)
        order_button.click()

    def fill_order_form(self, user_data):
        self.driver.find_element(*NAME).send_keys(user_data['name'])
        self.driver.find_element(*SURNAME).send_keys(user_data['surname'])
        self.driver.find_element(*ADDRESS).send_keys(user_data['address'])
        self.driver.find_element(*METRO).send_keys(user_data['metro'],Keys.DOWN, Keys.ENTER)
        self.driver.find_element(*TELEPHONE_NUMBER).send_keys(user_data['telephone'])

        # Переход к следующему шагу
        self.driver.find_element(*NEXT_BUTTON).click()

        self.driver.find_element(*TIME_DELIVERY).click()

        # Выбор даты доставки и ввод комментария
        date_element = self.driver.find_element(By.XPATH, user_data['date_order'])
        date_element.click()
        self.driver.find_element(*RENT_PERIOD).click()
       # WebDriverWait(self.driver, 5).until(EC.url_to_be(BASE_URL_ORDER))
        self.driver.find_element(*user_data['order_period']).click()
        self.driver.find_element(*user_data['scooter_color']).click()
        self.driver.find_element(*COMMENT_FOR_COURIER).send_keys(user_data['comment'])

        # Завершение заказа
        finish_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(ORDER_BUTTON_FINISH)
        )
        finish_button.click()

        apply_button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(APPLY_ORDER_BUTTON)
        )
        apply_button.click()

    def check_order_success(self):
        success_message = self.driver.find_element(*SUCCESS_MESSAGE).text

        end_button = WebDriverWait(self.driver, 2).until(
            EC.element_to_be_clickable(END_ORDER_BUTTON)
        )
        end_button.click()
        #print(success_message)
        if 'Заказ оформлен' in success_message:
            return True
        else:
            return False
        #return success_message == 'Заказ оформлен'

