from pages.base_page import BasePage
from locators.components.maintenance.purge_employee_locators import PurgeEmployeeLocators
from constants.components.maintenance.purge_employee_constants import PurgeEmployeeConstants
from pytest_pulse import step, pulse_step


class PurgeEmployeePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    @step("Navigate to Purge Employee page")
    def navigate_to_page(self):
        with pulse_step("Navigating to Purge Employee page via direct URL"):
            self.navigateToUrl(PurgeEmployeeConstants.PURGE_EMPLOYEE_URL)

    @step("Verify Purge Employee page is loaded")
    def verify_page_loaded(self):
        with pulse_step("Verifying Purge Employee page heading is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.PAGE_HEADING)

    @step("Verify admin access interstitial is displayed")
    def verify_admin_access_page(self):
        with pulse_step("Verifying Administrator Access heading is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.ADMIN_ACCESS_HEADING)

    @step("Confirm admin access by entering password")
    def confirm_admin_access(self, password: str = ""):
        with pulse_step("Filling admin access password"):
            pwd = password or PurgeEmployeeConstants.ADMIN_ACCESS_PASSWORD
            self.fill(PurgeEmployeeLocators.ADMIN_ACCESS_PASSWORD_INPUT, pwd)

        with pulse_step("Clicking Confirm button on admin access page"):
            self.click(PurgeEmployeeLocators.ADMIN_ACCESS_CONFIRM_BUTTON)

    @step("Navigate to Purge Employee and handle admin access")
    def navigate_and_confirm_admin_access(self):
        with pulse_step("Navigate to Purge Employee page"):
            self.navigate_to_page()

        with pulse_step("Check for admin access interstitial and confirm if present"):
            self.wait_for_timeout(2000)
            if self.get_element_count(PurgeEmployeeLocators.ADMIN_ACCESS_HEADING) > 0:
                self.confirm_admin_access()

        with pulse_step("Verify Purge Employee page is loaded"):
            self.verify_page_loaded()

    @step("Verify core form elements are visible")
    def verify_form_elements(self):
        with pulse_step("Verify Past Employee autocomplete input is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.PAST_EMPLOYEE_INPUT)

        with pulse_step("Verify Search button is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.SEARCH_BUTTON)

    @step("Search for a past employee via autocomplete")
    def search_past_employee(self, query: str) -> dict:
        with pulse_step(f"Typing '{query}' into Past Employee autocomplete"):
            self.autocomplete_dropdown(PurgeEmployeeLocators.PAST_EMPLOYEE_INPUT, query)

        with pulse_step("Clicking Search button and intercepting API response"):
            response = self.base_page.wait_for_api_call(
                lambda: self.click(PurgeEmployeeLocators.SEARCH_BUTTON),
                PurgeEmployeeConstants.PAST_EMPLOYEE_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    @step("Click Search without selecting an employee")
    def click_search_without_employee(self):
        with pulse_step("Clicking Search button without selecting an employee"):
            self.click(PurgeEmployeeLocators.SEARCH_BUTTON)

    @step("Verify validation error is displayed")
    def verify_validation_error(self):
        with pulse_step("Verifying validation error message is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.VALIDATION_ERROR)

    @step("Verify no records found in autocomplete dropdown")
    def verify_no_records_found(self):
        with pulse_step("Verifying No Records Found option is visible in dropdown"):
            self.verify_element_is_visible(PurgeEmployeeLocators.NO_RECORDS_FOUND_OPTION)

    @step("Verify API response has zero past employees")
    def verify_empty_api_response(self, response: dict):
        with pulse_step("Verifying API response indicates zero past employees"):
            total = response.get("meta", {}).get("total") if isinstance(response.get("meta"), dict) else None
            if total is not None:
                assert total == 0, f"Expected 0 past employees, but got {total}"

    @step("Verify purge button is not visible (no employee selected)")
    def verify_purge_button_not_visible(self):
        with pulse_step("Verifying Purge button is not visible without employee selection"):
            self.verify_element_is_not_visible(PurgeEmployeeLocators.PURGE_BUTTON)

    @step("Verify topbar Purge Records navigation tab")
    def verify_topbar_navigation(self):
        with pulse_step("Verifying Purge Records tab is visible in topbar"):
            self.verify_element_is_visible(PurgeEmployeeLocators.PURGE_RECORDS_TAB)

    @step("Expand Purge Records dropdown and verify sub-menu items")
    def verify_purge_records_submenu(self):
        with pulse_step("Clicking Purge Records tab to expand dropdown"):
            self.click(PurgeEmployeeLocators.PURGE_RECORDS_TAB)

        with pulse_step("Verifying Employee Records sub-menu item is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.EMPLOYEE_RECORDS_SUBMENU)

        with pulse_step("Verifying Candidate Records sub-menu item is visible"):
            self.verify_element_is_visible(PurgeEmployeeLocators.CANDIDATE_RECORDS_SUBMENU)

    @step("Fetch past employees data via API")
    def fetch_past_employees_data(self, query: str) -> dict:
        with pulse_step(f"Typing '{query}' into autocomplete to trigger API"):
            self.autocomplete_dropdown(PurgeEmployeeLocators.PAST_EMPLOYEE_INPUT, query)

        with pulse_step("Intercepting past employees API response"):
            response = self.base_page.wait_for_api_call(
                lambda: None,
                PurgeEmployeeConstants.PAST_EMPLOYEE_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response