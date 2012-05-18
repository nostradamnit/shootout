Feature: Bookmark creation, modification and supression
    In order to create bookmarks
    As an authenticated user
    I must supply the link and optional description
    
    Scenario: Create new bookmark
        Given I want to create a bookmark
        When I complete the form with link and description
        And submit the form without errors
        Then I receive notification that my bookmark was created

    Scenario: View my bookmarks
        Given I want to view my bookmarks
        When I visit the my bookmark view URL
        Then I see a list of my bookmarks
