
Feature: Verify API Response Code
  Scenario: GET request to /products endpoint
    Given the API endpoint "http://172.21.128.1:3000/products"
    When a GET request is made to the endpoint
    Then the response code should be 200
