Feature: Account creation
    In order to post bookmarks
    As a registered user
    I must create an account
    
    Scenario: Create new account
        Given I want to create an account
        When I complete the form with username and password
        And post the date
        Then I receive notification that my account was created
        
    Scenario: Existing username
        Given I choose a username that already exists
        When I submit the form
        Then I am notified that the username already exists
