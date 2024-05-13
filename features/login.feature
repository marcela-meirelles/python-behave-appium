Feature: Login Feature
    As a user
    I want to login to my app
    So that I can access its features

    Scenario: Successful Login
        Given I am on the login screen
        When I enter valid username and password
        And I press the login button
        Then I should be redirected to the home screen

    Scenario: Unsuccessful Login
        Given I am on the login screen
        When I enter invalid username and password
        And I press the login button
        Then I should see an error message for unsuccessful login