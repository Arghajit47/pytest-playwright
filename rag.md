# Playwright-Python RAG Context Model & Coding Standards

This document serves as the absolute, single source of truth for repository structure, configuration, design patterns, and coding standards. **Any AI agent modifying or writing code in this repository must strictly adhere to the guidelines and rules outlined in this document.**

---

## 1. CRITICAL DIRECTIVES FOR AI AGENTS (STRICT COMPLIANCE)

When adding or refactoring code in this repository, you **MUST** follow these rules without exception:
1. **Never Hardcode Selectors**: All locators must be defined in class-level variables inside the dedicated locators package (e.g., `locators/components/`).
2. **Never Hardcode Test Data or Magic Keys**: All keyboard interaction strings (e.g. `"ArrowDown"`, `"Enter"`), test remarks, URL patterns, or page tab texts must be declared inside constants modules (e.g. `constants/common_constants.py` or `constants/components/`).
3. **Do Not Redefine Core Fixtures**: Do not redefine `page`, `browser`, or `context` in `./conftest.py`. Doing so clashes with `pytest-playwright`'s internal event loop and causes `playwright._impl._errors.Error: It looks like you are using Playwright Sync API inside the asyncio loop`.
4. **Always Instrument Steps**: Every page action and test stage must be wrapped using the `pytest-pulse` framework via the `@step` decorator or `with pulse_step` context manager.
5. **Use Cookie Authentication for Speed**: Unless explicitly testing the login process itself, tests must use the `login_via_cookies` fixture to bypass UI login.
6. **No Direct Browser/Expect Calls in POM**: All page objects must route page interactions and assertion validations through `BasePage` methods (e.g. `self.base_page.press_key()`, `self.base_page.wait_for_timeout()`, `self.base_page.verify_page_url()`). Do not import `expect` or call page methods directly.
7. **Keep Test Files Clean**: Test files must only orchestrate high-level Page Object method calls and verify final outcomes. Move parameterizations, default values, and setup parameters inside Page Object wrapper functions.
8. **Prevent Strict Mode Violations**: Use `(...)[1]` wrapping on XPath selectors to extract the first match when targeting elements in dynamic, duplicate-heavy tables/grids.

---

## 2. Directory Mapping & Architecture

```bash
project-root/
├── .github/                  # GitHub Actions CI workflow (pytest.yml)
├── api/                      # Backend API client models
│   ├── base_api.py           # Core HTTP client wrapping Playwright RequestContext
│   └── orangehrm_api_auth.py # Dedicated requests session authentication client
├── constants/                # Test data, configuration maps, and API endpoints
│   ├── common_constants.py   # Global shared enums (e.g., Cookies)
│   ├── api_constants.py      # Repository-wide endpoint maps
│   ├── my_info_constants.py  # PIM section enums and selectors
│   └── components/           # Page-specific feature constants (leave, performance, etc.)
├── locators/                 # DOM selectors mapped as static classes (CSS / XPath)
│   ├── about_me_locators.py
│   ├── orangeHRM_login_locators.py
│   └── components/           # Component-specific element locators
├── pages/                    # Page Object Model (POM) page actions and assertions
│   ├── base_page.py          # Ancestor class holding wrapped Playwright assertions and utility methods
│   ├── orangeHRM_login_page.py
│   └── components/           # Page objects grouped by business domain (PIM, Leave, Claim, etc.)
├── tests/                    # Executable Pytest automation suites
│   ├── orangehrm/            # OrangeHRM UI & UI-API integration suites
│   │   ├── components/       # Feature-specific subdirectories (pim, leave, performance, etc.)
│   │   └── test_directory.py
│   ├── test_dummyjson_api.py # Pure backend API tests
│   └── test_flaky.py         # Flakiness demonstration and retry logic validation
├── conftest.py               # Session/function lifecycle fixtures and pytest hooks
├── pytest.ini                # Pytest command-line options and framework defaults
├── requirements.txt          # Python packaging manifest
└── .hermes_blueprint.md      # Hermes agent style guide and locator tokens
```

---

## 3. Directory Map & Component Linkages

For efficient RAG retrieval, use this registry to map page actions, locators, constants, and test cases:

### A. General & Common Pages
* **Core Base Page**: 
  - Page Class: [pages/base_page.py](./pages/base_page.py)
* **OrangeHRM Login**:
  - Page Class: [pages/orangeHRM_login_page.py](./pages/orangeHRM_login_page.py)
  - Locators: [locators/orangeHRM_login_locators.py](./locators/orangeHRM_login_locators.py)
  - Constants: [constants/login_page_constants.py](./constants/login_page_constants.py)
  - Test Suite: [tests/orangehrm/test_login.py](./tests/orangehrm/test_login.py)
* **Dashboard Main**:
  - Page Class: [pages/dashboard_page.py](./pages/dashboard_page.py)
  - Locators: [locators/dashboard_locators.py](./locators/dashboard_locators.py)
  - Constants: [constants/dashboard_page_constants.py](./constants/dashboard_page_constants.py)
  - Test Suite: [tests/orangehrm/test_dashboard.py](./tests/orangehrm/test_dashboard.py)
* **Directory Page**:
  - Page Class: [pages/directory_page.py](./pages/directory_page.py)
  - Locators: [locators/directory_locators.py](./locators/directory_locators.py)
  - Constants: [constants/directory_constants.py](./constants/directory_constants.py)
  - Test Suite: [tests/orangehrm/test_directory.py](./tests/orangehrm/test_directory.py)
* **About Me Section**:
  - Page Class: [pages/about_me_page.py](./pages/about_me_page.py)
  - Locators: [locators/about_me_locators.py](./locators/about_me_locators.py)
  - Constants: [constants/about_me_constants.py](./constants/about_me_constants.py)
  - Test Suite: [tests/orangehrm/test_about_me.py](./tests/orangehrm/test_about_me.py)

### B. OrangeHRM Component Pages

#### 1. Personal Information Management (PIM / My Info)
* **Personal Details**:
  - Page Component: [pages/components/my_info/personal_details_components.py](./pages/components/my_info/personal_details_components.py)
  - Locators: [locators/components/my_info/personal_details_locators.py](./locators/components/my_info/personal_details_locators.py)
  - Constants: [constants/my_info_constants.py](./constants/my_info_constants.py)
  - Test Suite: [tests/orangehrm/components/pim/test_personal_details.py](./tests/orangehrm/components/pim/test_personal_details.py)
* **Emergency Contacts**:
  - Page Component: [pages/components/my_info/emergency_contacts_components.py](./pages/components/my_info/emergency_contacts_components.py)
  - Locators: [locators/components/my_info/emergency_contacts_locators.py](./locators/components/my_info/emergency_contacts_locators.py)
  - Constants: [constants/my_info_constants.py](./constants/my_info_constants.py)
  - Test Suite: [tests/orangehrm/components/pim/test_emergency_contacts.py](./tests/orangehrm/components/pim/test_emergency_contacts.py)
* **Contact Details**:
  - Page Component: [pages/components/my_info/contact_details_components.py](./pages/components/my_info/contact_details_components.py)
  - Locators: [locators/components/my_info/contact_details_locators.py](./locators/components/my_info/contact_details_locators.py)
  - Constants: [constants/my_info_constants.py](./constants/my_info_constants.py)
  - Test Suite: [tests/orangehrm/components/pim/test_contact_details.py](./tests/orangehrm/components/pim/test_contact_details.py)

#### 2. Leave Management
* **Leave List**:
  - Page Component: [pages/components/leave/leave_list_page.py](./pages/components/leave/leave_list_page.py)
  - Locators: [locators/components/leave/leave_list_locators.py](./locators/components/leave/leave_list_locators.py)
  - Constants: [constants/components/leave/leave_list_constants.py](./constants/components/leave/leave_list_constants.py)
  - Test Suite: [tests/orangehrm/components/leave/test_leave_list.py](./tests/orangehrm/components/leave/test_leave_list.py)

#### 3. Recruitment Management
* **Candidates**:
  - Page Component: [pages/components/recruitment/candidates_page.py](./pages/components/recruitment/candidates_page.py)
  - Locators: [locators/components/recruitment/candidates_locators.py](./locators/components/recruitment/candidates_locators.py)
  - Constants: [constants/components/recruitment/candidates_constants.py](./constants/components/recruitment/candidates_constants.py)
  - Test Suite: [tests/orangehrm/components/recruitment/test_candidates.py](./tests/orangehrm/components/recruitment/test_candidates.py)

#### 4. Time Management & Timesheets
* **Timesheets**:
  - Page Component: [pages/components/time/timesheet_page.py](./pages/components/time/timesheet_page.py)
  - Locators: [locators/timesheet_locators.py](./locators/timesheet_locators.py)
  - Constants: [constants/components/time/time_sheet_constants.py](./constants/components/time/time_sheet_constants.py)
  - Test Suite: [tests/orangehrm/components/time/test_timesheet.py](./tests/orangehrm/components/time/test_timesheet.py)

#### 5. Claims Management
* **Assign Claim**:
  - Page Component: [pages/components/claim/assign_claim_page.py](./pages/components/claim/assign_claim_page.py) & [pages/components/claim/claim_components.py](./pages/components/claim/claim_components.py)
  - Locators: [locators/components/claim/claim_locators.py](./locators/components/claim/claim_locators.py)
  - Constants: [constants/components/claim/claim_constants.py](./constants/components/claim/claim_constants.py)
  - Test Suite: [tests/orangehrm/components/claim/test_assign_claim.py](./tests/orangehrm/components/claim/test_assign_claim.py)

#### 6. Performance Evaluation
* **Performance Reviews**:
  - Page Component: [pages/components/performance/performance_reviews_page.py](./pages/components/performance/performance_reviews_page.py)
  - Locators: [locators/components/performance/performance_reviews_locators.py](./locators/components/performance/performance_reviews_locators.py)
  - Constants: [constants/components/performance/performance_reviews_constants.py](./constants/components/performance/performance_reviews_constants.py)
  - Test Suite: [tests/orangehrm/components/performance/test_performance_reviews.py](./tests/orangehrm/components/performance/test_performance_reviews.py)

#### 7. Admin Panel Configuration
* **System User Filter**:
  - Page Component: [pages/components/admin/system_user_filter_components.py](./pages/components/admin/system_user_filter_components.py)
  - Locators: [locators/components/admin/system_user_filter_locators.py](./locators/components/admin/system_user_filter_locators.py)
  - Constants: [constants/components/admin/system_user_filter_constants.py](./constants/components/admin/system_user_filter_constants.py)
  - Test Suite: [tests/orangehrm/components/admin/test_admin_filter.py](./tests/orangehrm/components/admin/test_admin_filter.py)

#### 8. Dashboard Grid Cards
* **Leaves Summary**:
  - Page Component: [pages/components/dashboard/leaves_components.py](./pages/components/dashboard/leaves_components.py)
  - Locators: [locators/components/dashboard/leaves_locators.py](./locators/components/dashboard/leaves_locators.py)
  - Constants: [constants/components/dashboard/leaves_constants.py](./constants/components/dashboard/leaves_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_leaves.py](./tests/orangehrm/components/dashboard/test_leaves.py)
* **My Actions Summary**:
  - Page Component: [pages/components/dashboard/my_actions_components.py](./pages/components/dashboard/my_actions_components.py)
  - Locators: [locators/components/dashboard/my_actions_locators.py](./locators/components/dashboard/my_actions_locators.py)
  - Constants: [constants/components/dashboard/my_actions_constants.py](./constants/components/dashboard/my_actions_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_my_actions.py](./tests/orangehrm/components/dashboard/test_my_actions.py)
* **Locations Summary**:
  - Page Component: [pages/components/dashboard/location_components.py](./pages/components/dashboard/location_components.py)
  - Locators: [locators/components/dashboard/location_locators.py](./locators/components/dashboard/location_locators.py)
  - Constants: [constants/components/dashboard/locations_constants.py](./constants/components/dashboard/locations_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_location.py](./tests/orangehrm/components/dashboard/test_location.py)
* **Quick Launch Items**:
  - Page Component: [pages/components/dashboard/quick_launch_components.py](./pages/components/dashboard/quick_launch_components.py)
  - Locators: [locators/components/dashboard/quick_launch_locators.py](./locators/components/dashboard/quick_launch_locators.py)
  - Constants: [constants/components/dashboard/quick_launch_constants.py](./constants/components/dashboard/quick_launch_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_quick_launch.py](./tests/orangehrm/components/dashboard/test_quick_launch.py)
* **Latest Buzz Posts**:
  - Page Component: [pages/components/dashboard/latest_posts_components.py](./pages/components/dashboard/latest_posts_components.py)
  - Locators: [locators/components/dashboard/latest_posts_locators.py](./locators/components/dashboard/latest_posts_locators.py)
  - Constants: [constants/components/dashboard/latest_posts_constants.py](./constants/components/dashboard/latest_posts_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_latest_posts.py](./tests/orangehrm/components/dashboard/test_latest_posts.py)
* **Help Overlay**:
  - Page Component: [pages/components/dashboard/help_components.py](./pages/components/dashboard/help_components.py)
  - Locators: [locators/components/dashboard/help_locators.py](./locators/components/dashboard/help_locators.py)
  - Constants: [constants/components/dashboard/help_constants.py](./constants/components/dashboard/help_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_help.py](./tests/orangehrm/components/dashboard/test_help.py)
* **Subunit Summary**:
  - Page Component: [pages/components/dashboard/subunit_components.py](./pages/components/dashboard/subunit_components.py)
  - Locators: [locators/components/dashboard/subunit_locators.py](./locators/components/dashboard/subunit_locators.py)
  - Constants: [constants/components/dashboard/subunits_constants.py](./constants/components/dashboard/subunits_constants.py)
  - Test Suite: [tests/orangehrm/components/dashboard/test_subunit.py](./tests/orangehrm/components/dashboard/test_subunit.py)

---

## 4. Fixture Registry (`conftest.py`)

All shared fixtures are defined in [conftest.py](./conftest.py):

| Fixture Name | Scope | Description |
| :--- | :--- | :--- |
| `login` | `function` | Performs UI-based login on OrangeHRM, verifying the logo and fetching demo credentials. |
| `logout` | `function` | Teardown fixture that clicks the user profile dropdown and signs out of OrangeHRM. |
| `login_via_api` | `function` | Hits the OrangeHRM backend validate endpoint directly using Python `requests` to fetch the authenticated session cookie. |
| `login_via_cookies` | `function` | Injects the cookie value retrieved by `login_via_api` into the Playwright browser context, bypassing UI login for ultra-fast execution. |
| `request_setup` | `function` | Instantiates and disposes of a Playwright `RequestContext` for API interactions. |
| `base_api_setup` | `function` | Returns a `BaseAPI` instance powered by `request_setup`. |
| `authentication_token` | `function` | Logs into the dummyjson API and returns the access token. |
| `api_client` | `function` | Simple alias returning the instantiated API helper instance. |
| `employee_data` | `function` | Returns common test data (e.g., `{"employee_name": "Peter Mac Anderson"}`). |

---

## 5. Coding Standards & Implementation Rules

### A. Page Object Class Design
1. **Inheritance & Helpers**: Page classes representing main landing pages must inherit from `BasePage`. Page classes representing sub-sections or side tabs can either inherit or act as independent components.
2. **Initialization**: Page objects must initialize `self.base_page = BasePage(page)` and optionally `self.ui_helper = UIHelpers(page)` in their constructor to access wrapped Playwright assertions.
   ```python
   # Example constructor
   class PersonalDetailsComponent:
       def __init__(self, page) -> None:
           self.page = page
           self.base_page = BasePage(page)
           self.ui_helper = UIHelpers(page)
   ```

### B. Selector Hygiene & Design Tokens
1. **No Inline Selectors**: Keep POM classes clean. Selectors must be fetched from the `locators` package.
2. **Button tokens**:
   - **Active Actions (Search, Save, Add)**: Always use the `.oxd-button--secondary` class:
     `button.oxd-button--secondary:has-text('Save')`
   - **Neutral Actions (Cancel, Reset)**: Always use the `.oxd-button--ghost` class:
     `button.oxd-button--ghost:has-text('Reset')`
3. **Dropdown Containers**: The select input boxes use `.oxd-select-text`, NOT `.oxd-select-text-container`.
4. **Dropdown Options Selection**: Active dropdown list items use `.oxd-select-option`.
5. **No Native `<table>` Elements**: OrangeHRM lists use CSS-styled `div`s. Locate results tables using `.oxd-table` (do not combine with tag names like `table.oxd-table`).
6. **Empty Grid States**: Check for `"//span[text()='No Records Found']"` to verify empty listings.

### C. Autocomplete Fields
Autocomplete input boxes require deliberate input latency to trigger AJAX search hints, combined with Escape keypresses to handle "no-result" blurring.
- **Recipe**:
  ```python
  def autocomplete_dropdown(self, locator, text):
      autocomplete_input = self.page.locator(locator)
      autocomplete_input.click()
      autocomplete_input.press_sequentially(text, delay=100) # delay triggers AJAX
      
      dropdown = self.page.locator(".oxd-autocomplete-dropdown")
      target_option = dropdown.get_by_text(text).first
      try:
          expect(target_option).to_be_visible(timeout=3000)
          target_option.click()
      except AssertionError:
          print("Option not found, escaping dropdown overlay.")
          autocomplete_input.press("Escape") # closes overlay to restore focus
  ```

### D. Step Instrumentation & Metadata
Every test run is indexed by the reporting engine. You must explicitly tag and step-decorate your test structures.
1. **Decorators**: Use `@pytest.mark.pulse_severity("High"|"Medium"|"Critical"|"Low")` and `@pytest.mark.pulse_tag("Category")`.
2. **Title Steps**: Decorate test functions with `@step("Test description")`.
3. **Internal Phase Tracking**: Wrap test sections and page transitions in `with pulse_step("Description"):`.
   ```python
   @pytest.mark.pulse_severity("Medium")
   @pytest.mark.pulse_tag("PIM")
   @step("Verify Personal Details Page")
   def test_personal_details(page):
       with pulse_step("Instantiate Personal Details page component"):
           personal_details = PersonalDetailsComponent(page)
       with pulse_step("Fetch API data and validate UI values"):
           res = personal_details.fetch_employee_details_from_api()
           personal_details.validate_employee_details(res)
   ```

### E. API Interception & Verification
Verify UI actions using live API intercepts to make tests immune to database differences.
1. **Method Interception**: Use `wait_for_api_call` to wrap clicks that trigger network requests:
   ```python
   response = self.base_page.wait_for_api_call(
       lambda: self.click(LeaveListLocators.SEARCH_BUTTON),
       LeaveListConstants.LEAVE_REQUESTS_URL
   )
   ```
2. **Adaptive Assertions**: Use the metadata from the returned JSON response to dynamically check visible elements:
   ```python
   if response["meta"]["total"] > 0:
       self.verify_element_is_visible(LeaveListLocators.RESULTS_TABLE)
   else:
       self.verify_element_is_visible(LeaveListLocators.NO_RECORDS_TEXT)
   ```

---

## 6. Execution Configurations (`pytest.ini`)

Configured options located in [pytest.ini](./pytest.ini):
- **Headless Mode**: `--headless` is active by default.
- **Trace & Artifact Capture**: Traces are recorded (`--trace=on`), screenshots are taken on failure (`--screenshot=on`), and videos are saved (`--video=on`).
- **Execution Speed**: `--slowmo=200` is active to buffer interactions.
- **Reports**: Exports inline HTML report to `reports/report.html`.

---

## 7. RAG Code Recipes

Use these recipes as structural starting points when creating new automation components.

### A. Template: Locators Class
```python
# locators/components/feature_locators.py
class FeatureLocators:
    PAGE_TITLE = ".oxd-text--h5:has-text('Feature Name')"
    INPUT_FIELD = "//label[contains(text(), 'Field Label')]/following::input[1]"
    STATUS_DROPDOWN = "//label[contains(text(), 'Status')]/following::div[contains(@class, 'oxd-select-text')]"
    SAVE_BUTTON = "button.oxd-button--secondary:has-text('Save')"
    CANCEL_BUTTON = "button.oxd-button--ghost:has-text('Cancel')"
    
    # Lambda locator helper for dropdown option
    DROPDOWN_OPTION = lambda option_text: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option_text}')]"
```

### B. Template: Page Object Class
```python
# pages/components/feature_page.py
from pages.base_page import BasePage
from locators.components.feature_locators import FeatureLocators
from constants.components.feature_constants import FeatureConstants
from pytest_pulse import pulse_step, step

class FeaturePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    @step("Fill form and submit")
    def submit_feature_form(self, input_val: str, status: str):
        with pulse_step("Fill input field"):
            self.base_page.fill(FeatureLocators.INPUT_FIELD, input_val)
        with pulse_step("Select dropdown option"):
            self.base_page.click(FeatureLocators.STATUS_DROPDOWN)
            self.base_page.click(FeatureLocators.DROPDOWN_OPTION(status))
            
        # Intercept and return the backend API response payload
        response = self.base_page.wait_for_api_call(
            lambda: self.base_page.click(FeatureLocators.SAVE_BUTTON),
            FeatureConstants.FEATURE_SUBMIT_API_URL
        )
        self.base_page.wait_for_fully_page_loaded()
        return response
```

### C. Template: Test Case File
```python
# tests/orangehrm/components/test_feature.py
import pytest
from pages.components.feature_page import FeaturePage
from pytest_pulse import pulse_step, step

# Automatically apply cookie authentication to bypass UI login
pytestmark = pytest.mark.usefixtures("login_via_cookies")

@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("FeatureTag")
@step("Test Feature submission workflow")
def test_feature_submission(page):
    with pulse_step("Initialize Feature Page Object"):
        feature_page = FeaturePage(page)
        
    with pulse_step("Submit form and verify dynamic response"):
        response = feature_page.submit_feature_form("Test Input", "Enabled")
        
        # Verify response metadata
        assert response["data"]["status"] == "success"
```
