from constants.components.leave.leave_list_constants import LeaveListConstants
import pytest
from pages.components.leave.leave_list_page import LeaveListPage
from locators.components.leave.leave_list_locators import LeaveListLocators
from pytest_pulse import pulse_step, step

@pytest.mark.usefixtures("login", "logout")
@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("LeaveManagement")
@step("Test to verify that filtering with non-existent data correctly displays 'No Records Found' message.")
def test_leave_list_no_records_with_random_filter(page):
    leave_list_page = LeaveListPage(page)
    
    with pulse_step("Navigate to Leave List page via menu"):
        response = leave_list_page.fetch_leave_list_data()
        leave_list_page.verify_page_loaded()
    
    with pulse_step("Apply filters with non-existent date range"):
        filtered_response = leave_list_page.filter_leaves(
            from_date="2000-01-01",
            to_date="2000-01-02"
        )
    
    with pulse_step("Verify 'No Records Found' message is displayed"):
        leave_list_page.verify_no_records_found(filtered_response)


@pytest.mark.usefixtures("login", "logout")
@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("LeaveManagement")
@step("Test to verify that the reset button clears applied filters on the Leave List page.")
def test_leave_list_reset_filters(page):
    leave_list_page = LeaveListPage(page)
    
    with pulse_step("Navigate to Leave List page via menu"):
        leave_list_page.fetch_leave_list_data()
        
    baseline_date = page.locator(LeaveListLocators.FROM_DATE).get_attribute("value") or ""
    
    with pulse_step("Apply a specific 'From Date' filter"):
        leave_list_page.filter_leaves(from_date=LeaveListConstants.TEST_DATE)
    
    with pulse_step("Reset all applied filters"):
        leave_list_page.reset_filters()
    
    leave_list_page.verify_date_reset(LeaveListLocators.FROM_DATE, baseline_date)


@pytest.mark.usefixtures("login", "logout")
@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("LeaveManagement")
@step("Test to verify that filtering by leave status updates the results table correctly.")
def test_leave_list_filter_by_status(page):
    leave_list_page = LeaveListPage(page)
    
    with pulse_step("Navigate to Leave List page via menu"):
        response = leave_list_page.fetch_leave_list_data()
    
    with pulse_step("Filter leave list by 'Pending Approval' status"):
        filtered_response = leave_list_page.filter_leaves(status=LeaveListConstants.TEST_STATUS)
    
    with pulse_step("Verify results table is visible"):
        leave_list_page.verify_records_exist(filtered_response)
