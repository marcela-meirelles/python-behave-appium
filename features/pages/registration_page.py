from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import wait_until_element_visible
from selenium.webdriver.common.by import By
import time

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        
    def click_Get_Started(self):
        element = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/getStartedButton')
        element.click()

    def click_none_of_the_above(self):
        current_context = self.driver.current_context
        self.driver.switch_to.context("NATIVE_APP")
        alert = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.google.android.gms:id/cancel"))
        )
        alert.click()
        self.driver.switch_to.context(current_context)
        
    def select_country_code(self, country_code):
        element = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/spinner')
        element.click()
        
        current_context = self.driver.current_context
        self.driver.switch_to.context("NATIVE_APP")
        country_code_list = alert = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.ListView"))
                )
        scroll_to_element = "new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains(\"" + country_code + "\"))"
        country_code_item = self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, scroll_to_element)
        country_code_item.click()
        self.driver.switch_to.context(current_context)
        
    def enter_phone_number(self, phone_number):
        phone_number_input = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/input')
        phone_number_input.send_keys(phone_number)
        continue_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/continueButton')
        continue_button.click() 

    def enter_verification_code(self, code):
        continue_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/continueButton')
        continue_button.click() 

        # Split the code into individual digits
        code_digits = list(str(code))

        # Send each digit to the corresponding input field
        for i in range(len(code_digits)):
            xpath_locator = f'(//android.widget.EditText[@resource-id="com.hdw.james.rider:id/inputEditText"])[{i+1}]'
            input_field = wait_until_element_visible(self.driver, By.XPATH, xpath_locator)
            input_field.send_keys(code_digits[i])
        
        continue_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/continueButton')
        continue_button.click() 
        
    def allow_permissions(self):
        allow_locations_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/permissionsLocationButton')
        allow_locations_button.click()
        
        current_context = self.driver.current_context
        self.driver.switch_to.context("NATIVE_APP")
        location_only_this_time_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_one_time_button"))
        )
        location_only_this_time_button.click()
        self.driver.switch_to.context(current_context)
        
        #  use if notifications need to be set up
        allow_notifications_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/permissionsNotificationButton')
        allow_notifications_button.click()
        self.driver.switch_to.context("NATIVE_APP")
        notifications_allow_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.android.permissioncontroller:id/permission_allow_button"))
        )
        notifications_allow_button.click()
        self.driver.switch_to.context(current_context)
        
        try:
            continue_button = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/permissionsContinueButton')
            continue_button.click()
        except:
            pass

    # def enter_full_name(self, first_name, last_name):
    #     wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/firstNameInput').send_keys(first_name)
    #     wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/lastNameInput').send_keys(last_name)
    #     wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/buttonContinue').click()
        
    # def review_splash_and_continue(self):
    #     wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/splash_title').is_displayed()
    #     wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/splash_continue_button').click()

    # def skip_onboarding(self):
    #     self.driver.find_element_by_id('com.hdw.james.rider:id/SKIP_ONBOARDING').click()

    def get_main_menu(self):
        toolbar = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/MAIN_MENU_ID')
        return toolbar

    # def enter_details(self, username, password, email):
    #     # replace 'username_locator', 'password_locator', and 'email_locator' with the actual locators
    #     self.driver.find_element_by_id('username_locator').send_keys(username)
    #     self.driver.find_element_by_id('password_locator').send_keys(password)
    #     self.driver.find_element_by_id('email_locator').send_keys(email)

    # def press_register_button(self):
    #     self.driver.find_element_by_id('register_button_locator').click()

    def get_error_message(self):
        error_msg = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/snackbar_text').text
        return error_msg