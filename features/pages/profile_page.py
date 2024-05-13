class ProfilePage:
    def __init__(self, driver):
        self.driver = driver

    def enter_details(self, username, email):
        # replace 'username_locator' and 'email_locator' with the actual locators
        self.driver.find_element_by_id('username_locator').send_keys(username)
        self.driver.find_element_by_id('email_locator').send_keys(email)

    def press_save_button(self):
        # replace 'save_button_locator' with the actual locator
        self.driver.find_element_by_id('save_button_locator').click()

    def get_success_message(self):
        # replace 'success_message_locator' with the actual locator
        return self.driver.find_element_by_id('success_message_locator').text

    def get_error_message(self):
        # replace 'error_message_locator' with the actual locator
        return self.driver.find_element_by_id('error_message_locator').text