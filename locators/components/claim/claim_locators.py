from playwright.sync_api import Locator
from enum import Enum

class ClaimLocators:
    CLAIM_TAB = lambda name: f"//li//a//span[text()='{name}']"
    ASSIGN_CLAIM_SUB_MENU = lambda name: f"//nav[@role='navigation']//a[text()='{name}']"

    EMPLOYEE_NAME_INPUT = "//label[normalize-space(text())='Employee Name']/following::input[1]"
    EVENT_INPUT = "//label[normalize-space(text())='Event']/following::div[contains(@class, 'oxd-select-text')][1]"
    CURRENCY_INPUT = "//label[normalize-space(text())='Currency']/following::div[contains(@class, 'oxd-select-text')][1]"
    REMARKS_TEXTAREA = "//label[normalize-space(text())='Remarks']/following::textarea[1]"
    CREATE_BUTTON = "button[type='submit']"
    SUCCESS_MESSAGE = "div.oxd-toast.oxd-toast--success.oxd-toast-container"
    DROPDOWN_OPTION = lambda option: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"

