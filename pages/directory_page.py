import re
from playwright.sync_api import expect
from pytest_pulse import pulse_step
from constants.directory_constants import DirectoryConstants
from locators.directory_locators import DirectoryPageLocators
from utils.ui_helpers import UIHelpers
from pages.base_page import BasePage
from pytest_pulse import step


class DirectoryPage:
    def __init__(self, page):
        self.page = page
        self.base_page = BasePage(page)
        self.ui_helper = UIHelpers(page)

    @step("Navigate to directory page")
    def navigate_to_directory_page(self):
        with pulse_step("Click on directory option"):
            self.base_page.click(DirectoryPageLocators.DIRECTORY_OPTION)
        with pulse_step("Verify directory page url"):
            self.base_page.verify_page_url(DirectoryConstants.DIRECTORY_PAGE_URL)
        with pulse_step("Verify directory page header text"):
            self.base_page.verify_element_text(
                DirectoryPageLocators.DIRECTORY_PAGE_HEADER_TITLE,
                DirectoryConstants.DIRECTORY_OPTION_TEXT,
            )
        with pulse_step("Verify directory page header"):
            self.base_page.verify_element_text(
                DirectoryPageLocators.DIRECTORY_PAGE_HEADER,
                DirectoryConstants.DIRECTORY_OPTION_TEXT,
            )

    @step("Search employee by name")
    def search_employee_by_name(self, name):
        with pulse_step("Autocomplete dropdown"):
            self.base_page.autocomplete_dropdown(
                DirectoryPageLocators.EMPLOYEE_NAME_DROPDOWN, name
            )
            self.page.wait_for_timeout(1000)

    @step("Select dropdown for job title")
    def select_dropdown_for_job_title(self, job_title):
        with pulse_step("Click on job title dropdown"):
            self.base_page.click(DirectoryPageLocators.SELECT_DROPDOWN)
        with pulse_step(
            "Verify dropdown list visible and Select job title from dropdown"
        ):
            self.base_page.verify_element_is_visible(
                DirectoryPageLocators.DROPDOWN_SELECT_OPTION
            )
            self.base_page.click(DirectoryPageLocators.DROPDOWN_OPTIONS(job_title))
        with pulse_step("Wait for dropdown to close"):
            self.page.wait_for_timeout(1000)

    @step("Select dropdown for location")
    def select_dropdown_for_location(self, location_name):
        with pulse_step("Click on location dropdown"):
            self.base_page.click(DirectoryPageLocators.SELECT_DROPDOWN, 1)
        with pulse_step(
            "Verify dropdown list visible and Select location from dropdown"
        ):
            self.base_page.verify_element_is_visible(
                DirectoryPageLocators.DROPDOWN_SELECT_OPTION
            )
            self.base_page.click(DirectoryPageLocators.DROPDOWN_OPTIONS(location_name))
        with pulse_step("Wait for dropdown to close"):
            self.page.wait_for_timeout(1000)

    @step("Reset search form")
    def reset_search_form(self):
        self.base_page.click(DirectoryPageLocators.RESET_BUTTON)

    @step("Click search button")
    def click_search_button(self):
        self.base_page.click(DirectoryPageLocators.SEARCH_BUTTON)

    @step("Get live directory data")
    def get_live_directory_data(self) -> list:
        """
        Navigates to the directory page, captures the live API response,
        and returns the list of employee data dictionaries.
        """

        response = self.base_page.wait_for_api_call(
            lambda: self.base_page.navigateToUrl(DirectoryConstants.DIRECTORY_PAGE_URL),
            DirectoryConstants.API_PATTERN,
        )
        return response.get("data", [])

    def verify_single_employee_card(self, employee):
        """
        Takes a single employee's live API data and verifies
        that their specific UI card renders perfectly, including conditional fields.
        """
        # 1. Name Formatting
        first = employee.get("firstName") or ""
        middle = employee.get("middleName") or ""
        last = employee.get("lastName") or ""
        expected_full_name = " ".join(
            [n.strip() for n in [first, middle, last] if n and n.strip()]
        )
        self.base_page.verify_directory_card(
            expected_full_name=expected_full_name,
            emp_number=employee.get("empNumber"),
            live_job_title=employee.get("jobTitle", {}).get("title"),
            live_subunit=employee.get("subunit", {}).get("name"),
            live_location=employee.get("location", {}).get("name"),
            card_locator_str=DirectoryPageLocators.DIRECTORY_CARD,
            profile_img_locator_str=DirectoryPageLocators.PROFILE_PICTURE,
            job_title_locator_str=DirectoryPageLocators.CARD_SUBTITLE,
            card_body_locator_str=DirectoryPageLocators.CARD_BODY,
            description_locator_str=DirectoryPageLocators.CARD_DESCRIPTION,
        )

    def verify_employee_details_with_api_data(self, live_employees):
        self.base_page.verify_element_is_visible(
            DirectoryPageLocators.MEMBER_CARD_CONTAINER
        )
        for employee in live_employees:
            with pulse_step("Verify single employee card"):
                self.verify_single_employee_card(employee)
