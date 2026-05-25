from pages.components.my_info.personal_details_components import PersonalDetailsComponent
import pytest


@pytest.mark.usefixtures("login", "logout")


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("PersonalDetails")
def test_personal_details_ui_api_validation(page, request_setup, login_via_api):
    personal_details_component = PersonalDetailsComponent(page)
    response_json = personal_details_component.fetch_employee_details_from_api()
    personal_details_component.verify_employee_details()
    personal_details_component.validate_employee_details(response_json)
