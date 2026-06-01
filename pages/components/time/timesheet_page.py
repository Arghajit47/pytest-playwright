from locators.timesheet_locators import TimeSheetLocators
from constants.components.time.time_sheet_constants import TimeSheetConstants
from pages.base_page import BasePage
from pytest_pulse import step, pulse_step
import time


class TimeSheetPage:
    
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        
        # Initialize locators
        self.select_employee_heading = TimeSheetLocators.SELECT_EMPLOYEE_HEADING
        self.timesheets_pending_action_heading = TimeSheetLocators.TIMESHEETS_PENDING_ACTION_HEADING
        self.employee_name_input = TimeSheetLocators.EMPLOYEE_NAME_INPUT
        self.view_button = TimeSheetLocators.VIEW_BUTTON
        self.timesheet_table = TimeSheetLocators.TIMESHEET_TABLE
        self.timesheet_rows = TimeSheetLocators.TIMESHEET_ROWS
        self.employee_name_cell = TimeSheetLocators.EMPLOYEE_NAME_CELL
        self.timesheet_period_cell = TimeSheetLocators.TIMESHEET_PERIOD_CELL
        self.actions_cell = TimeSheetLocators.ACTIONS_CELL
        self.view_action_button = TimeSheetLocators.VIEW_ACTION_BUTTON
        self.records_found_text = TimeSheetLocators.RECORDS_FOUND_TEXT
        self.no_records_text = TimeSheetLocators.NO_RECORDS_TEXT
        
        # Initialize constants
        self.timesheet_page_url = TimeSheetConstants.TIMESHEETS_PAGE_URL
        self.timesheet_page_title = TimeSheetConstants.TIMESHEETS_PAGE_TITLE
        self.select_employee_heading_text = TimeSheetConstants.SELECT_EMPLOYEE_HEADING
        self.timesheets_pending_action_heading_text = TimeSheetConstants.TIMESHEETS_PENDING_ACTION_HEADING
        self.view_button_text = TimeSheetConstants.VIEW_BUTTON_TEXT
    
    @step("Navigate to Timesheet page")
    def navigate_to_timesheet_page(self):
        with pulse_step("Navigate to Timesheet page directly"):
            self.base_page.navigateToUrl(self.timesheet_page_url)
            
    @step("Verify Timesheet page loaded")
    def verify_timesheet_page_loaded(self):
        with pulse_step("Verify Timesheet page URL"):
            self.base_page.verify_page_url(self.timesheet_page_url)
        with pulse_step("Verify Timesheet page title"):
            self.base_page.verify_page_title(self.timesheet_page_title)
        with pulse_step("Verify Select Employee heading"):
            self.base_page.verify_element_text(
                self.select_employee_heading,
                self.select_employee_heading_text
            )
        with pulse_step("Verify Timesheets Pending Action heading"):
            self.base_page.verify_element_text(
                self.timesheets_pending_action_heading,
                self.timesheets_pending_action_heading_text
            )
            
    @step("Enter employee name in search")
    def enter_employee_name(self, employee_name: str):
        with pulse_step(f"Enter employee name: {employee_name}"):
            self.base_page.autocomplete_dropdown(self.employee_name_input, employee_name)
            
    @step("Click View button")
    def click_view_button(self):
        with pulse_step("Click View button"):
            self.base_page.click(self.view_button)
            
    @step("Get records count from table")
    def get_records_count(self):
        with pulse_step("Get records count from timesheet table"):
            return self.base_page.get_element_count(self.timesheet_rows)
            
    @step("Get records found text")
    def get_records_found_text(self):
        with pulse_step("Get records found text"):
            return self.base_page.get_element_inner_text(self.records_found_text)
            
    @step("Verify records exist based on API response")
    def verify_records_exist(self, api_response):
        """Verify UI matches API response - following blueprint pattern"""
        with pulse_step("Verify records exist based on API response"):
            total_records = api_response.get("meta", {}).get("total") if isinstance(api_response.get("meta"), dict) else None
            timesheet_id = api_response.get("data", {}).get("id") if isinstance(api_response.get("data"), dict) else None
            
            if total_records is not None:
                if total_records > 0:
                    self.base_page.verify_element_is_visible(self.timesheet_table)
                    self.base_page.verify_element_is_not_visible(self.no_records_text)
                    actual_count = self.get_records_count()
                    if actual_count != total_records:
                        raise AssertionError(f"Expected {total_records} rows, but found {actual_count}")
                else:
                    self.base_page.verify_element_is_visible(self.no_records_text)
                    self.base_page.verify_element_is_not_visible(self.timesheet_table)
            elif timesheet_id is not None:
                # If we are on the timesheet detail view page, verify timesheet header is visible
                self.base_page.verify_element_is_visible("h6:has-text('Timesheet')")
                
    @step("Click View action for first timesheet")
    def click_view_first_timesheet(self):
        """Click the View button for the first timesheet in the table"""
        with pulse_step("Click View action for first timesheet"):
            # Get all view buttons and click the first one
            view_buttons = self.page.locator(self.view_action_button)
            if view_buttons.count() > 0:
                view_buttons.first.click()
                self.base_page.wait_for_fully_page_loaded()
            else:
                raise AssertionError("No View buttons found in timesheet table")
                
    @step("Verify View button is visible")
    def verify_view_button_visible(self):
        with pulse_step("Verify View button is visible"):
            self.base_page.verify_element_is_visible(self.view_button)
            
    @step("Verify employee name input is visible")
    def verify_employee_name_input_visible(self):
        with pulse_step("Verify employee name input is visible"):
            self.base_page.verify_element_is_visible(self.employee_name_input)

    # New method to fetch timesheet data via API call
    @step("Fetch timesheet data via API")
    def fetch_timesheet_data(self, employee_name: str) -> dict:
        """Performs search and returns API response using wait_for_api_call.
        This method encapsulates the action and API interception.
        """        
        with pulse_step(f"Enter employee name: {employee_name}"):
            self.enter_employee_name(employee_name)
        
        response = self.base_page.wait_for_api_call(
            lambda: self.click_view_button(),
            TimeSheetConstants.TIMESHEET_API_URL_ENDPOINT
        )
        
        self.base_page.wait_for_fully_page_loaded()
        return response

    @step("Get live timesheet employees")
    def get_live_timesheet_employees(self) -> dict:
        """Navigates to timesheet page and captures the initial timesheets list response."""
        return self.base_page.wait_for_api_call(
            lambda: self.navigate_to_timesheet_page(),
            "**/api/v2/time/employees/timesheets/list**"
        )
