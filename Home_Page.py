import data
from helperClasses.Actions import Actions
from selenium.webdriver.common.by import By


class HomePage:
    actions = Actions

    # Elements into the HomePage
    home_page_title = (By.CSS_SELECTOR, "div[class='text-vertical-center'] h1")
    home_page_subtitle = (By.CSS_SELECTOR, "div[class='text-vertical-center'] h3")
    make_appointment_button = (By.ID, 'btn-make-appointment')

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)

# Click on make appointment button
    def click_make_appointment_button(self):
        self.actions.click(self.make_appointment_button)

# Check the text title of the page
    def title_home_page_check(self):
        self.actions.assert_text_in_text(data.home_page_title_text, self.actions.get_text(self.home_page_title))

# Check the text title of the page
    def subtitle_home_page_check(self):
        self.actions.assert_text_in_text(data.home_page_subtitle_text, self.actions.get_text(self.home_page_subtitle))

# Check the text of make appointment button
    def make_appointment_button_check(self):
        self.actions.assert_text_in_text(data.make_appointment_button_text,self.actions.get_text(self.make_appointment_button))

# Click the make appointment button the first time - to go to login page
    def click_make_appointment_first_time(self):
        from Login_Page import LoginPage
        login_page = LoginPage(self.driver)
        self.click_make_appointment_button()
        self.actions.assert_text_in_text(data.login_text, self.actions.get_text(login_page.login_title))

# Click the make appointment button - to go to make an appointment page
    def click_make_appointment_to_the_form(self):
        from Login_Page import LoginPage
        login_page = LoginPage(self.driver)

        self.actions.assert_text_in_text(data.make_appointment_button_text, self.actions.get_text(self.make_appointment_button))
        self.actions.click(self.make_appointment_button)
        self.actions.assert_text_in_text(data.login_text, self.actions.get_text(login_page.login_title))

