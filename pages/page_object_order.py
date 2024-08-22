from pages.page_base import BasePage
from locators import *
from selenium.webdriver.common.keys import Keys


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_order(self):
        self.click(ORDER_BUTTON_IN_CORNER)

    def fill_order_form(self, user_data):
        self.send_keys(NAME, user_data['name'])
        self.send_keys(SURNAME, user_data['surname'])
        self.send_keys(ADDRESS, user_data['address'])
        self.send_keys(METRO, user_data['metro'])
        self.find_element(METRO).send_keys(Keys.DOWN, Keys.ENTER)
        self.send_keys(TELEPHONE_NUMBER, user_data['telephone'])

        self.click(NEXT_BUTTON)
        self.click(TIME_DELIVERY)

        date_element = self.find_element((By.XPATH, user_data['date_order']))
        date_element.click()

        self.click(RENT_PERIOD)
        self.click(user_data['order_period'])
        self.click(user_data['scooter_color'])
        self.send_keys(COMMENT_FOR_COURIER, user_data['comment'])
        self.click(ORDER_BUTTON_FINISH)
        self.click(APPLY_ORDER_BUTTON)

    def check_order_success(self):
        success_message = self.find_element(SUCCESS_MESSAGE).text
        self.click(END_ORDER_BUTTON)

        return 'Заказ оформлен' in success_message
