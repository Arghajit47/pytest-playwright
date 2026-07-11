import pytest

from pages.components.maintenance.purge_employee_page import PurgeEmployeePage
from constants.components.maintenance.purge_employee_constants import PurgeEmployeeConstants
from pytest_pulse import step, pulse_step


pytestmark = pytest.mark.usefixtures("login_via_cookies")


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Maintenance")
@pytest.mark.pulse_tag("PurgeEmployee")
@step("Test navigation to Purge Employee page and verify core UI elements are visible.")
def test_purge_employee_basic_navigation_and_ui_elements(page):
    purge_employee_page = PurgeEmployeePage(page)

    with pulse_step("Navigate to Purge Employee page and handle admin access"):
        purge_employee_page.navigate_and_confirm_admin_access()

    with pulse_step("Verify page is loaded"):
        purge_employee_page.verify_page_loaded()

    with pulse_step("Verify core form elements are visible"):
        purge_employee_page.verify_form_elements()


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Maintenance")
@pytest.mark.pulse_tag("PurgeEmployee")
@step("Test that clicking Search without selecting an employee shows a validation error.")
def test_purge_employee_search_without_selection_shows_validation(page):
    purge_employee_page = PurgeEmployeePage(page)

    with pulse_step("Navigate to Purge Employee page and handle admin access"):
        purge_employee_page.navigate_and_confirm_admin_access()

    with pulse_step("Verify page is loaded"):
        purge_employee_page.verify_page_loaded()

    with pulse_step("Click Search without selecting an employee"):
        purge_employee_page.click_search_without_employee()

    with pulse_step("Verify validation error is displayed"):
        purge_employee_page.verify_validation_error()


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Maintenance")
@pytest.mark.pulse_tag("PurgeEmployee")
@step("Test that searching for a non-existent past employee returns no records and API confirms zero results.")
def test_purge_employee_search_nonexistent_past_employee(page):
    purge_employee_page = PurgeEmployeePage(page)

    with pulse_step("Navigate to Purge Employee page and handle admin access"):
        purge_employee_page.navigate_and_confirm_admin_access()

    with pulse_step("Verify page is loaded"):
        purge_employee_page.verify_page_loaded()

    with pulse_step("Search for a past employee with query that yields no results"):
        api_response = purge_employee_page.search_past_employee(
            PurgeEmployeeConstants.SEARCH_QUERY
        )

    with pulse_step("Verify API response indicates zero past employees"):
        purge_employee_page.verify_empty_api_response(api_response)

    with pulse_step("Verify Purge button is not visible without a selected employee"):
        purge_employee_page.verify_purge_button_not_visible()


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Maintenance")
@pytest.mark.pulse_tag("PurgeEmployee")
@step("Test that the topbar Purge Records dropdown contains Employee Records and Candidate Records sub-menu items.")
def test_purge_employee_topbar_navigation_submenu(page):
    purge_employee_page = PurgeEmployeePage(page)

    with pulse_step("Navigate to Purge Employee page and handle admin access"):
        purge_employee_page.navigate_and_confirm_admin_access()

    with pulse_step("Verify page is loaded"):
        purge_employee_page.verify_page_loaded()

    with pulse_step("Verify topbar Purge Records tab is visible"):
        purge_employee_page.verify_topbar_navigation()

    with pulse_step("Expand Purge Records dropdown and verify sub-menu items"):
        purge_employee_page.verify_purge_records_submenu()


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Maintenance")
@pytest.mark.pulse_tag("PurgeEmployee")
@step("Test admin access interstitial page appears when navigating to Purge Employee for the first time.")
def test_purge_employee_admin_access_verification(page):
    purge_employee_page = PurgeEmployeePage(page)

    with pulse_step("Navigate to Purge Employee page"):
        purge_employee_page.navigate_to_page()

    with pulse_step("Verify admin access interstitial is displayed"):
        purge_employee_page.verify_admin_access_page()

    with pulse_step("Confirm admin access with password"):
        purge_employee_page.confirm_admin_access()

    with pulse_step("Verify Purge Employee page is loaded after confirmation"):
        purge_employee_page.verify_page_loaded()