import data
from helperClasses import Actions
from selenium.webdriver.common.by import By


class MakeAppointmentPage:
    actions = Actions

    # Elements into the HomePage
    make_appointment_page_title = (By.CSS_SELECTOR, "div[class='col-sm-12 text-center'] h2")

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)