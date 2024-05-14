from features.pages.base_page import BasePage

class SettingsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_account_settings(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/accountSettingsContainer').click()
        
    def open_payment_methods(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/paymentSettingsContainer').click()
        
    def open_calendar_settings(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/calendarSettingsContainer').click()
        
    def open_default_tip(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/defaultTipSettingsContainer').click()
        
    def open_support(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/supportContainer').click()