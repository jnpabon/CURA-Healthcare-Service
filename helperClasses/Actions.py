from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import WebDriverException


class Actions:

    def __init__(self, driver):
        self.driver = driver

    # Acctions
    def click(self, locator):
        self.driver.find_element(*locator).click()

    def set_input_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    def get_text(self, locator):
        return self.driver.find_element(*locator).text

    def get_property_text(self, locator, attribute):
        return self.driver.find_element(*locator).get_property(attribute)

    # Assertions
    @staticmethod
    def assert_text_in_text(text, in_text):
        assert text in in_text