from pages.components.my_info.emergency_contacts_components import EmergencyContactsComponent
from constants.my_info_constants import EmergencyContactsTestData
import pytest
from pytest_pulse import step, pulse_step

pytestmark = pytest.mark.usefixtures("login", "logout")


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("EmergencyContacts")
@step("Verify Emergency Contacts UI")
def test_emergency_contacts_ui_api_validation(page, request_setup, login_via_api):
    emergency_contacts_component = EmergencyContactsComponent(page)
    response_json = emergency_contacts_component.fetch_emergency_contacts_from_api()
    emergency_contacts_component.verify_emergency_contacts_ui(response_json)


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("EmergencyContacts")
@step("Verify adding and deleting emergency contact")
def test_add_and_verify_emergency_contact(page, request_setup, login_via_api):
    emergency_contacts_component = EmergencyContactsComponent(page)
    
    # 1. Navigate and load baseline contacts
    response_json = emergency_contacts_component.fetch_emergency_contacts_from_api()
    
    contact_name = EmergencyContactsTestData.get_dynamic_contact_name()

    # 2. Add contact via UI form
    emergency_contacts_component.add_emergency_contact(
        name=contact_name,
        relationship=EmergencyContactsTestData.RELATIONSHIP,
        home_phone=EmergencyContactsTestData.HOME_TELEPHONE,
        mobile=EmergencyContactsTestData.MOBILE,
        work_phone=EmergencyContactsTestData.WORK_TELEPHONE
    )
    
    # 3. Assert and verify the new contact shows up inside the UI records table
    new_response_json = emergency_contacts_component.fetch_emergency_contacts_from_api()
    emergency_contacts_component.verify_emergency_contacts_ui(new_response_json)
    
    # 4. Clean up: Delete the test contact via the UI and confirm deletion
    emergency_contacts_component.delete_emergency_contact(contact_name)
