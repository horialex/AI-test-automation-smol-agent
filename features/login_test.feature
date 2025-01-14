Feature: User Login
  As a user,
  I want to be able to log in to the application,
  So that I can access my account.

  Scenario: User opens the application
    Given I open the application
    Then I should see the login page

  Scenario: User submits empty login name
    Given I am on the login page
    And I enter an empty login name
    And I enter a valid password
    When I click the login button
    Then I should see an error message "Login name cannot be empty"

  Scenario: User submits empty password
    Given I am on the login page
    And I enter a valid login name
    And I enter an empty password
    When I click the login button
    Then I should see an error message "Password cannot be empty"

  Scenario: User submits both empty fields
    Given I am on the login page
    And I enter an empty login name
    And I enter an empty password
    When I click the login button
    Then I should see an error message "Login name and Password cannot be empty"

  Scenario: User submits non-existent login name
    Given I am on the login page
    And I enter a non-existent login name
    And I enter a valid password
    When I click the login button
    Then I should see an error message "Invalid login name or password"

  Scenario: User submits incorrect password
    Given I am on the login page
    And I enter a valid login name
    And I enter an incorrect password
    When I click the login button
    Then I should see an error message "Invalid login name or password"

  Scenario: User submits valid login name and password
    Given I am on the login page
    And I enter a valid login name
    And I enter a valid password
    When I click the login button
    Then I should be redirected to the dashboard
