from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants

class RecruitmentCandidatesLocators:
    # Side panel locators
    RECRUITMENT_OPTION = (
        f"//li//a//span[text()='{RecruitmentCandidatesConstants.SIDE_PANEL_MENU}']"
    )
    # Top navigation bar locators
    CANDIDATES_LINK = f"//a[text()='{RecruitmentCandidatesConstants.TOP_NAV_LINK}']"

    # Header
    PAGE_TITLE = ".oxd-text--h5:has-text('Candidates')"
    
    # Filter Fields
    JOB_TITLE_DROPDOWN = "//label[contains(text(), 'Job Title')]/following::div[contains(@class, 'oxd-select-text')]"
    VACANCY_DROPDOWN = "//label[contains(text(), 'Vacancy')]/following::div[contains(@class, 'oxd-select-text')]"
    HIRING_MANAGER_DROPDOWN = "//label[contains(text(), 'Hiring Manager')]/following::div[contains(@class, 'oxd-select-text')]"
    STATUS_DROPDOWN = "//label[contains(text(), 'Status')]/following::div[contains(@class, 'oxd-select-text')]"
    CANDIDATE_NAME = "//label[contains(text(), 'Candidate Name')]/following::input[1]"
    KEYWORDS = "//label[contains(text(), 'Keywords')]/following::input[1]"
    DATE_FROM = "//label[contains(text(), 'Date of Application')]/following::input[1]"
    DATE_TO = "//label[contains(text(), 'Date of Application')]/following::input[2]"
    METHOD_DROPDOWN = "//label[contains(text(), 'Method of Application')]/following::div[contains(@class, 'oxd-select-text')]"
    
    # Buttons
    RESET_BUTTON = "button.oxd-button--ghost:has-text('Reset')"
    SEARCH_BUTTON = "button.oxd-button--secondary:has-text('Search')"
    ADD_BUTTON = "button.oxd-button--secondary:has-text('Add')"
    
    # Results Table
    RESULTS_TABLE = ".oxd-table"
    RECORD_COUNT_TEXT = ".oxd-text--body:has-text('Records Found')"
    NO_RECORDS_TEXT = "//span[text()='No Records Found']"
    TABLE_HEADER_CANDIDATE = "th:has-text('Candidate')"
    TABLE_HEADER_STATUS = "th:has-text('Status')"

    # Filter dropdown options
    DROPDOWN_OPTIONS = lambda option: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"
