Feature: Test the login functionality on https://www.demo.guru99.com/V4/
  Scenario: Verify the login Section using valid credentials
    When I navigate to https://www.demo.guru99.com/V4/
    And I click on Accept All button
    And I enter valid userId
    And I enter valid password
    And I click Login button
    Then The Login is successfuly done

