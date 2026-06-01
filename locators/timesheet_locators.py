class TimeSheetLocators:
    SELECT_EMPLOYEE_HEADING = "h5:has-text('Select Employee'), h6:has-text('Select Employee'), .oxd-text:has-text('Select Employee')"
    TIMESHEETS_PENDING_ACTION_HEADING = "h5:has-text('Timesheets Pending Action'), h6:has-text('Timesheets Pending Action'), .oxd-text:has-text('Timesheets Pending Action')"
    
    # Employee selection
    EMPLOYEE_NAME_INPUT = "//input[@placeholder='Type for hints...']"
    VIEW_BUTTON = "button[type='submit']:has-text('View')"
    
    # Timesheet table
    TIMESHEET_TABLE = ".oxd-table"
    TIMESHEET_ROWS = ".oxd-table-row"
    EMPLOYEE_NAME_CELL = ".oxd-table-cell:nth-child(1)"
    TIMESHEET_PERIOD_CELL = ".oxd-table-cell:nth-child(2)"
    ACTIONS_CELL = ".oxd-table-cell:nth-child(3)"
    VIEW_ACTION_BUTTON = "button:has-text('View')"
    
    # Records found text
    RECORDS_FOUND_TEXT = "//*[contains(text(), 'Records Found')]"
    
    # No records text (following the blueprint pattern)
    NO_RECORDS_TEXT = "//span[text()='No Records Found']"