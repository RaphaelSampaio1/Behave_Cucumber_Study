Feature: Login Testing

    Scenario: Valid Login
        Given user is on the login page
        When user enters valid username and password
        Then user should be redirected to the dashboard
