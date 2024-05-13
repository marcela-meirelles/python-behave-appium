from behave import given, when, then
from features.pages.registration_page import RegistrationPage

@given('I am on the registration screen')
def step_given(context):
    context.registration_page = RegistrationPage(context.driver)

@when('I enter a valid phone number')
def step_when(context):
    context.registration_page.enter_phone_number('93701111112')

@when('I enter a valid verification code')
def step_when(context):
    context.registration_page.enter_verification_code('123456')

@when('I enter a valid full name and finish the registration process')
def step_when(context):
    context.registration_page.enter_full_name('valid_first_name', 'valid_last_name')
    context.registration_page.review_splash_and_continue()
    context.registration_page.accept_location_permission()
    context.registration_page.skip_onboarding()

@then('I should see the home screen dashboard')
def step_then(context):
    assert context.registration_page.home_screen_dashboard_is_displayed()

@when('I enter invalid details')
def step_when(context):
    context.registration_page.enter_phone_number('INVALID *** 123123')

@then('I should see an error message')
def step_then(context):
    assert context.registration_page.get_error_message() == 'Expected error message'