from constants.components.buzz.buzz_constants import BuzzConstants


class BuzzLocators:
    # Page heading
    PAGE_HEADING = f"h6:has-text('{BuzzConstants.BUZZ_HEADING}')"
    NEWSFEED_TITLE = f".orangehrm-buzz-newsfeed-title:has-text('{BuzzConstants.BUZZ_NEWSFEED_TITLE}')"

    # Post input area
    POST_INPUT = f".{BuzzConstants.POST_INPUT_CLASS}"
    POST_BUTTON = f"button[type='submit']:has-text('{BuzzConstants.POST_BUTTON_TEXT}')"

    # Share buttons
    SHARE_PHOTOS_BUTTON = f"button:has-text('{BuzzConstants.SHARE_PHOTOS_TEXT}')"
    SHARE_VIDEO_BUTTON = f"button:has-text('{BuzzConstants.SHARE_VIDEO_TEXT}')"

    # Filter buttons
    MOST_RECENT_POSTS_BUTTON = f".orangehrm-post-filters-button:has-text('{BuzzConstants.MOST_RECENT_POSTS}')"
    MOST_LIKED_POSTS_BUTTON = f".orangehrm-post-filters-button:has-text('{BuzzConstants.MOST_LIKED_POSTS}')"
    MOST_COMMENTED_POSTS_BUTTON = f".orangehrm-post-filters-button:has-text('{BuzzConstants.MOST_COMMENTED_POSTS}')"

    # Post elements
    BUZZ_POST = ".orangehrm-buzz-post"
    POST_EMPLOYEE_NAME = f".{BuzzConstants.POST_EMPLOYEE_NAME_CLASS}"
    POST_BODY_TEXT = f".{BuzzConstants.POST_BODY_TEXT_CLASS}"
    POST_TIME = f".{BuzzConstants.POST_TIME_CLASS}"

    # Post footer actions
    LIKE_BUTTON = f".{BuzzConstants.HEART_ICON_CLASS}"
    COMMENT_BUTTON = ".orangehrm-buzz-post-footer button:has(i.bi-chat-text-fill)"
    SHARE_BUTTON = ".orangehrm-buzz-post-footer button:has(i.bi-share-fill)"

    # Stats
    POST_STATS_ROW = ".orangehrm-buzz-stats-row"

    # Post config (three dots menu) — click the icon-button, not the icon
    POST_CONFIG_BUTTON = ".oxd-icon-button:has(.bi-three-dots)"

    # Delete post menu item inside the config dropdown
    DELETE_POST_MENU_ITEM = f".{BuzzConstants.POST_CONFIG_MENU_ITEM_CLASS}:has-text('{BuzzConstants.DELETE_POST_MENU_TEXT}')"

    # Delete confirmation dialog button
    DELETE_DIALOG_BUTTON = f".oxd-dialog-sheet button:has-text('{BuzzConstants.DELETE_CONFIRMATION_TEXT}')"

    # Empty state
    NO_POSTS_AVAILABLE = f"//p[text()='{BuzzConstants.NO_POSTS_AVAILABLE}']"