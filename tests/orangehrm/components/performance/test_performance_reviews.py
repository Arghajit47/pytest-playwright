from constants.components.performance.performance_reviews_constants import PerformanceReviewsConstants
import pytest
from pages.components.performance.performance_reviews_page import PerformanceReviewsPage
from locators.components.performance.performance_reviews_locators import PerformanceReviewsLocators
from pytest_pulse import pulse_step, step

pytestmark = pytest.mark.usefixtures("login_via_cookies")

@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Performance")
@pytest.mark.pulse_tag("Reviews")
@step("Test to verify navigation to Performance Reviews page and that basic components are visible.")
def test_performance_reviews_basic_navigation_and_ui_elements(page):
    performance_reviews_page = PerformanceReviewsPage(page)
    
    with pulse_step("Navigate to Performance Reviews page"):
        performance_reviews_page.navigate_to_page()
        performance_reviews_page.verify_page_loaded()
        
    performance_reviews_page.verify_search_inputs_and_action_buttons()


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Performance")
@pytest.mark.pulse_tag("Reviews")
@step("Test to verify that filtering by Employee Name updates the performance reviews table correctly matching the API.")
def test_performance_reviews_records_display_based_on_api_response(page):
    performance_reviews_page = PerformanceReviewsPage(page)
    
    with pulse_step("Get dynamic employee name from live Performance Reviews list response"):
        employee_name = performance_reviews_page.get_first_employee_name_from_live_reviews()
        
    with pulse_step("Verify page loaded successfully"):
        performance_reviews_page.verify_page_loaded()
        
    if employee_name:
        with pulse_step(f"Filter reviews by employee name: '{employee_name}'"):
            api_response = performance_reviews_page.fetch_performance_reviews_data(employee_name)
        with pulse_step("Verify results table matches API response"):
            performance_reviews_page.verify_records_exist(api_response)
    else:
        with pulse_step("No reviews found. Filter using empty name to verify empty state"):
            api_response = performance_reviews_page.fetch_performance_reviews_data("")
        with pulse_step("Verify empty state matches API response"):
            performance_reviews_page.verify_records_exist(api_response)
