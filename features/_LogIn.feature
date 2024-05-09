Feature: Log in
    The purpose of this feature is to cover all the scenarios the log in.

Background:
    Given The page loads

@Test
Scenario: 01. Log in the app with standard user
    Given The user enters the "standard_user" and "secret_sauce"
    When The user clicks on the log in button
    Then The user is logged in successfully