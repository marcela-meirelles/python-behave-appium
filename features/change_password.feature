Feature: Change password

  As a user,
  I want to change my password,
  So that I can keep my account secure.

  Scenario: Successful password change
    Given I am on the account settings page
    And I am on the change password screen
    When I enter my current password
    And I enter a new password
    And I confirm the new password
    Then I should see a confirmation message that the password change was successful