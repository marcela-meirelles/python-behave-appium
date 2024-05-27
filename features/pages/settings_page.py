from features.pages.base_page import BasePage
from helper import wait_until_element_visible
from selenium.webdriver.common.by import By

class SettingsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_account_settings(self):
        open_account_settings_btn = wait_until_element_visible(self.driver, By.XPATH, '//android.widget.TextView[@resource-id="com.hdw.james.rider:id/title" and @text="ACCOUNT"]')
        open_account_settings_btn.click()
        
    def open_payment_methods(self):
        open_payment_methods_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/paymentSettingsContainer')
        open_payment_methods_btn.click()
        
    def open_calendar_settings(self):
        open_calendar_settings_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/calendarSettingsContainer')
        open_calendar_settings_btn.click()
        
    def open_default_tip(self):
        open_default_tip_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/defaultTipSettingsContainer')
        open_default_tip_btn.click()
        
    def open_support(self):
        open_support_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/supportContainer')
        open_support_btn.click()