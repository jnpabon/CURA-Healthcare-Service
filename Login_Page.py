import data
from Home_Page import HomePage
from helperClasses.Actions import Actions
from selenium.webdriver.common.by import By


class LoginPage:
    actions = Actions
    home_page = HomePage

    # Elements into the HomePage
    login_title = (By.CSS_SELECTOR, "div[class='col-sm-12 text-center'] h2")
    username_input = (By.ID, 'txt-username')
    password_input = (By.ID, 'txt-password')
    login_button = (By.ID, 'btn-login')
    warning_message_login_selector = (By.CSS_SELECTOR, ".lead.text-danger")
    

    def __init__(self, driver):
        self.driver = driver
        self.actions = Actions(driver)
        self.home_page = HomePage(driver)

# Set the input
    def set_username_input(self, username):
        # Type the username into username input
        self.actions.set_input_text(self.username_input, username)

# Click on login button
    def click_login_button(self):
        self.actions.click(self.login_button)

# Check the text title of the page
    def title_login_page_check(self):
        from MakeAppointmentPage import MakeAppointmentPage
        make_appointment = MakeAppointmentPage(self.driver)
        self.actions.assert_text_in_text(data.home_page_title_text, self.actions.get_text(make_appointment.make_appointment_page_title))

# Check the first time click on the make appointment button - to go to login page
    def click_make_appointment_first_time(self):
        self.home_page.click_make_appointment_button()
        self.actions.assert_text_in_text(data.login_text, self.actions.get_text(self.login_title))

# login success
    def login_success(self):
        # Click on a Make Appointment Button
        self.home_page.click_make_appointment_button()
        # Type the username into username input
        self.actions.set_input_text(self.username_input, data.username)
        # Check the username typed into the username input
        self.actions.assert_text_in_text(self.actions.get_property_text(self.username_input,'value'), data.username)
        # Type the username into password input
        self.actions.set_input_text(self.password_input, data.password)
        # Check the password typed into the password input
        self.actions.assert_text_in_text(self.actions.get_property_text(self.password_input, 'value'), data.password)
        # Click on a Login Button
        self.click_login_button()

# login success
    def negative_login(self, username, password):
        # Click on a Make Appointment Button
        self.home_page.click_make_appointment_button()
        print(username)
        print(password)
        # Type the username into username input
        self.actions.set_input_text(self.username_input, username)
        # Check the username typed into the username input
        self.actions.assert_text_in_text( self.actions.get_property_text(self.username_input,'value'), username)
        # Type the username into password input
        self.actions.set_input_text(self.password_input, password)
        # Check the password typed into the password input
        self.actions.assert_text_in_text( self.actions.get_property_text(self.password_input, 'value'), password)
        # Click on a Login Button
        self.click_login_button()
        # Check the warning message by typed wrong username or password
        self.actions.assert_text_in_text(data.warning_message_wrong_username_or_password, self.actions.get_text(self.warning_message_login_selector))



