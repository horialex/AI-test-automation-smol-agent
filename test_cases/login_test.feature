
Feature: User Login
  As a user
  I want to be able to log in to the application
  So that I can access my account

  Scenario: Successful login with valid username and password
    Given the user is on the login page
    When the user enters a valid username and password
    And the user clicks the login button
    Then the user should be redirected to the home page

  Scenario: Error when login name is left blank
    Given the user is on the login page
    When the user leaves the login name field blank
    And the user enters a valid password
    And the user clicks the login button
    Then the user should see an error message "Login name cannot be blank"

  Scenario: Error when password is left blank
    Given the user is on the login page
    When the user enters a valid login name
    And the user leaves the password field blank
    And the user clicks the login button
    Then the user should see an error message "Password cannot be blank"

  Scenario: Error when both login name and password are left blank
    Given the user is on the login page
    When the user leaves the login name and password fields blank
    And the user clicks the login button
    Then the user should see an error message "Login name and password cannot be blank"

  Scenario: Error when username does not exist
    Given the user is on the login page
    When the user enters a non-existent username
    And the user enters a valid password
    And the user clicks the login button
    Then the user should see an error message "Invalid username or password"

  Scenario: Error when password is incorrect
    Given the user is on the login page
    When the user enters a valid username
    And the user enters an incorrect password
    And the user clicks the login button
    Then the user should see an error message "Invalid username or password"
