Feature: Testing GET endpoint for products

  Scenario Outline: GET /products should return 200
    Given I set the URL to "http://172.21.128.1:3000/products"
    When I send a GET request
    Then I should receive a response code of <status_code>

    Examples:
      | status_code |
      | 200         |