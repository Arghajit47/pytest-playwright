from playwright.sync_api import Page
from locators.components.dashboard.help_locators import HelpLocators
from constants.components.dashboard.help_constants import HelpConstants
from pages.base_page import BasePage
from pytest_pulse import step

class HelpComponents(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)

    @step("Click on the help button")
    def click_help_button(self):
        self.base_page.waitForFullyPageLoad()
        self.click_element(HelpLocators.HELP_BUTTON)
        
    @step("Verify help icon is visible")
    def verify_help_icon_is_visible(self):
        self.base_page.waitForFullyPageLoad()
        self.base_page.verify_element_is_visible(HelpLocators.HELP_ICON)
    
    @step("Verify help url")
    def verify_help_url(self):
        self.base_page.waitForFullyPageLoad()
        self.base_page.verify_url(HelpConstants.HELP_URL)