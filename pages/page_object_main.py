from locators import *
from pages.page_base import BasePage

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def open_question(self, index):
        questions = self.find_elements(QUESTION)
        self.scroll_to_element(questions[index])
        self.wait_for_visibility(questions[index])
        self.click(questions[index])

    def get_answer(self, index):
        answers = self.find_elements(ANSWER)
        self.wait_for_visibility(answers[index])
        if answers and len(answers) > index:
            return answers[index].text
        return None

    def click_order_button_top(self):
        self.click(ORDER_BUTTON_IN_CORNER)

    def click_order_button_bottom(self):
        order_button = self.find_element(ORDER_BUTTON_IN_BOTTOM)
        self.scroll_to_element(order_button)
        self.click(ORDER_BUTTON_IN_BOTTOM)

    def click_scooter_logo(self):
        self.click(SCOOTER_BUTTON)

    def click_yandex_logo(self):
        self.click(YANDEX_BUTTON)
