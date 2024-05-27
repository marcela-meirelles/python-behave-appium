from behave import given, when, then
from features.pages.account_settings_page import AccountSettingsPage
from features.pages.main_menu_page import MainMenu
from features.pages.settings_page import SettingsPage
import allure

@given('I am on the account settings page')
def step_given_i_am_on_the_account_settings_page(context):
    context.page = AccountSettingsPage(context.driver)
    context.main_menu = MainMenu(context.driver)
    context.settings_page = SettingsPage(context.driver)
    context.page.open_main_menu()
    context.main_menu.open_settings()
    context.settings_page.open_account_settings()
    allureLogs('Given I am on the account settings page')
    
@given('I am on the change password screen')
def step_given_i_am_on_the_change_password_screen(context):
    context.account_settings_page = AccountSettingsPage(context.driver)   
    context.account_settings_page.change_password()
    allureLogs('and I am on the change password screen')
     
@when('I enter my current password')
def step_when_i_enter_my_current_password(context):
    context.account_settings_page.change_password('pass1', 'pass2')  # Replace 'current_password' with the actual password
    allureLogs('When I enter my current password')

@when('I enter a new password')
def step_when_i_enter_a_new_password(context):
    context.page.enter_new_password('new_password')  # Replace 'new_password' with the actual new password
    allureLogs('And I enter a new password')

@when('I confirm the new password')
def step_when_i_confirm_the_new_password(context):
    context.page.confirm_new_password('new_password')  # Replace 'new_password' with the actual new password
    allureLogs('And I confirm the new password')

@then('I should see a confirmation message that the password change was successful')
def step_then_i_should_see_a_confirmation_message(context):
    assert context.page.is_password_change_successful()
    allureLogs('Then I should see a confirmation message that the password change was successful')
    
def allureLogs(text):
    with allure.step(text):
        pass