Feature: Account Creation Feature
    As a user
    I want to create an account in my app
    So that I can access its features

    Scenario: Successful Account Creation
        Given I am on the registration screen
        When I enter a valid phone number
        And I enter a valid verification code
        And I enter a valid full name and finish the registration process
        Then I should see the home screen dashboard

    Scenario: Unsuccessful Account Creation
        Given I am on the registration screen
        When I enter invalid details
        And I press the register button
        Then I should see an error message