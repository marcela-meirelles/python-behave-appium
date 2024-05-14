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
            'newCommandTimeout': 600,
            'appPackage': 'com.hdw.james.rider',
            'appActivity': 'com.hdw.james.rider.viewlayer.launcher.LauncherActivity'
        })
    except Exception as e:
        print(f"Error setting up driver: {e}")
        context.driver = None

def after_all(context):
    if hasattr(context, 'driver') and context.driver is not None:
        context.driver.quit()


# Translate those capabilities into Python appium style
# options = UiAutomator2Options()
# options.platform_name = 'Android'
# options.udid = 'emulator-5554'
# options.app_package = 'com.hdw.james.rider'
# options.app_activity = 'com.hdw.james.rider.viewlayer.launcher.LauncherActivity'
# options.device_name = 'Pixel 4 API 33'
# options.automation_name = 'UiAutomator2'
# options.platformVersion = '13'
# options.auto_grant_permissions = True

# # Create a driver instance  
# driver = webdriver.Remote('http://localhost:4723/wd/hub', options.to_capabilities())