from pages.base_page import BasePage
import pytest
from pages.directory_page import DirectoryPage
from pytest_pulse import pulse_step, step

pytestmark = pytest.mark.usefixtures("login_via_cookies")


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Directory")
@step("Test Directory Page Filters: Search by Name, Job Title and Location")
def test_directory_page(page) -> None:
    with pulse_step("Instantiate Directory Page"):
        directory_page = DirectoryPage(page)
    with pulse_step("Verify Directory page url and title"):
        directory_page.navigate_to_directory_page()
    with pulse_step("Verify Directory page Search by Name"):
        directory_page.search_employee_by_name("manda")
    with pulse_step("Verify Directory page Search by Job Title"):
        directory_page.select_dropdown_for_job_title("Account Assistant")
    with pulse_step("Verify Directory page Search by Location"):
        directory_page.select_dropdown_for_location("New York Sales Office")
        directory_page.click_search_button()


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Directory")
@step("Test Employee Directory Live Sync")
def test_employee_directory_live_sync(page):
    with pulse_step("Instantiate Directory Page"):
        directory_page = DirectoryPage(page)
    with pulse_step("Get live directory data"):
        live_employees = directory_page.get_live_directory_data()
    with pulse_step("Verify grid container"):
        directory_page.verify_employee_details_with_api_data(live_employees)
