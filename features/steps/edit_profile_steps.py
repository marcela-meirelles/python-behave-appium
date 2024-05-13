from behave import given, when, then
from features.pages.profile_page import ProfilePage

@given('I am on the profile screen')
def step_given(context):
    context.profile_page = ProfilePage(context.driver)

@when('I enter new valid details')
def step_when(context):
    context.profile_page.enter_details('new_valid_username', 'new_valid_email')

@when('I press the save button')
def step_when(context):
    context.profile_page.press_save_button()

@then('I should see a success message for editing the profile')
def step_then(context):
    assert context.profile_page.get_success_message() == 'Expected success message'

@when('I enter new invalid details')
def step_when(context):
    context.profile_page.enter_details('new_invalid_username', 'new_invalid_email')

@then('I should see an error message for unsuccessful editing of the profile')
def step_then(context):
    assert context.profile_page.get_error_message() == 'Expected error message'