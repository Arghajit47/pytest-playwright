class PerformanceReviewsLocators:
    PAGE_TITLE = ".oxd-text--h5:has-text('Employee Reviews')"
    
    # Search filters
    EMPLOYEE_NAME = "//label[text()='Employee Name']/following::input[1]"
    JOB_TITLE_DROPDOWN = "//label[text()='Job Title']/following::div[contains(@class, 'oxd-select-text')][1]"
    SUB_UNIT_DROPDOWN = "//label[text()='Sub Unit']/following::div[contains(@class, 'oxd-select-text')][1]"
    STATUS_DROPDOWN = "//label[text()='Status']/following::div[contains(@class, 'oxd-select-text')][1]"
    
    SEARCH_BUTTON = "button[type='submit']:has-text('Search')"
    RESET_BUTTON = "button:has-text('Reset')"
    
    # Grid results
    RESULTS_TABLE = ".oxd-table"
    RESULTS_ROWS = ".oxd-table-row"
    NO_RECORDS_TEXT = "//span[text()='No Records Found']"
    
    # Dropdown selections
    DROPDOWN_OPTIONS = lambda option : f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"
