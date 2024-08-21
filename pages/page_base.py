from selenium.common import NoSuchWindowException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)

    def wait_for_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def wait_for_visibility(self, locator):
        if isinstance(locator, tuple):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        else:
            WebDriverWait(self.driver, 10).until(EC.visibility_of(locator))

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_window(self):
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        new_window = self.driver.window_handles[-1]
        try:
            self.driver.switch_to.window(new_window)
        except NoSuchWindowException:
            print("Failed to switch to the new window.")
            WebDriverWait(self.driver, 5).until(lambda d: len(d.window_handles) > 1)
            self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url_to_contain(self, url_fragment):
        WebDriverWait(self.driver, 10).until(EC.url_contains(url_fragment))
