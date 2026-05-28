from playwright.sync_api import Page, expect
from locators.components.dashboard.help_locators import HelpLocators
from constants.components.dashboard.help_constants import HelpConstants
from pages.base_page import BasePage
from pytest_pulse import step

class HelpComponents(BasePage):
    def __init__(self, page: Page):
        self.page = page
        self.base_page = BasePage(page)
        self.new_page = None

    @step("Click on the help button")
    def click_help_button(self):
        self.base_page.wait_for_fully_page_loaded()
        with self.page.context.expect_page() as new_page_info:
            self.base_page.click(HelpLocators.HELP_BUTTON)
        self.new_page = new_page_info.value
        self.new_page.wait_for_load_state()
        
    @step("Verify help icon is visible")
    def verify_help_icon_is_visible(self):
        self.base_page.wait_for_fully_page_loaded()
        self.base_page.verify_element_is_visible(HelpLocators.HELP_ICON)
    
    @step("Verify help url")
    def verify_help_url(self):
        if self.new_page:
            expect(self.new_page).to_have_url(HelpConstants.HELP_URL)
            self.new_page.close()
        else:
            self.base_page.verify_page_url(HelpConstants.HELP_URL)