Feature: Sample code testing

    Scenario: Open google and check title
        Given Opening browser
        When Providing url in browser
        Then Verify title of the Google page
