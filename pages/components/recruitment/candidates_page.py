from pages.base_page import BasePage
from locators.components.recruitment.candidates_locators import RecruitmentCandidatesLocators
from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants
from pytest_pulse import pulse_step, step

class RecruitmentCandidatesPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    @step("Navigate to Recruitment Candidates via Side Panel")
    def navigate_via_menu(self):
        with pulse_step(f"Click on '{RecruitmentCandidatesConstants.SIDE_PANEL_MENU}' menu in side panel"):
            self.click(RecruitmentCandidatesLocators.RECRUITMENT_OPTION)

    def verify_page_loaded(self):
        with pulse_step("Verifying Recruitment Candidates page is loaded"):
            self.verify_element_is_visible(RecruitmentCandidatesLocators.PAGE_TITLE)

    @step("Fetch candidates list from API")
    def fetch_candidates_data(self):
        response = self.base_page.wait_for_api_call(
            lambda: self.navigate_via_menu(),
            RecruitmentCandidatesConstants.CANDIDATES_REQUESTS_URL
        )
        self.base_page.wait_for_fully_page_loaded()
        return response

    def filter_candidates(self, job_title=None, vacancy=None, hiring_manager=None, status=None, candidate_name=None, keywords=None, date_from=None, date_to=None, method=None):
        with pulse_step("Filtering candidates with provided criteria"):
            if job_title:
                self.click(RecruitmentCandidatesLocators.JOB_TITLE_DROPDOWN)
                self.click(RecruitmentCandidatesLocators.DROPDOWN_OPTIONS(job_title))
            if vacancy:
                self.click(RecruitmentCandidatesLocators.VACANCY_DROPDOWN)
                self.click(RecruitmentCandidatesLocators.DROPDOWN_OPTIONS(vacancy))
            if hiring_manager:
                self.click(RecruitmentCandidatesLocators.HIRING_MANAGER_DROPDOWN)
                self.click(RecruitmentCandidatesLocators.DROPDOWN_OPTIONS(hiring_manager))
            if status:
                self.click(RecruitmentCandidatesLocators.STATUS_DROPDOWN)
                self.click(RecruitmentCandidatesLocators.DROPDOWN_OPTIONS(status))
            if candidate_name:
                self.autocomplete_dropdown(RecruitmentCandidatesLocators.CANDIDATE_NAME, candidate_name)
            if keywords:
                self.fill(RecruitmentCandidatesLocators.KEYWORDS, keywords)
            if date_from:
                self.fill(RecruitmentCandidatesLocators.DATE_FROM, date_from)
            if date_to:
                self.fill(RecruitmentCandidatesLocators.DATE_TO, date_to)
            if method:
                self.click(RecruitmentCandidatesLocators.METHOD_DROPDOWN)
                self.click(RecruitmentCandidatesLocators.DROPDOWN_OPTIONS(method))
            
            response = self.base_page.wait_for_api_call(
                lambda: self.click(RecruitmentCandidatesLocators.SEARCH_BUTTON),
                RecruitmentCandidatesConstants.CANDIDATES_REQUESTS_URL
            )
            self.base_page.wait_for_fully_page_loaded()
            return response


    def reset_filters(self):
        with pulse_step("Resetting candidate filters"):
            self.click(RecruitmentCandidatesLocators.RESET_BUTTON)

    def verify_no_records_found(self, response):
        with pulse_step("Verifying no records found based on API response"):
            if response["meta"]["total"] == 0:
                self.verify_element_is_visible(RecruitmentCandidatesLocators.NO_RECORDS_TEXT)

    def verify_records_exist(self, response):
        with pulse_step("Verifying candidates exist based on API response"):
            if response["meta"]["total"] > 0:
                self.verify_element_is_visible(RecruitmentCandidatesLocators.RESULTS_TABLE)
                self.verify_element_is_not_visible(RecruitmentCandidatesLocators.NO_RECORDS_TEXT)
            else:
                self.verify_element_is_visible(RecruitmentCandidatesLocators.NO_RECORDS_TEXT)
                self.verify_element_is_not_visible(RecruitmentCandidatesLocators.RESULTS_TABLE)

    def verify_candidate_reset(self, locator, value):
        with pulse_step(f"Verifying filter reset for {locator}"):
            current_val = self.base_page.get_attribute(locator, "value") or ""
            self.base_page.verify_equal(current_val, value or "")

    def get_record_count_text(self):
        with pulse_step("Fetching record count text"):
            return self.get_element_inner_text(RecruitmentCandidatesLocators.RECORD_COUNT_TEXT)
