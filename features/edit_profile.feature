Feature: Edit Profile Feature
    As a user
    I want to edit my profile in the app
    So that I can update my information

    Scenario: Successful Profile Edit
        Given I am on the profile screen
        When I enter new valid details
        And I press the save button
        Then I should see a success message for editing the profile

    Scenario: Unsuccessful Profile Edit
        Given I am on the profile screen
        When I enter new invalid details
        And I press the save button
        Then I should see an error message for unsuccessful editing of the profile