from features.pages.base_page import BasePage
from helper import wait_until_element_visible
from selenium.webdriver.common.by import By

class MainMenu(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        open_profile_btn = wait_until_element_visible(self.driver, By.XPATH, '//android.widget.FrameLayout[@resource-id="com.hdw.james.rider:id/profileContainer"]/android.view.ViewGroup')
        open_profile_btn.click()
        
    def open_settings(self):
        open_settings_btn = wait_until_element_visible(self.driver, By.XPATH, '//android.widget.TextView[@resource-id="com.hdw.james.rider:id/title" and @text="SETTINGS"]')
        open_settings_btn.click()
        
    def open_previous_rides(self):
        open_previous_rides_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/previousRidesContainer')
        open_previous_rides_btn.click()
        
    def open_my_drivers(self):
        open_my_drivers_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/myDriversContainer')
        open_my_drivers_btn.click()
        
    def open_legal(self):
        open_legal_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/legalContainer')
        open_legal_btn.click()
        
    def sign_out(self):
        sign_out_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/signOutContainer')
        sign_out_btn.click()