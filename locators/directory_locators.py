from constants.directory_constants import DirectoryConstants


class DirectoryPageLocators:
    DIRECTORY_OPTION = (
        f"//li//a//span[text()='{DirectoryConstants.DIRECTORY_OPTION_TEXT}']"
    )
    DIRECTORY_PAGE_HEADER_TITLE = "h6.oxd-topbar-header-breadcrumb-module"
    DIRECTORY_PAGE_HEADER = "h5.oxd-table-filter-title"
    FILTER_LABELS = "label.oxd-label"
    EMPLOYEE_NAME_DROPDOWN = "//input[@placeholder='Type for hints...']"
    DROPDOWN_SELECT_OPTION = "div.oxd-select-dropdown"
    DROPDOWN_OPTIONS = (
        lambda value: f"div.oxd-select-dropdown div.oxd-select-option span:has-text('{value}')"
    )
    SELECT_DROPDOWN = "div.oxd-select-text"
    RESET_BUTTON = "button[type='reset']"
    SEARCH_BUTTON = "button[type='submit']"
    DIRECTORY_CARD = ".orangehrm-directory-card"
    PROFILE_PICTURE = ".orangehrm-profile-picture-img"
    CARD_SUBTITLE = ".orangehrm-directory-card-subtitle"
    CARD_BODY = ".orangehrm-directory-card-body"
    CARD_DESCRIPTION = ".orangehrm-directory-card-description"
    MEMBER_CARD_CONTAINER = ".orangehrm-container"
