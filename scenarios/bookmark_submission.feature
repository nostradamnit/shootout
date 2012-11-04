Feature: Save bookmark
    In order to save a bookmark
    As as authenticated user
    I must submit the link to the bookmark service
    
    Scenario: Save bookmark
        Given I want to save a specific URL
        When I submit it to the bookmark service
        Then I receive notification that it was saved
