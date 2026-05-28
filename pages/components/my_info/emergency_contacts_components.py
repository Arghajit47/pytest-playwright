from constants.my_info_constants import Api_Endpoints, MyInfoConstants, EmergencyContacts
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from locators.components.my_info.emergency_contacts_locators import EmergencyContactsLocators
from pages.components.my_info.personal_details_components import PersonalDetailsComponent
from pages.base_page import BasePage
from pytest_pulse import step, pulse_step


class EmergencyContactsComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.personal_details = PersonalDetailsComponent(page)

    @step("Click on Emergency Contacts Tab")
    def click_on_emergency_contacts_tab(self):
        with pulse_step("Click on Emergency Contacts Tab"):
            self.personal_details.click_on_my_info_tab()
            self.base_page.click(PersonalDetailsLocators.TAB(MyInfoConstants.EMERGENCY_CONTACT_TAB_TEXT))

    @step("fetch emergency contacts from api")
    def fetch_emergency_contacts_from_api(self):
        response = self.base_page.wait_for_api_call(self.click_on_emergency_contacts_tab, Api_Endpoints.EMERGENCY_CONTACTS_ENDPOINT.value)
        return response

    @step("verify emergency contacts")
    def verify_emergency_contacts_ui(self, response):
        contacts = response.get("data") or []
        for contact in contacts:
            name = contact.get("name")
            relationship = contact.get("relationship")
            home_phone = contact.get("homePhone") or ""
            mobile = contact.get("mobilePhone") or ""
            work_phone = contact.get("officePhone") or ""
            
            with pulse_step(f"verify details for emergency contact: {name}"):
                self.base_page.verify_element_is_visible(EmergencyContactsLocators.RECORD_ROW_BY_NAME(name))
                self.base_page.verify_element_text(EmergencyContactsLocators.RECORD_CELL(name, 2), name)
                self.base_page.verify_element_text(EmergencyContactsLocators.RECORD_CELL(name, 3), relationship)
                self.base_page.verify_element_text(EmergencyContactsLocators.RECORD_CELL(name, 4), home_phone)
                self.base_page.verify_element_text(EmergencyContactsLocators.RECORD_CELL(name, 5), mobile)
                self.base_page.verify_element_text(EmergencyContactsLocators.RECORD_CELL(name, 6), work_phone)

    @step("add emergency contact")
    def add_emergency_contact(self, name, relationship, home_phone=None, mobile=None, work_phone=None):
        with pulse_step("Click on Add button"):
            self.base_page.click(EmergencyContactsLocators.ADD_CONTACT_BUTTON)
            
        with pulse_step("Fill emergency contact form"):
            self.base_page.fill(EmergencyContactsLocators.INPUT_FIELDS(EmergencyContacts.NAME.value), name)
            self.base_page.fill(EmergencyContactsLocators.INPUT_FIELDS(EmergencyContacts.RELATIONSHIP.value), relationship)
            if home_phone is not None:
                self.base_page.fill(EmergencyContactsLocators.INPUT_FIELDS(EmergencyContacts.HOME_TELEPHONE.value), home_phone)
            if mobile is not None:
                self.base_page.fill(EmergencyContactsLocators.INPUT_FIELDS(EmergencyContacts.MOBILE.value), mobile)
            if work_phone is not None:
                self.base_page.fill(EmergencyContactsLocators.INPUT_FIELDS(EmergencyContacts.WORK_TELEPHONE.value), work_phone)
                
        with pulse_step("Click Save button"):
            self.base_page.wait_for_api_call(
                lambda: self.base_page.click(EmergencyContactsLocators.SAVE_BUTTON),
                Api_Endpoints.EMERGENCY_CONTACTS_ENDPOINT.value
            )
            self.base_page.wait_for_fully_page_loaded()

    @step("delete emergency contact")
    def delete_emergency_contact(self, name):
        with pulse_step(f"Click Delete button for contact: {name}"):
            self.base_page.click(EmergencyContactsLocators.RECORD_DELETE_BUTTON(name))
            
        with pulse_step("Confirm deletion in popup dialog"):
            confirm_btn = "//button[contains(., 'Yes, Delete')]"
            self.base_page.wait_for_api_call(
                lambda: self.base_page.click(confirm_btn),
                Api_Endpoints.EMERGENCY_CONTACTS_ENDPOINT.value
            )
            self.base_page.wait_for_fully_page_loaded()
