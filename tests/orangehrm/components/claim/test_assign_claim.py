import pytest

from pages.components.claim.assign_claim_page import AssignClaimPage
from pytest_pulse import step, pulse_step


pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Claim")
@step("Test Assign Claim with Valid Data")
def test_assign_claim_with_valid_data(page):
    with pulse_step("Initialize Assign Claim Page Object"):
        assign_claim_page = AssignClaimPage(page)
    with pulse_step("Navigate to Assign Claim Page"):
        assign_claim_page.navigate_to_assign_claim_page()

    with pulse_step("Assign a claim with valid data"):
        assign_claim_page.assign_valid_claim()

    with pulse_step("Verify claim assignment success message"):
        assign_claim_page.verify_claim_assignment_success_message()



