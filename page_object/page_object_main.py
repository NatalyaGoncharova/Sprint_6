from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def confirm_cookie(self):
        cookie_button = self.driver.find_element(*COOKIES)
        cookie_button.click()

    def open_question(self, index):
        questions = self.driver.find_elements(*QUESTION)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", questions[index])
        WebDriverWait(self.driver, 2).until(EC.visibility_of(questions[index]))
        WebDriverWait(self.driver, 2).until(EC.element_to_be_clickable(questions[index]))
        questions[index].click()

    def get_answer(self, index):
        answers = self.driver.find_elements(*ANSWER)
        WebDriverWait(self.driver, 2).until(EC.visibility_of(answers[index]))
        if answers and len(answers) > index:
            return answers[index].text
        else:
            return None
    def click_order_button_top(self):
        order_button_top = (self.driver.find_element(*ORDER_BUTTON_IN_CORNER))
        order_button_top.click()

    def click_order_button_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        order_button_bottom = (self.driver.find_element(*ORDER_BUTTON_IN_BOTTOM))
        order_button_bottom.click()

    def click_scooter_logo(self):
        scooter_button = (self.driver.find_element(*SCOOTER_BUTTON))
        scooter_button.click()

    def click_yandex_logo(self):
        yandex_button = (self.driver.find_element(*YANDEX_BUTTON))
        yandex_button.click()
