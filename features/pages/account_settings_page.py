from features.pages.base_page import BasePage

class AccountSettingsPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def change_password(self, currentPassword, newPassword):
        self.driver.find_element_by_xpath('//androidx.recyclerview.widget.RecyclerView[@resource-id="com.hdw.james.rider:id/accountMenuRecycler"]/android.view.ViewGroup[3]').click()
        self.driver.find_element_by_id('com.hdw.james.rider:id/currentPasswordInput').send_keys(currentPassword)
        self.driver.find_element_by_id('com.hdw.james.rider:id/newPasswordInput').send_keys(newPassword)
        self.driver.close_menu() # this is a method from the BasePage class, it clicks on Done
        
    def delete_account(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/saveButton').click()
        # implement the logic to delete the account