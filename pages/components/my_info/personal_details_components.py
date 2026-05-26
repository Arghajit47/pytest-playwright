from constants.my_info_constants import Api_Endpoints
from utils.ui_helpers import UIHelpers
from constants.my_info_constants import MyInfoConstants
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from pytest_pulse import pulse_step, step
from pages.base_page import BasePage
class PersonalDetailsComponent:
    def __init__(self, page) -> None:
        self.page = page
        self.base_page = BasePage(page)
        self.ui_helper = UIHelpers(page)

    @step("Click on My Info Tab option")
    def click_on_my_info_tab(self):
        with pulse_step("Click on My Info Tab option"):
            self.base_page.waitForFullyPageLoad()
            self.base_page.click(PersonalDetailsLocators.MY_INFO_OPTION)    

    @step("Verify employee details is visible")
    def verify_employee_details(self):
        with pulse_step("Verify employee details is visible in sidebar"):
            self.base_page.verify_element_is_visible(PersonalDetailsLocators.TAB(MyInfoConstants.PERSONAL_DETAILS_TAB_TEXT))
        with pulse_step("Verify employee full name is visible"):
            self.base_page.verify_element_is_visible(PersonalDetailsLocators.EMPLOYEE_NAME)
        with pulse_step("Verify employee image is visible"):
            self.base_page.verify_element_is_visible(PersonalDetailsLocators.EMPLOYEE_IMAGE)

    @step("Fetch employee details from API")
    def fetch_employee_details_from_api(self):
        response = self.base_page.wait_for_api_call(self.click_on_my_info_tab, Api_Endpoints.PERSONAL_DETAILS_ENDPOINT.value)
        return response

    @step("Verify Gender")
    def verify_gender(self, gender):
        with pulse_step("Verify Gender"):
            if gender == 1 or gender == "1":
                self.base_page.verify_element_is_checked(PersonalDetailsLocators.GENDER_MALE)
            elif gender == 2 or gender == "2":
                self.base_page.verify_element_is_checked(PersonalDetailsLocators.GENDER_FEMALE)    

    @step("Verify Smoker Status")
    def verify_smoker_status(self, smoker):
        with pulse_step("Verify Smoker Status"):
            if smoker is True or smoker == "true":
                self.base_page.verify_element_is_checked(PersonalDetailsLocators.SMOKER_STATUS)
            else:
                self.base_page.verify_element_is_not_checked(PersonalDetailsLocators.SMOKER_STATUS)    
                    
    @step("Validate employee details")
    def validate_employee_details(self, response_json):
        data = response_json["data"]
        with pulse_step("Validate employee details"):
            self.base_page.verify_element_value(PersonalDetailsLocators.FIRST_NAME, data.get("firstName", ""))
            self.base_page.verify_element_value(PersonalDetailsLocators.MIDDLE_NAME, data.get("middleName", ""))
            self.base_page.verify_element_value(PersonalDetailsLocators.LAST_NAME, data.get("lastName", ""))
        with pulse_step("Validate Employee Id and Other Id"):
            self.base_page.verify_element_value(PersonalDetailsLocators.EMPLOYEE_ID, data.get("employeeId", ""))
            self.base_page.verify_element_value(PersonalDetailsLocators.OTHER_ID, data.get("otherId", ""))
        with pulse_step("Validate Driving License Number"):
            self.base_page.verify_element_value(PersonalDetailsLocators.DRIVER_LICENSE_NUMBER, data.get("drivingLicenseNo", ""))
        with pulse_step("Validate License Expiry Date"):
            expiry = data.get("drivingLicenseExpiredDate")
            formatted_expiry = self.ui_helper.convert_date_to_dropdown_format(expiry) if expiry else ""
            self.base_page.verify_element_value(PersonalDetailsLocators.LICENSE_EXPIRY_DATE, formatted_expiry)
        with pulse_step("Validate Nationality"):
            nationality_dict = data.get("nationality")
            nationality_name = nationality_dict.get("name", "") if nationality_dict else ""
            self.base_page.verify_element_text(PersonalDetailsLocators.NATIONALITY, nationality_name)
        with pulse_step("Validate Maritial Status"):
            self.base_page.verify_element_text(PersonalDetailsLocators.MARITAL_STATUS, data.get("maritalStatus", ""))
        with pulse_step("Validate Date of Birth"):
            dob = data.get("birthday")
            formatted_dob = self.ui_helper.convert_date_to_dropdown_format(dob) if dob else ""
            self.base_page.verify_element_value(PersonalDetailsLocators.DATE_OF_BIRTH, formatted_dob)
        with pulse_step("Validate Gender"):
            self.verify_gender(data.get("gender"))
        # Validate Military Service if present in both DOM and API response
        military_service_locator = self.page.locator(PersonalDetailsLocators.MILITARY_SERVICE)
        if military_service_locator.count() > 0 and "militaryService" in data:
            with pulse_step("Validate Military Service"):
                self.base_page.verify_element_value(PersonalDetailsLocators.MILITARY_SERVICE, data["militaryService"])
                
        # Validate Smoker Status if present in both DOM and API response
        smoker_locator = self.page.locator(PersonalDetailsLocators.SMOKER_STATUS)
        if smoker_locator.count() > 0 and "smoker" in data:
            with pulse_step("Validate Smoker Status"):
                self.verify_smoker_status(data["smoker"])
            
    @step("Validate custom fields")
    def validate_custom_fields(self):
        with pulse_step("Reload the page and wait for custom fields api call"):            
            response = self.base_page.wait_for_api_call(self.base_page.refresh_page, Api_Endpoints.PERSONAL_DETAILS_CUSTOM_FIELDS_ENDPOINT.value)
            customFields = response.get("data") or {}
            self.base_page.waitForFullyPageLoad()
        
            if "custom1" in customFields and customFields["custom1"]:
                with pulse_step("Validate blood group"):    
                    self.base_page.verify_element_text(PersonalDetailsLocators.BLOOD_GROUP, customFields["custom1"])
        
            if "custom2" in customFields and customFields["custom2"]:
                with pulse_step("Validate test field"):    
                    self.base_page.verify_element_value(PersonalDetailsLocators.TEST_FIELD, customFields["custom2"])
            