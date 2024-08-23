from pages.page_object_main import *
from pages.page_object_order import *
import allure
from data import *


@allure.feature("Order Flow")
@allure.story("Order scooter from corner button")
class TestMainPageOrderTop:
    def test_order_flow_button_in_corner(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        order_data_1 = USER_DATA['user_1']

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step("Clicking on the order button in the top corner"):
            main_page.click_order_button_top()

        with allure.step("Filling out the order form"):
            order_page.fill_order_form(order_data_1)

        with allure.step("Verifying that the order was successful"):
            assert order_page.check_order_success()
