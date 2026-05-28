from constants.components.leave.leave_list_constants import LeaveListConstants
from enum import Enum

class LeaveListLocators:
    # Side panel locators
    LEAVE_OPTION = (
        f"//li//a//span[text()='{LeaveListConstants.SIDE_PANEL_MENU}']"
    )
    # Top navigation bar locators
    LEAVE_LIST_ACCORDIAN = f"//a[text()='{LeaveListConstants.TOP_NAV_LINK}']"

    # Header - Using a more robust XPath that targets the specific heading class
    PAGE_TITLE = ".oxd-text--h5:has-text('Leave List')"
    
    # Filter Fields - Targeting by associated label text but using a more stable relationship
    FROM_DATE = "//label[contains(text(), 'From Date')]/following::input[1]"
    TO_DATE = "//label[contains(text(), 'To Date')]/following::input[1]"
    STATUS_DROPDOWN = "//label[contains(text(), 'Show Leave with Status')]/following::div[contains(@class, 'oxd-select-text')]"
    LEAVE_TYPE_DROPDOWN = "//label[contains(text(), 'Leave Type')]/following::div[contains(@class, 'oxd-select-text')]"
    EMPLOYEE_NAME = "//label[contains(text(), 'Employee Name')]/following::input[1]"
    SUB_UNIT_DROPDOWN = "//label[contains(text(), 'Sub Unit')]/following::div[contains(@class, 'oxd-select-text')]"
    INCLUDE_PAST_EMPLOYEES_CHECKBOX = "//label[contains(text(), 'Include Past Employees')]/following::input[1]"
    
    # Buttons - Using class and text combined for better stability
    RESET_BUTTON = "button.oxd-button--ghost:has-text('Reset')"
    SEARCH_BUTTON = "button.oxd-button--secondary:has-text('Search')"
    
    # Results Table
    RESULTS_TABLE = ".oxd-table"
    NO_RECORDS_TEXT = "//span[text()='No Records Found']"
    TABLE_HEADER_DATE = "th:has-text('Date')"
    TABLE_HEADER_EMPLOYEE = "th:has-text('Employee Name')"
    TABLE_HEADER_STATUS = "th:has-text('Status')"

    # Filter dropdown options
    DROPDOWN_OPTIONS = lambda status : f"//div[contains(@class, 'oxd-select-option') and contains(., '{status}')]"
