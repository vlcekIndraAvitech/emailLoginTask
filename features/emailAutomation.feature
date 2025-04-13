Feature: Gmail Workflows

  Background:
    Given the browser is launched and the user navigates to the Gmail login page
    And the user inputs valid credentials
    Then the user should be logged in successfully

  Scenario: Block level 1 - Login and Logout
    When the user signs out
    Then the user should be redirected to the login page

  Scenario: Block level 2 - Send email to contact
    Given the user creates a new email to a contact
    When the user sends the email
    Then the email containing the message user composed should be in Sent messages
    When the user signs out
    Then the user should be redirected to the login page

  Scenario: Block level 3 - Send email with attachment
    Given the user creates a new email to a contact
    When the user adds an attachment
    Then the attachment should be visible in the message
    When the user sends the email
    Then the email containing the message user composed should be in Sent messages
    When the user signs out
    Then the user should be redirected to the login page