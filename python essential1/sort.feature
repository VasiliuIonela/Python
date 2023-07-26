Feature: Test the sort functionality in Mobile List page for http://live.techpanda.org/index.php/
  Scenario: Verify item in Mobile List page can be sorted by 'Name'
    When I go to http://live.techpanda.org/index.php/
    And I click on 'MOBILE' page
    And I select 'SORT BY' dropdown as 'name'
    Then I should see a sorted mobile list by name
