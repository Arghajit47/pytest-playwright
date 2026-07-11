from constants.components.maintenance.purge_employee_constants import PurgeEmployeeConstants


class PurgeEmployeeLocators:
    # Page heading
    PAGE_HEADING = f"h6:has-text('{PurgeEmployeeConstants.PURGE_EMPLOYEE_HEADING}')"
    BREADCRUMB_MODULE = f".oxd-topbar-header-breadcrumb h6:text('{PurgeEmployeeConstants.PURGE_EMPLOYEE_MODULE_BREADCRUMB}')"
    BREADCRUMB_SECTION = f".oxd-topbar-header-breadcrumb h6:text('{PurgeEmployeeConstants.PURGE_EMPLOYEE_BREADCRUMB}')"

    # Admin access page (intermediate verification page)
    ADMIN_ACCESS_HEADING = f"h6:has-text('{PurgeEmployeeConstants.ADMIN_ACCESS_HEADING}')"
    ADMIN_ACCESS_USERNAME_INPUT = "//label[text()='Username']/following::input[1]"
    ADMIN_ACCESS_PASSWORD_INPUT = "//label[text()='Password']/following::input[1]"
    ADMIN_ACCESS_CONFIRM_BUTTON = f"button:has-text('Confirm')"
    ADMIN_ACCESS_CANCEL_BUTTON = f"button:has-text('{PurgeEmployeeConstants.ADMIN_ACCESS_CANCEL_TEXT}')"

    # Past Employee autocomplete
    PAST_EMPLOYEE_INPUT = f"//label[text()='{PurgeEmployeeConstants.PAST_EMPLOYEE_LABEL}']/following::input[1]"
    AUTOCOMPLETE_DROPDOWN = ".oxd-autocomplete-dropdown"
    AUTOCOMPLETE_OPTION = ".oxd-autocomplete-option"
    NO_RECORDS_FOUND_OPTION = f".oxd-autocomplete-option:has-text('{PurgeEmployeeConstants.NO_RECORDS_FOUND}')"

    # Search button
    SEARCH_BUTTON = f"button[type='submit']:has-text('{PurgeEmployeeConstants.SEARCH_BUTTON_TEXT}')"

    # Required field hint
    REQUIRED_HINT = ".orangehrm-form-hint"

    # Validation error (appears when Search clicked without selecting employee)
    VALIDATION_ERROR = ".oxd-input-field-error-message"

    # Selected employee section (appears after successful search)
    SELECTED_EMPLOYEE_SECTION = ".orangehrm-card-container:has-text('Employee')"

    # Purge button and confirmation dialog
    PURGE_BUTTON = f"button:has-text('{PurgeEmployeeConstants.PURGE_BUTTON_TEXT}')"
    PURGE_DIALOG = ".oxd-dialog-sheet"
    PURGE_DIALOG_YES_BUTTON = f".oxd-dialog-sheet button:has-text('{PurgeEmployeeConstants.PURGE_CONFIRMATION_TEXT}')"
    PURGE_DIALOG_CANCEL_BUTTON = f".oxd-dialog-sheet button:has-text('{PurgeEmployeeConstants.PURGE_DIALOG_CANCEL_TEXT}')"

    # Data privacy notice
    DATA_PRIVACY_NOTICE = f"//p[contains(text(), '{PurgeEmployeeConstants.DATA_PRIVACY_NOTICE_TEXT}')]"

    # Topbar navigation
    PURGE_RECORDS_TAB = ".oxd-topbar-body-nav-tab.--parent"
    EMPLOYEE_RECORDS_SUBMENU = f".oxd-topbar-body-nav-tab-link:has-text('{PurgeEmployeeConstants.EMPLOYEE_RECORDS_SUBMENU}')"
    CANDIDATE_RECORDS_SUBMENU = f".oxd-topbar-body-nav-tab-link:has-text('{PurgeEmployeeConstants.CANDIDATE_RECORDS_SUBMENU}')"
    ACCESS_RECORDS_TAB = f".oxd-topbar-body-nav-tab:has-text('{PurgeEmployeeConstants.ACCESS_RECORDS_TAB}')"

    # Sidebar Maintenance link
    SIDEBAR_MAINTENANCE_LINK = f"a:has-text('{PurgeEmployeeConstants.PURGE_EMPLOYEE_MODULE_BREADCRUMB}')"

    # Form
    PURGE_FORM = "form.oxd-form"