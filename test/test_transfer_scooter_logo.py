from pages.page_object_main import *
from data import *
import allure


@allure.feature("Scooter logo")
@allure.story("Transfer to main page with scooter logo click")
class TestMainPageScooter:

    def test_check_transfer_from_scooter_logo_click(self, driver):
        main_page = MainPage(driver)

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step("Clicking on the order button in the top"):
            main_page.click_order_button_top()

        with allure.step("Click on the scooter logo"):
            main_page.click_scooter_logo()

        with allure.step("Verify right transfer to main page"):
            assert main_page.get_current_url() == BASE_URL
