class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def click_none_of_the_above(self):
        self.driver.find_element_by_id('com.google.android.gms:id/button_area').click()

    def enter_phone_number(self, phone_number):
        # replace 'phone_number_locator' with the actual locator
        self.driver.find_element_by_id('com.hdw.james.rider:id/input').send_keys(phone_number)
        self.driver.find_element_by_id('com.hdw.james.rider:id/continueButton').click() 

    def enter_verification_code(self, code):
        self.driver.find_element_by_id('com.hdw.james.rider:id/continueButton').click() 
        self.driver.find_element_by_xpath('(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[1]').send_keys(code)
        # xpath locator for James code: (//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[1]   
        # 	(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[2]
        # 	(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[3]
        # 	(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[4]
        # 	(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[5]
        # 	(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[6]

    def enter_full_name(self, first_name, last_name):
        self.driver.find_element_by_id('com.hdw.james.rider:id/firstNameInput').send_keys(first_name)
        self.driver.find_element_by_id('com.hdw.james.rider:id/lastNameInput').send_keys(last_name)
        self.driver.find_element_by_id('com.hdw.james.rider:id/buttonContinue').click()

    def review_splash_and_continue(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/splash_title').is_displayed()
        self.driver.find_element_by_id('com.hdw.james.rider:id/splash_continue_button').click() 

    def accept_location_permission(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/askPermissionTitle').is_displayed()
        self.driver.find_element_by_id('com.hdw.james.rider:id/askPermissionAlertImage').click()
        # verify permission options are displayed
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_message').is_displayed()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').is_displayed()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_deny_button').is_displayed()
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_one_time_button').is_displayed()
        # select permission option
        self.driver.find_element_by_id('com.android.permissioncontroller:id/permission_allow_foreground_only_button').click()

    def skip_onboarding(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/SKIP_ONBOARDING').click()

    def home_screen_dashboard_is_displayed(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/dashboardTopBar').is_displayed()

    def enter_details(self, username, password, email):
        # replace 'username_locator', 'password_locator', and 'email_locator' with the actual locators
        self.driver.find_element_by_id('username_locator').send_keys(username)
        self.driver.find_element_by_id('password_locator').send_keys(password)
        self.driver.find_element_by_id('email_locator').send_keys(email)

    def press_register_button(self):
        # replace 'register_button_locator' with the actual locator
        self.driver.find_element_by_id('register_button_locator').click()

    def get_success_message(self):
        # replace 'success_message_locator' with the actual locator
        return self.driver.find_element_by_id('success_message_locator').text

    def get_error_message(self):
        # replace 'error_message_locator' with the actual locator
        return self.driver.find_element_by_id('error_message_locator').text