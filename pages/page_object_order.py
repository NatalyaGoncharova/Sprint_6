from pages.page_base import BasePage
from locators import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def confirm_cookie(self):
        self.click(COOKIES)

    def open_order(self):
        self.click(ORDER_BUTTON_IN_CORNER)

    def fill_order_form(self, user_data):
        self.send_keys(NAME, user_data['name'])
        self.send_keys(SURNAME, user_data['surname'])
        self.send_keys(ADDRESS, user_data['address'])
        self.send_keys(METRO, user_data['metro'])
        self.driver.find_element(*METRO).send_keys(Keys.DOWN, Keys.ENTER)
        self.send_keys(TELEPHONE_NUMBER, user_data['telephone'])

        self.click(NEXT_BUTTON)
        self.click(TIME_DELIVERY)

        date_element = self.driver.find_element(By.XPATH, user_data['date_order'])
        date_element.click()

        self.click(RENT_PERIOD)
        self.click(user_data['order_period'])
        self.click(user_data['scooter_color'])
        self.send_keys(COMMENT_FOR_COURIER, user_data['comment'])

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

        return 'Заказ оформлен' in success_message
