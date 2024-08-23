from pages.page_object_main import *
import allure


@allure.feature("Yandex logo")
@allure.story("Transfer to dzen with yandex logo click")
class TestMainPageYandex:
    def test_check_transfer_from_yandex_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step("Click yandex logo"):
            main_page.click_yandex_logo()

        with allure.step("Switch to the new dzen window"):
            main_page.switch_to_new_window()

        with allure.step("Wait for dzen page to load"):
            main_page.wait_for_url_to_contain('dzen.ru')

        with allure.step("Verify correct URL for dzen"):
            assert 'dzen.ru' in main_page.get_current_url()
