from pages.components.my_info.contact_details_components import ContactDetailsComponent
import pytest
from pytest_pulse import step


@pytest.mark.usefixtures("login", "logout")


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("ContactDetails")
@step("Verify Contact Details UI")
def test_contact_details_ui_api_validation(page, request_setup, login_via_api):
    contact_details_component = ContactDetailsComponent(page)
    response_json = contact_details_component.fetch_contact_details_from_api()
    contact_details_component.verify_contact_details()
