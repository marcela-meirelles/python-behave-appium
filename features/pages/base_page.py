from helper import wait_until_element_visible
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_menu(self):
        main_menu_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/MAIN_MENU_ID')
        main_menu_btn.click()
        
    def close_menu(self):
        close_menu_btn = wait_until_element_visible(self.driver, By.ID, 'com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID')
        close_menu_btn.click()
           
    def click_back_arrow(self):
        back_arrow_btn = wait_until_element_visible(self.driver, By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
        back_arrow_btn.click()
    