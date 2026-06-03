from pages.base_page import BasePage
from locators.components.performance.performance_reviews_locators import PerformanceReviewsLocators
from constants.components.performance.performance_reviews_constants import PerformanceReviewsConstants
from pytest_pulse import step, pulse_step

class PerformanceReviewsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    @step("Navigate to Performance Reviews via direct URL")
    def navigate_to_page(self):
        with pulse_step("Navigating to Performance Reviews directly"):
            self.navigateToUrl(PerformanceReviewsConstants.PERFORMANCE_REVIEWS_URL)
            
    def verify_page_loaded(self):
        with pulse_step("Verifying Performance Reviews page is loaded"):
            self.verify_element_is_visible(PerformanceReviewsLocators.PAGE_TITLE)

    @step("Verify core search filters and action buttons are visible")
    def verify_search_inputs_and_action_buttons(self):
        """Verifies that all core search filter inputs and action buttons are fully visible."""
        with pulse_step("Verify core search inputs are visible"):
            self.verify_element_is_visible(PerformanceReviewsLocators.EMPLOYEE_NAME)
            self.verify_element_is_visible(PerformanceReviewsLocators.JOB_TITLE_DROPDOWN)
            
        with pulse_step("Verify action buttons are visible"):
            self.verify_element_is_visible(PerformanceReviewsLocators.SEARCH_BUTTON)
            self.verify_element_is_visible(PerformanceReviewsLocators.RESET_BUTTON)

    @step("Get live performance reviews")
    def get_live_performance_reviews(self) -> dict:
        """Navigates to page and intercepts the initial reviews response list payload."""
        response = self.base_page.wait_for_api_call(
            lambda: self.navigate_to_page(),
            PerformanceReviewsConstants.PERFORMANCE_REVIEWS_API_ENDPOINT
        )
        self.base_page.wait_for_fully_page_loaded()
        return response

    def get_first_employee_name_from_live_reviews(self) -> str:
        """Fetches live reviews and extracts the full name of the first employee if present."""
        reviews_response = self.get_live_performance_reviews()
        reviews_data = reviews_response.get("data", [])
        if not reviews_data:
            return ""
        first_employee = reviews_data[0].get("employee", {})
        first_name = first_employee.get("firstName") or ""
        middle_name = first_employee.get("middleName") or ""
        last_name = first_employee.get("lastName") or ""
        return " ".join([n.strip() for n in [first_name, middle_name, last_name] if n.strip()])

    @step("Fetch performance reviews data via API")
    def fetch_performance_reviews_data(self, employee_name: str) -> dict:
        """Performs employee search and intercepts the dynamic reviews search response."""
        with pulse_step(f"Entering employee name: '{employee_name}'"):
            self.autocomplete_dropdown(PerformanceReviewsLocators.EMPLOYEE_NAME, employee_name)
            
        response = self.base_page.wait_for_api_call(
            lambda: self.click(PerformanceReviewsLocators.SEARCH_BUTTON),
            PerformanceReviewsConstants.PERFORMANCE_REVIEWS_API_ENDPOINT
        )
        self.base_page.wait_for_fully_page_loaded()
        return response

    def verify_records_exist(self, response: dict):
        """Verify UI matches API response following the high-reliability blueprint"""
        with pulse_step("Verifying records exist based on API response"):
            total_records = response.get("meta", {}).get("total") if isinstance(response.get("meta"), dict) else None
            
            if total_records is not None:
                if total_records > 0:
                    self.verify_element_is_visible(PerformanceReviewsLocators.RESULTS_TABLE)
                    self.verify_element_is_not_visible(PerformanceReviewsLocators.NO_RECORDS_TEXT)
                    # Verify count of rows (including header)
                    actual_count = self.get_element_count(PerformanceReviewsLocators.RESULTS_ROWS)
                    expected_rows = total_records + 1
                    if actual_count != expected_rows:
                        raise AssertionError(f"Expected {expected_rows} table rows, but found {actual_count}")
                else:
                    self.verify_element_is_visible(PerformanceReviewsLocators.NO_RECORDS_TEXT)
                    # When 0 records are found, the table wrapper and header (1 row) are still visible.
                    actual_count = self.get_element_count(PerformanceReviewsLocators.RESULTS_ROWS)
                    if actual_count > 1:
                        raise AssertionError(f"Expected 1 table row (header) for empty state, but found {actual_count} rows")
        
