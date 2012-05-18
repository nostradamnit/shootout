Feature: User authentication
    In order to access authenicated features
    As a registered user
    I must authenticate my credentials
    
    Scenario: Account authentication
        Given I want to perform an authenticated action
        When I complete the form with my username and password
        And submit the form
        Then I receive notification that my credentials were correctly authenticated
        And that I have a authenticated session
        
    
