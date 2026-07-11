from constants.components.claim.claim_constants import ClaimConstants, ClaimEvent, ClaimCurrency, Api_Endpoints
from locators.components.claim.claim_locators import ClaimLocators
from pages.base_page import BasePage
from pytest_pulse import step, pulse_step
import re


class AssignClaimPage:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)

    @step("Click on Claim Tab")
    def click_on_claim_tab(self):
        with pulse_step("Click on Claim Tab"):
            self.base_page.verify_element_is_visible(ClaimLocators.CLAIM_TAB(ClaimConstants.CLAIM_TAB_TEXT))
            self.base_page.click(ClaimLocators.CLAIM_TAB(ClaimConstants.CLAIM_TAB_TEXT))
            self.base_page.wait_for_fully_page_loaded()
            self.base_page.strict_wait()    

    @step("Navigate to Assign Claim page")
    def navigate_to_assign_claim_page(self):
        self.click_on_claim_tab()
        with pulse_step("Click on Assign Claim sub-menu"):
            self.base_page.click(ClaimLocators.ASSIGN_CLAIM_SUB_MENU(ClaimConstants.ASSIGN_CLAIM_TAB_TEXT))
        self.base_page.wait_for_fully_page_loaded()

    @step("Assign valid claim with default data")
    def assign_valid_claim(self):
        self.assign_claim(
            employee_name=ClaimConstants.TEST_EMPLOYEE_NAME,
            event=ClaimEvent.TRAVEL_ALLOWANCE,
            currency=ClaimCurrency.EURO,
            remarks=ClaimConstants.TEST_REMARKS
        )


    @step("Assign Claim")
    def assign_claim(
        self, employee_name, event: ClaimEvent, currency: ClaimCurrency, remarks=None
    ):
        with pulse_step(f"Assigning claim for {employee_name}"):
            self.base_page.autocomplete_dropdown(ClaimLocators.EMPLOYEE_NAME_INPUT, employee_name)

            self.base_page.click(ClaimLocators.EVENT_INPUT)
            self.base_page.click(ClaimLocators.DROPDOWN_OPTION(event.value))

            self.base_page.click(ClaimLocators.CURRENCY_INPUT)
            self.base_page.click(ClaimLocators.DROPDOWN_OPTION(currency.value))

            if remarks:
                self.base_page.fill(ClaimLocators.REMARKS_TEXTAREA, remarks)

            self.base_page.wait_for_api_call(
                lambda: self.base_page.click(ClaimLocators.CREATE_BUTTON),
                Api_Endpoints.CLAIM_ENDPOINT.value
            )
            self.base_page.wait_for_fully_page_loaded()


    @step("Verify claim assignment success message")
    def verify_claim_assignment_success_message(self):
        with pulse_step("Verify redirected to details page url"):
            self.base_page.verify_page_url(re.compile(ClaimConstants.CLAIM_DETAILS_URL_PATTERN))



