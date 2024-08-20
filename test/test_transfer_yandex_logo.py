from page_object.page_object_main import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class TestMainPage:

    @allure.feature("Yandex logo")
    @allure.story("Transfer to dzen with yandex logo click")
    @allure.title("Test transfer to dzen using yandex logo click")
    def test_check_transfer_from_yandex_logo(self, driver):
        main_page = MainPage(driver)

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step("Click yandex logo"):
            main_page.click_yandex_logo()

        with allure.step("Switch window on dzen"):
            driver.switch_to.window(driver.window_handles[-1])

        with allure.step("Wait loading dzen"):
            WebDriverWait(driver, 7).until(EC.url_to_be('https://dzen.ru/?yredirect=true'))

        with allure.step("Verify right switch to dzen"):
            assert 'dzen.ru' in driver.current_url