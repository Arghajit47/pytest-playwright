from constants.my_info_constants import Api_Endpoints, MyInfoConstants, ContactDetails
from utils.ui_helpers import UIHelpers
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from pages.components.my_info.personal_details_components import PersonalDetailsComponent
from pages.base_page import BasePage
from locators.components.my_info.contact_details_locators import ContactDetailsLocators
from pytest_pulse import step, pulse_step


class ContactDetailsComponent:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.ui_helpers = UIHelpers(page)
        self.personal_details = PersonalDetailsComponent(page)

    @step("Click on Contact Details Tab")
    def click_on_contact_details_tab(self):
        with pulse_step("Click on Contact Details Tab"):
            self.personal_details.click_on_my_info_tab()
            self.base_page.click(PersonalDetailsLocators.TAB(MyInfoConstants.CONTACT_DETAILS_TAB_TEXT))

    @step("fetch contact details from api")
    def fetch_contact_details_from_api(self):
        response = self.base_page.wait_for_api_call(self.click_on_contact_details_tab, Api_Endpoints.CONTACT_DETAILS_ENDPOINT.value)
        return response

    @step("verify contact details")
    def verify_contact_details(self, response):
        with pulse_step("verify contact details"):
            contact_details = response["data"]
        with pulse_step("verify street 1"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.STREET_1.value), contact_details.get("street1") or "")
        with pulse_step("verify street 2"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.STREET_2.value), contact_details.get("street2") or "")
        with pulse_step("verify city"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.CITY.value), contact_details.get("city") or "")
        with pulse_step("verify state"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.STATE.value), contact_details.get("province") or "")
        with pulse_step("verify postal code"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.POSTAL_CODE.value), contact_details.get("zipCode") or "")
        with pulse_step("verify country"):
            country_code = contact_details.get("countryCode")
            expected_country = self.ui_helpers.get_country_name(country_code) if country_code else "-- Select --"
            self.base_page.verify_element_text(ContactDetailsLocators.CONTACT_DETAILS_DROPDOWN_FIELDS, expected_country)
        with pulse_step("verify home"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.HOME.value), contact_details.get("homeTelephone") or "")
        with pulse_step("verify mobile"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.MOBILE.value), contact_details.get("mobile") or "")
        with pulse_step("verify work"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.WORK.value), contact_details.get("workTelephone") or "")
        with pulse_step("verify work email"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.WORK_EMAIL.value), contact_details.get("workEmail") or "")
        with pulse_step("verify other email"):
            self.base_page.verify_element_value(ContactDetailsLocators.CONTACT_DETAILS_INPUT_FIELDS(ContactDetails.OTHER_EMAIL.value), contact_details.get("otherEmail") or "")
