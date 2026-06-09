Feature: Login Testing

    # Scenario: Valid Login
    #     Given user is on the login page
    #     When user enters valid username and password
    #     Then user should be redirected to the dashboard

    # Scenario Outline: Invalid Login
    #     Given user is on the login page
    #     When user enters "<username>" and "<password>"
    #     Then user should see an error message
    #     Examples:
    #         | username       | password       |
    #         | user123    | 123456  |
    #         | teste_one      | @*&$0 |
    #         | admin@gmail.com    | admin|

    Scenario: query params login
        Given user is on the login page
        When verify with bellow query params
            | username | password       |
            | admin  | admin         |
        Then verify login was made