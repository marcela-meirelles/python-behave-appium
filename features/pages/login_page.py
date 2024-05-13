class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        # replace 'username_locator' with the actual locator
        self.driver.find_element_by_id('username_locator').send_keys(username)

    def enter_password(self, password):
        # replace 'password_locator' with the actual locator
        self.driver.find_element_by_id('password_locator').send_keys(password)

    def press_login_button(self):
        # replace 'login_button_locator' with the actual locator
        self.driver.find_element_by_id('login_button_locator').click()

    def get_error_message(self):
        # replace 'error_message_locator' with the actual locator
        return self.driver.find_element_by_id('error_message_locator').text