from appium import webdriver
import os
import pytest

# Options are only available since client version 2.3.0
# If you use an older client then switch to desired_capabilities
# instead: https://github.com/appium/python-client/pull/720
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from appium.webdriver.appium_service import AppiumService
from appium.webdriver.common.appiumby import AppiumBy

APPIUM_PORT = 4723
APPIUM_HOST = '127.0.0.1'


@pytest.fixture(scope='session')
def appium_service():
    service = AppiumService()
    service.start(
        # Check the output of `appium server --help` for the complete list of
        # server command line arguments
        args=['-address', APPIUM_HOST, '-p', str(APPIUM_PORT)],
        timeout_ms=20000,
        )
    yield service
    service.stop()
    
# def create_ios_driver(custom_opts = None):
#     options = XCUITestOptions()
#     options.platform_name = 'iOS'
#     options.udid = 'XXXXXXXXXXXXX'
#     options.app_package = 'com.hdw.james.rider'
#     options.app_activity = 'com.hdw.james.rider.viewlayer.launcher.LauncherActivity'
#     options.platformVersion = '13'
#     if custom_opts is not None:
#         options.load_capabilities(custom_opts)
#     # Appium1 points to http://127.0.0.1:4723/wd/hub by default
#     return webdriver.Remote('http://{APPIUM_HOST}:{APPIUM_PORT}', options=options)  

def create_android_driver(custom_opts = None):
    options = UiAutomator2Options()
    options.platformVersion = '13'
    options.udid = 'emulator-5554'
    options.app_package = 'com.hdw.james.rider'
    options.app_activity = 'com.hdw.james.rider.viewlayer.launcher.LauncherActivity'
    # options.auto_grant_permissions = True
    # options.auto_dismiss_alerts = True
    if custom_opts is not None:
        options.load_capabilities(custom_opts)
    # Appium1 points to http://127.0.0.1:4723/wd/hub by default
    return webdriver.Remote('http://127.0.0.1:4723', options=options)

    
def before_all(context):
    print(os.getcwd())
    
    apk_path = '/Users/marcelameirelles/Desktop/Python Appium/James Rider_1.22.0.apk'
    print(os.path.exists(apk_path))

    options = {
        'platformName': 'Android',
        'appium:app': '/Users/marcelameirelles/Desktop/Python Appium/James Rider_1.22.0.apk',
        'appium:udid': 'emulator-5554',
        'appium:platformName': 'Android',
        'appium:automationName': 'UiAutomator2',
        'appium:autoDismissAlerts': 'true',
        'appium:appPackage': 'com.hdw.james.rider',
        'appium:appActivity': 'com.hdw.james.rider.viewlayer.launcher.LauncherActivity',
        'appium:noReset': 'false',
    }
    context.driver = create_android_driver(options)
    # context.ios_driver = create_ios_driver(options) 
    
def after_all(context):
    if hasattr(context, 'driver'):
        context.driver.quit()
    
# def test_ios_click(appium_service, ios_driver_factory):
#     # Usage of the context manager ensures the driver session is closed properly
#     # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
#     with ios_driver_factory({
#         'appium:app': '/path/to/app/UICatalog.app.zip'
#     }) as driver:
#         el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
#         el.click()


def test_android_click(appium_service, android_driver_factory):
    # Usage of the context manager ensures the driver session is closed properly
    # after the test completes. Otherwise, make sure to call `driver.quit()` on teardown.
    with android_driver_factory({
        'appium:app': '/path/to/app/test-app.apk',
        'appium:udid': 'emulator-5554',
    }) as driver:
        el = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='item')
        el.click()
        
         
# def before_all(context):
#     try:
#         # capabilities = dict(
#         #     platformName='Android',
#         #     platformVersion='13',
#         #     deviceName='Pixel 4 API 33',
#         #     automationName='UiAutomator2',
#         #     appPackage='com.hdw.james.rider',
#         #     appActivity='com.hdw.james.rider.viewlayer.launcher.LauncherActivity',
#         #     autoGrantPermissions=True
#         # )

#         # appium_server_url = 'http://localhost:4723'

#         # context.driver = webdriver.Remote(appium_server_url, capabilities)
#         dir_path = os.path.dirname(os.path.realpath(__file__))
#         app_path = os.path.join(dir_path, '..', 'James Rider_1.22.0.apk')
#         context.driver = webdriver.Remote('http://127.0.0.1/:4723', desired_capabilities={
#             "appium:automationName": "UiAutomator2",
#             "platformName": "Android",
#             "appium:udid": "emulator-5554",
#             "appium:deviceName": "Pixel 8 Pro API 34",
#             "appium:autoGrantPermissions": True,
#             "appium:appPackage": "com.hdw.james.rider",
#             "appium:appActivity": "com.hdw.james.rider.viewlayer.launcher.LauncherActivity"
#         })
#         # yield context.driver
#     except Exception as e:
#         print(f"Error setting up driver: {e}")
#         context.driver = None

# def after_all(context):
#     if hasattr(context, 'driver') and context.driver is not None:
#         context.driver.quit()


# capabilities = dict(
#     platformName='Android',
#     platformVersion='13',
#     deviceName='Pixel 4 API 33',
#     automationName='UiAutomator2',
#     appPackage='com.hdw.james.rider',
#     appActivity='com.hdw.james.rider.viewlayer.launcher.LauncherActivity',
#     autoGrantPermissions=True
# )

# appium_server_url = 'http://localhost:4723'

# driver = webdriver.Remote(appium_server_url, capabilities)

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