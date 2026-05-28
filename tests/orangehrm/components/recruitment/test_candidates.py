from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants
import pytest
from pages.components.recruitment.candidates_page import RecruitmentCandidatesPage
from locators.components.recruitment.candidates_locators import RecruitmentCandidatesLocators
from pytest_pulse import pulse_step, step

@pytest.mark.usefixtures("login", "logout")
@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Recruitment")
@step("Test to verify that filtering with non-existent data correctly displays 'No Records Found' message in Recruitment Candidates list.")
def test_recruitment_candidates_no_records_with_random_filter(page):
    candidates_page = RecruitmentCandidatesPage(page)
    
    with pulse_step("Navigate to Recruitment Candidates page via menu"):
        response = candidates_page.fetch_candidates_data()
        candidates_page.verify_page_loaded()
    
    with pulse_step("Apply filters with non-existent keyword"):
        filtered_response = candidates_page.filter_candidates(
            keywords=RecruitmentCandidatesConstants.TEST_CANDIDATE_NAME
        )
    
    with pulse_step("Verify 'No Records Found' message is displayed"):
        candidates_page.verify_no_records_found(filtered_response)


@pytest.mark.usefixtures("login", "logout")
@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Recruitment")
@step("Test to verify that the reset button clears applied filters on the Recruitment Candidates page.")
def test_recruitment_candidates_reset_filters(page):
    candidates_page = RecruitmentCandidatesPage(page)
    
    with pulse_step("Navigate to Recruitment Candidates page via menu"):
        candidates_page.fetch_candidates_data()
    
    baseline_keywords = page.locator(RecruitmentCandidatesLocators.KEYWORDS).get_attribute("value") or ""
    
    with pulse_step("Apply a specific keyword filter"):
        candidates_page.filter_candidates(
            keywords=RecruitmentCandidatesConstants.TEST_RESET_NAME
        )
    
    with pulse_step("Resetting all recruitment filters"):
        candidates_page.reset_filters()
    
    candidates_page.verify_candidate_reset(
        RecruitmentCandidatesLocators.KEYWORDS, 
        baseline_keywords
    )
