from features.pages.base_page import BasePage

class MainMenu(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.hdw.james.rider:id/profileContainer"]/android.view.ViewGroup').click()
        
    def open_settings(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/settingsContainer').click()
        
    def open_previous_rides(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/previousRidesContainer').click()
        
    def open_my_drivers(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/myDriversContainer').click()
        
    def open_legal(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/legalContainer').click()
        
    def sign_out(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/signOutContainer').click()