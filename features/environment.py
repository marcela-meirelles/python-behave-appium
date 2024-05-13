from appium import webdriver
import os

def before_all(context):
    try:
        dir_path = os.path.dirname(os.path.realpath(__file__))
        app_path = os.path.join(dir_path, '..', 'James Rider_1.22.0.apk')
        context.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_capabilities={
            'platformName': 'Android',
            'deviceName': 'emulator-5554',
            'app': app_path,
            'automationName': 'UiAutomator2',
        })
    except Exception as e:
        print(f"Error setting up driver: {e}")
        context.driver = None

def after_all(context):
    if hasattr(context, 'driver') and context.driver is not None:
        context.driver.quit()