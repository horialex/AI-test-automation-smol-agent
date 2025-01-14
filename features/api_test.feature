
Feature: Verify response code for products endpoint

  Scenario: GET request to products endpoint without query parameters
    Given the API endpoint "http://172.21.128.1:3000/products"
    When a GET request is made to the endpoint without query parameters
    Then the response code should be 200
