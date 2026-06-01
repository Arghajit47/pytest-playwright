import pytest
from pages.components.time.timesheet_page import TimeSheetPage
from pytest_pulse import pulse_step, step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Time")
@pytest.mark.pulse_tag("Timesheet")
@step("Verify Timesheet page navigation and that basic elements are visible")
def test_timesheet_page_basic_navigation_and_ui_elements(page):
    with pulse_step("Instantiate Timesheet Page"):
        timesheet_page = TimeSheetPage(page)
        
    with pulse_step("Navigate to Timesheet page"):
        timesheet_page.navigate_to_timesheet_page()
        
    with pulse_step("Verify Timesheet page is fully loaded"):
        timesheet_page.verify_timesheet_page_loaded()
        
    with pulse_step("Verify basic UI elements are visible"):
        timesheet_page.verify_employee_name_input_visible()
        timesheet_page.verify_view_button_visible()


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Time")
@pytest.mark.pulse_tag("Timesheet")
@step("Verify Timesheet records display based on API response matching UI elements dynamically")
def test_timesheet_records_display_based_on_api_response(page, request_setup, login_via_api):
    with pulse_step("Instantiate Page Object"):
        timesheet_page = TimeSheetPage(page)
        
    with pulse_step("Get dynamic employee name from Timesheet List API"):
        timesheets_response = timesheet_page.get_live_timesheet_employees()
        timesheets_data = timesheets_response.get("data", [])
        assert len(timesheets_data) > 0, "No active timesheets found in database"
        
        # Combine name parts to form a valid employee name for searching
        first_employee = timesheets_data[0].get("employee", {})
        first_name = first_employee.get("firstName") or ""
        middle_name = first_employee.get("middleName") or ""
        last_name = first_employee.get("lastName") or ""
        employee_name = " ".join([n.strip() for n in [first_name, middle_name, last_name] if n.strip()])
        if not employee_name:
            employee_name = "manda akhil user"
            
    with pulse_step("Verify Timesheet page loaded"):
        timesheet_page.verify_timesheet_page_loaded()
        
    with pulse_step(f"Fetch timesheet data via API and verify UI for: {employee_name}"):
        api_response = timesheet_page.fetch_timesheet_data(employee_name)
        timesheet_page.verify_records_exist(api_response)
