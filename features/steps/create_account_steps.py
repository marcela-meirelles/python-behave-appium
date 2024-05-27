from behave import given, when, then
from features.pages.registration_page import RegistrationPage
import allure

@given('I am on the registration screen')
def step_given(context):
    context.registration_page = RegistrationPage(context.driver)
    context.registration_page.click_Get_Started()
    allureLogs('Given I am on the registration screen')

@when('I enter a valid phone number')
def step_when(context):
    context.registration_page.click_none_of_the_above()
    #   Afghanistan (+93)
    context.registration_page.select_country_code('Afghanistan (+93)')
    context.registration_page.enter_phone_number('701111112')
    allureLogs('When I enter a valid phone number')

@when('I enter a valid verification code')
def step_when(context):
    context.registration_page.enter_verification_code('123456')
    allureLogs('And I enter a valid verification code')

@when('I allow permissions and finish the registration process')
def step_when(context):
    context.registration_page.allow_permissions()

@then('I should see the home screen dashboard')
def step_then(context):
    assert context.registration_page.get_main_menu().is_displayed()

@when('I enter invalid details')
def step_when(context):
    context.registration_page.click_none_of_the_above()
    context.registration_page.select_country_code('Afghanistan (+93)')
    context.registration_page.enter_phone_number('INVALID *** 123123')
    allureLogs('When I enter invalid details')

@then('I should see an error message')
def step_then(context):
    assert context.registration_page.get_error_message() == 'Something went wrong, please try again'
    allureLogs('Then I should see an error message')
    
def allureLogs(text):
    with allure.step(text):
        pass