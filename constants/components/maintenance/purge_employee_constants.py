class PurgeEmployeeConstants:
    PURGE_EMPLOYEE_URL = "https://opensource-demo.orangehrmlive.com/web/index.php/maintenance/purgeEmployee"
    PURGE_EMPLOYEE_PAGE_TITLE = "OrangeHRM"
    PURGE_EMPLOYEE_HEADING = "Purge Employee Records"
    PURGE_EMPLOYEE_BREADCRUMB = "Purge Records"
    PURGE_EMPLOYEE_MODULE_BREADCRUMB = "Maintenance"

    # Autocomplete label
    PAST_EMPLOYEE_LABEL = "Past Employee"

    # API endpoints (glob patterns for Playwright expect_response)
    PAST_EMPLOYEE_API_ENDPOINT = "**/api/v2/pim/employees*"
    PURGE_EMPLOYEE_API_ENDPOINT = "**/api/v2/maintenance/purge*"

    # Admin access page
    ADMIN_ACCESS_HEADING = "Administrator Access"
    ADMIN_ACCESS_PASSWORD = "admin123"
    ADMIN_ACCESS_CANCEL_TEXT = "Cancel"
    ADMIN_VERIFY_URL = "**/auth/adminVerify*"

    # Form validation
    REQUIRED_FIELD_ERROR = "Required"
    SEARCH_BUTTON_TEXT = "Search"
    PURGE_BUTTON_TEXT = "Purge"

    # Autocomplete dropdown
    NO_RECORDS_FOUND = "No Records Found"

    # Purge confirmation dialog
    PURGE_CONFIRMATION_TEXT = "Yes, Purge"
    PURGE_DIALOG_HEADING = "Purge Employee Records"
    PURGE_DIALOG_CANCEL_TEXT = "Cancel"

    # Data privacy notice text
    DATA_PRIVACY_NOTICE_TEXT = "Data@orangehrm.com"

    # Topbar sub-menu items
    PURGE_RECORDS_TAB = "Purge Records"
    EMPLOYEE_RECORDS_SUBMENU = "Employee Records"
    CANDIDATE_RECORDS_SUBMENU = "Candidate Records"
    ACCESS_RECORDS_TAB = "Access Records"

    # Search query hint for autocomplete (demo instance has zero past employees)
    SEARCH_QUERY = "a"