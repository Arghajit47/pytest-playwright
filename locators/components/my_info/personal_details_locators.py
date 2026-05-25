from constants.my_info_constants import MyInfoConstants
from constants.my_info_constants import PersonalDetails
class PersonalDetailsLocators:
    MY_INFO_OPTION = (
        f"//li//a//span[text()='{MyInfoConstants.MY_INFO_TAB_OPTION}']"
    )
    TAB = lambda tabText : f"//div[@class='orangehrm-tabs-wrapper']/a[text()='{tabText}']"
    EMPLOYEE_NAME = "div.orangehrm-edit-employee-name h6"
    EMPLOYEE_IMAGE = "div.orangehrm-edit-employee-image img"
    SECTION_HEADERS = lambda headerText : f"//h6[contains(@class,'orangehrm-main-title') and text()='{headerText}']"
    LABEL_HEADERS = lambda labelText : f"//label[contains(@class, 'oxd-label') and contains(text(), '{labelText}')]"
    FIRST_NAME = "input[name='firstName']"
    MIDDLE_NAME = "input[name='middleName']"
    LAST_NAME = "input[name='lastName']"
    NICKNAME = "(//label[normalize-space(text())='Nickname']/following::input)[1]"
    EMPLOYEE_ID = f'(//label[normalize-space(text())="{PersonalDetails.EMPLOYEE_ID.value}"]/following::input)[1]'
    OTHER_ID = f'(//label[normalize-space(text())="{PersonalDetails.OTHER_ID.value}"]/following::input)[1]'
    DRIVER_LICENCE_NUMBER = f'(//label[normalize-space(text())="{PersonalDetails.DRIVER_LICENSE_NUMBER.value}"]/following::input)[1]'
    DRIVER_LICENSE_NUMBER = DRIVER_LICENCE_NUMBER
    LICENSE_EXPIRY_DATE = f'(//label[normalize-space(text())="{PersonalDetails.LICENSE_EXPIRY_DATE.value}"]/following::input)[1]'
    NATIONALITY = "(//div[@class='oxd-select-text-input'])[1]"
    MARITAL_STATUS = "(//div[@class='oxd-select-text-input'])[2]"
    DATE_OF_BIRTH = f'(//label[normalize-space(text())="{PersonalDetails.DATE_OF_BIRTH.value}"]/following::input)[1]'
    GENDER_MALE = f'(//label[normalize-space(text())="{PersonalDetails.GENDER.value}"]/following::input)[1]'
    GENDER_FEMALE = f'(//label[normalize-space(text())="{PersonalDetails.GENDER.value}"]/following::input)[2]'
    BLOOD_GROUP = "(//div[@class='oxd-select-text-input'])[3]"
    TEST_FIELD = f'(//label[normalize-space(text())="{PersonalDetails.TEST_FIELD.value}"]/following::input)[1]'
    MILITARY_SERVICE = f'(//label[normalize-space(text())="{PersonalDetails.MILITARY_SERVICE.value}"]/following::input)[1]'
    SMOKER_STATUS = f'(//label[normalize-space(text())="{PersonalDetails.SMOKER.value}"]/following::input)[1]'

    
