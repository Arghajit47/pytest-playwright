from constants.components.leave.leave_list_constants import LeaveListConstants
from pages.base_page import BasePage
from locators.components.leave.leave_list_locators import LeaveListLocators
from pytest_pulse import pulse_step, step

class LeaveListPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    @step("Navigate to Leave List via Side Panel")
    def navigate_via_menu(self):
        from constants.components.leave.leave_list_constants import LeaveListConstants
        with pulse_step(f"Click on '{LeaveListConstants.SIDE_PANEL_MENU}' menu in side panel"):
            self.click(LeaveListLocators.LEAVE_OPTION)


    def verify_page_loaded(self):
        with pulse_step("Verifying Leave List page is loaded"):
            self.verify_element_is_visible(LeaveListLocators.PAGE_TITLE)

    def filter_leaves(self, from_date=None, to_date=None, status=None, leave_type=None, employee_name=None, sub_unit=None, include_past=False):
        with pulse_step("Filtering leaves with provided criteria"):
            if from_date:
                self.fill(LeaveListLocators.FROM_DATE, from_date)
            if to_date:
                self.fill(LeaveListLocators.TO_DATE, to_date)
            if status:
                self.click(LeaveListLocators.STATUS_DROPDOWN)
                self.click(LeaveListLocators.DROPDOWN_OPTIONS(status))
            if leave_type:
                self.click(LeaveListLocators.LEAVE_TYPE_DROPDOWN)
                self.click(LeaveListLocators.DROPDOWN_OPTIONS(leave_type))
            if employee_name:
                self.autocomplete_dropdown(LeaveListLocators.EMPLOYEE_NAME, employee_name)
            if sub_unit:
                self.click(LeaveListLocators.SUB_UNIT_DROPDOWN)
                self.click(LeaveListLocators.DROPDOWN_OPTIONS(sub_unit))
            if include_past:
                self.click(LeaveListLocators.INCLUDE_PAST_EMPLOYEES_CHECKBOX)
            
            response = self.base_page.wait_for_api_call(
                lambda: self.click(LeaveListLocators.SEARCH_BUTTON),
                LeaveListConstants.LEAVE_REQUESTS_URL
            )
            self.base_page.wait_for_fully_page_loaded()
            return response


    def reset_filters(self):
        with pulse_step("Resetting leave filters"):
            self.click(LeaveListLocators.RESET_BUTTON)

    def verify_no_records_found(self, response):
        with pulse_step("Verifying no records found"):
            if response["meta"]["total"] == 0:
                self.verify_element_is_visible(LeaveListLocators.NO_RECORDS_TEXT)

    def verify_records_exist(self, response):
        with pulse_step("Verifying records exist in the table"):
            if response["meta"]["total"] > 0:
                self.verify_element_is_visible(LeaveListLocators.RESULTS_TABLE)
                self.verify_element_is_not_visible(LeaveListLocators.NO_RECORDS_TEXT)
            else:
                self.verify_element_is_visible(LeaveListLocators.NO_RECORDS_TEXT)
                self.verify_element_is_not_visible(LeaveListLocators.RESULTS_TABLE)

    def verify_date_reset(self, date_locator, expected_date_value):
        with pulse_step("Verifying date has been reset"):
            current_val = self.base_page.get_attribute(date_locator, "value") or ""
            self.base_page.verify_equal(current_val, expected_date_value or "")

    @step("Fetch leave list from API")
    def fetch_leave_list_data(self):
        response = self.base_page.wait_for_api_call(
                lambda: self.navigate_via_menu(),
                LeaveListConstants.LEAVE_REQUESTS_URL
            )
        self.base_page.wait_for_fully_page_loaded()
        return response