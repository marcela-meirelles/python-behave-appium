from features.pages.base_page import BasePage
from helper import wait_until_element_visible
from selenium.webdriver.common.by import By

class AccountSettingsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        
    def change_password(self, currentPassword, newPassword):
        
        wait_until_element_visible(self.driver, By.XPATH, '//android.widget.TextView[@resource-id="com.hdw.james.rider:id/title" and @text="CHANGE PASSWORD"]').click()
        wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/currentPasswordInput').send_keys(currentPassword)
        wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/newPasswordInput').send_keys(newPassword)
        self.driver.close_menu() # this is a method from the BasePage class, it clicks on Done
        
    def delete_account(self):
        wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/saveButton').click()
        # implement the logic to delete the account