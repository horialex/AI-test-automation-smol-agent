
Feature: Login Page Functionality
  As a user, 
  I want to be able to log in to the application,
  So that I can access my account.

  Scenario: User is presented with the login page first
    Given that I open the application
    Then I should be on the login page

  Scenario Outline: Error message is shown when either text field is left blank
    Given that I am on the login page
    When I enter "<username>" in the username field
    And I enter "<password>" in the password field
    And I click the login button
    Then I should see an error message "<error_message>"

    Examples:
      | username | password | error_message               |
      |          |          | Please enter both username and password. |
      | user1    |          | Please enter both username and password. |
      |          | pass1    | Please enter both username and password. |

  Scenario: Error message is shown when username does not exist
    Given that I am on the login page
    When I enter "nonexistentuser" in the username field
    And I enter "pass1" in the password field
    And I click the login button
    Then I should see an error message "Invalid username. Please try again."

  Scenario: Error message is shown when password is incorrect
    Given that I am on the login page
    When I enter "user1" in the username field
    And I enter "wrongpass" in the password field
    And I click the login button
    Then I should see an error message "Invalid password. Please try again."

  Scenario: Successful login with correct credentials
    Given that I am on the login page
    When I enter "existinguser" in the username field
    And I enter "correctpass" in the password field
    And I click the login button
    Then I should be redirected to the home page
