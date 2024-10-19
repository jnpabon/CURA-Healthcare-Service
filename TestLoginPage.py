import data
from selenium import webdriver
from Login_Page import LoginPage


class TestLoginPage:
    driver = None
    login_page = None

    @classmethod
    def setup_class(cls):
        options = webdriver.ChromeOptions()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(options=options)
        cls.login_page = LoginPage(cls.driver)
        cls.driver.get(data.url)

    def test_open_login_page(self):
        login_page = self.login_page
        login_page.click_make_appointment_first_time()

    def test_login_success(self):
        login_page = self.login_page
        login_page.login_success()

    def test_wrong_username(self):
        login_page = self.login_page
        login_page.negative_login(data.wrong_username, data.password)


    def test_wrong_password(self):
        login_page = self.login_page
        login_page.negative_login(data.username, data.wrong_password)