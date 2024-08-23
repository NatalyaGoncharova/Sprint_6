from selenium.webdriver.common.by import By
from data import *

QUESTION = (By.CSS_SELECTOR, '.accordion__button')
ANSWER = (By.CSS_SELECTOR, '.accordion__panel')

COOKIES = (By.ID, 'rcc-confirm-button')

#поля в заказе
NAME = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
SURNAME = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
ADDRESS = (By.XPATH, '//input[contains(@placeholder, "Адрес: куда привезти заказ")]')
METRO = (By.XPATH, '//input[contains(@placeholder, "Станция метро")]')
TELEPHONE_NUMBER = (By.XPATH, '//input[contains(@placeholder, "Телефон: на него позвонит курьер")]')
TIME_DELIVERY = (By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]')
RENT_PERIOD = (By.CSS_SELECTOR, 'div.Dropdown-root')
RENT_PERIOD_1 = (By.XPATH, '//div[contains(text(), "сутки")]')
RENT_PERIOD_2 =(By.XPATH, '//div[contains(text(), "двое суток")]')
ORDER_CHECKBOX_BLACK = (By.XPATH, '//input[@type="checkbox" and @id ="black"]')
ORDER_CHECKBOX_GRAY = (By.XPATH, '//input[@type="checkbox" and @id ="grey"]')
COMMENT_FOR_COURIER = (By.XPATH, '//input[@placeholder = "Комментарий для курьера"]')

#кнопки заказать/далее при заказе
NEXT_BUTTON = (By.CSS_SELECTOR, 'button.Button_Button__ra12g.Button_Middle__1CSJM')
ORDER_BUTTON_IN_CORNER = (By.CSS_SELECTOR, '.Button_Button__ra12g')
ORDER_BUTTON_IN_BOTTOM = (By.CSS_SELECTOR, '.Button_Button__ra12g.Button_Middle__1CSJM')
ORDER_BUTTON_FINISH = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")
APPLY_ORDER_BUTTON = (By.XPATH, '//button[text()="Да"]')

SUCCESS_MESSAGE = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')
END_ORDER_BUTTON = (By.XPATH, '//button[text()="Посмотреть статус"]')

#логотипы
SCOOTER_BUTTON = (By.XPATH, '//img[@alt="Scooter"]')
YANDEX_BUTTON = (By.XPATH, '//img[@alt="Yandex"]')




