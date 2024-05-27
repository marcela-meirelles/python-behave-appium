Feature: Account Creation Feature
    As a user
    I want to create an account in my app
    So that I can access its features

    Scenario: Successful Account Creation
        Given I am on the registration screen
        When I enter a valid phone number
        And I enter a valid verification code
        And I allow permissions and finish the registration process
        Then I should see the home screen dashboard

    @smoke @regression
    Scenario: Unsuccessful Account Creation
        Given I am on the registration screen
        When I enter invalid details
        Then I should see an error message