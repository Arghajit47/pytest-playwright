class BuzzConstants:
    BUZZ_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/buzz/viewBuzz"
    BUZZ_PAGE_TITLE = "OrangeHRM"
    BUZZ_HEADING = "Buzz"
    BUZZ_NEWSFEED_TITLE = "Buzz Newsfeed"

    # Post input
    POST_INPUT_CLASS = "oxd-buzz-post-input"
    POST_INPUT_PLACEHOLDER = "What's on your mind?"
    POST_BUTTON_TEXT = "Post"

    # Share buttons
    SHARE_PHOTOS_TEXT = "Share Photos"
    SHARE_VIDEO_TEXT = "Share Video"

    # Filter buttons
    MOST_RECENT_POSTS = "Most Recent Posts"
    MOST_LIKED_POSTS = "Most Liked Posts"
    MOST_COMMENTED_POSTS = "Most Commented Posts"

    # API endpoints (glob patterns for Playwright expect_response)
    BUZZ_FEED_API_ENDPOINT = "**/api/v2/buzz/feed*"
    BUZZ_POSTS_API_ENDPOINT = "**/api/v2/buzz/posts*"

    # Post elements
    POST_EMPLOYEE_NAME_CLASS = "orangehrm-buzz-post-emp-name"
    POST_BODY_TEXT_CLASS = "orangehrm-buzz-post-body-text"
    POST_TIME_CLASS = "orangehrm-buzz-post-time"
    HEART_ICON_CLASS = "orangehrm-heart-icon"

    # Stats
    LIKES_TEXT = "Like"
    COMMENTS_TEXT = "Comments"
    SHARES_TEXT = "Shares"

    # Post creation / deletion
    TEST_POST_TEXT = "This is an automated test post."
    DELETE_POST_MENU_TEXT = "Delete Post"
    DELETE_CONFIRMATION_TEXT = "Yes, Delete"
    POST_SUCCESS_TEXT = "Post Saved"

    # API endpoints for create / delete (glob patterns for Playwright expect_response)
    BUZZ_CREATE_POST_API_ENDPOINT = "**/api/v2/buzz/posts*"
    BUZZ_DELETE_POST_API_ENDPOINT = "**/api/v2/buzz/shares/*"

    # Post config menu item class (li inside oxd-dropdown-menu)
    POST_CONFIG_MENU_ITEM_CLASS = "orangehrm-buzz-post-header-config-item"

    # Delete confirmation dialog
    DELETE_DIALOG_BUTTON = ".oxd-dialog-sheet button:has-text('Yes, Delete')"

    # Empty state
    NO_POSTS_AVAILABLE = "No Posts Available"