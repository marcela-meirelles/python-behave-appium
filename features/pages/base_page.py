class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_main_menu(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/MAIN_MENU_ID').click()
        
    def close_menu(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/DEFAULT_TEXT_ACTION_MENU_ID').click()
           
    def click_back_arrow(self):
        self.driver.find_by_xpath('//android.widget.ImageButton[@content-desc="Navigate up"]').click()
    
    