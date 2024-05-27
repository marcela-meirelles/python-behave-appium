from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from appium.webdriver.common import TouchAction

def wait_until_element_visible(driver, by, value, timeout=20):
    """
    Wait until the specified element is visible on the page.

    :param driver: The WebDriver instance.
    :param by: The method to locate the element.
    :param value: The value for the method.
    :param timeout: The maximum wait time (in seconds). Default is 10.
    :return: The WebElement instance.
    """
    return WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((by, value)))

# def tap_at_coordinate(driver, x, y):
#         action = TouchAction(driver)
#         action.tap(None, x, y, 1).perform()
#         action.press(x=x, y=y).release().perform()