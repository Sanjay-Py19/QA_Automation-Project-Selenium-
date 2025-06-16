Feature: Login


  Scenario: Successful Login with valid credentials to flipkart
    Given login with valid credentials
    When Provide valid user and password
    And user click on enter button
    Then Login to system


