from features.pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def open_profile(self):
        self.driver.find_element_by_xpath('//android.widget.FrameLayout[@resource-id="com.hdw.james.rider:id/profileContainer"]/android.view.ViewGroup').click()
        
    def set_profile_photo(self):
        self.driver.find_element_by_id('com.hdw.james.rider:id/profileCameraButton').click()
        self.driver.find_element_by_id('com.hdw.james.rider:id/imagePickeGalleryRow').click()
        # implement the logic to select a photo from the gallery
        
    def enter_details(self, firstname, lastname):
        self.driver.find_element_by_id('com.hdw.james.rider:id/firstNameInput').send_keys(firstname)
        self.driver.find_element_by_id('com.hdw.james.rider:id/lastNameInput').send_keys(lastname)

    def press_save_button(self):
        # replace 'save_button_locator' with the actual locator
        self.driver.find_element_by_id('save_button_locator').click()

    def get_success_message(self):
        # replace 'success_message_locator' with the actual locator
        return self.driver.find_element_by_id('success_message_locator').text

    def get_error_message(self):
        # replace 'error_message_locator' with the actual locator
        return self.driver.find_element_by_id('error_message_locator').text