from behave import given, when, then
from features.pages.login_page import LoginPage

@given('I am on the login screen')
def step_given(context):
    context.login_page = LoginPage(context.driver)

@when('I enter valid username and password')
def step_when(context):
    context.login_page.enter_username('valid_username')
    context.login_page.enter_password('valid_password')

@when('I press the login button')
def step_when(context):
    context.login_page.press_login_button()

@then('I should be redirected to the home screen')
def step_then(context):
    # replace 'home_screen_locator' with the actual locator
    assert context.driver.find_element_by_id('home_screen_locator')

@when('I enter invalid username and password')
def step_when(context):
    context.login_page.enter_username('invalid_username')
    context.login_page.enter_password('invalid_password')

@then('I should see an error message for unsuccessful login')
def step_then(context):
    assert context.login_page.get_error_message() == 'Expected error message'