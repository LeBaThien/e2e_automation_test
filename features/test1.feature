Feature: Google Search

  Scenario: Search for a keyword
    Given I am on the Google home page
    When I search for "GitHub Copilot"
    Then the results page is displayed
