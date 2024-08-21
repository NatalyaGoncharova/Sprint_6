from pages.page_object_main import *
from pages.page_object_order import *
import allure
from data import *


@allure.feature("Order Flow")
@allure.story("Order scooter from the bottom")
@allure.title("Test order flow using the button in the bottom")
class TestMainPage:
    def test_order_flow_button_in_bottom(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data_2 = USER_DATA['user_2']

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step("Clicking on the order button in the bottom"):
            main_page.click_order_button_bottom()

        with allure.step("Filling out the order form"):
            order_page.fill_order_form(order_data_2)

        with allure.step("Verifying that the order was successful"):
            assert order_page.check_order_success()
