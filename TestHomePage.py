import data
from selenium import webdriver
from Home_Page import HomePage


class TestHomePage:
    driver = None
    home_page = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.home_page = HomePage(cls.driver)
        cls.driver.get(data.url)

    def test_open_make_appointment_page(self):
        home_page = self.home_page
        home_page.title_home_page_check()
        home_page.subtitle_home_page_check()
        home_page.make_appointment_button_check()

    def test_click_make_appointment_first_time(self):
        home_page = self.home_page
        home_page.click_make_appointment_first_time()

    def test_open_make_appointment_form(self):
        home_page = self.home_page
        home_page.click_make_appointment_first_time()
