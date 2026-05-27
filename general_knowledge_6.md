# PIM Emergency Contacts Automation Walkthrough by Antigravity AI Agent

We have successfully implemented and verified the automation suite for the **Emergency Contacts** section under the PIM My Info page in OrangeHRM. It matches the exact design patterns, reliability principles, and conventions of the pre-existing test files in the repository.

---

## Changes Implemented

### 1. Constants Setup
* **File**: [my_info_constants.py](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py)
* **Additions**:
  * Created `EmergencyContacts` enum class defining target field labels (`Name`, `Relationship`, `Home Telephone`, `Mobile`, and `Work Telephone`).
  * Registered `EMERGENCY_CONTACTS_ENDPOINT = "**/emergency-contacts*"` under `Api_Endpoints` with a trailing wildcard to capture requests with query parameters (e.g. `?limit=50&offset=0`).

### 2. Locators Design
* **File**: [emergency_contacts_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/emergency_contacts_locators.py)
* **Selectors**:
  * Form input inputs targeted by text label sibling paths.
  * Robust row and cell locators wrapped inside XPath first-match wrappers `(...)[1]` to prevent strict mode violations in duplicate database environments.

### 3. Component Page Logic
* **File**: [emergency_contacts_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py)
* **Methods**:
  * `click_on_emergency_contacts_tab()`: Seamlessly navigates to the Emergency Contacts section.
  * `fetch_emergency_contacts_from_api()`: Navigates and intercepts the JSON response payload.
  * `verify_emergency_contacts_ui(response)`: Validates active emergency contact rows against the real backend payload keys (`homePhone`, `mobilePhone`, `officePhone`).
  * `add_emergency_contact(...)`: Fills the add-form fields and waits for the API response.
  * `delete_emergency_contact(name)`: Clicks delete, handles the dialog confirmation, and ensures changes are persisted before asserting the UI updates.

### 4. Automated Test Suite
* **File**: [test_emergency_contacts.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_emergency_contacts.py)
* **Tests**:
  * `test_emergency_contacts_ui_api_validation`: Standard UI-to-API data matching.
  * `test_add_and_verify_emergency_contact`: Performs the complete form filling workflow using a dynamically isolated contact name (`Contact_<epoch>`) to prevent run collisions, verifies successful persistence, and carries out clean UI-based deletion teardown to guarantee zero persistent side effects.

---

## Verification & Execution Results

The newly implemented test suite was executed sequentially locally:

```bash
venv/bin/pytest -n0 tests/orangehrm/components/pim/test_emergency_contacts.py
```

### Execution Log

```text
Executing Global Setup and It also sets up the dotenv files
============================= test session starts ==============================
platform darwin -- Python 3.14.4, pytest-8.4.2, pluggy-1.6.0
rootdir: /Users/arghajitsingha/playwright-python
configfile: pytest.ini
plugins: repeat-0.9.4, playwright-0.7.2, allure-pytest-2.16.0, xdist-3.8.0, pulse-report-1.0.1, metadata-3.1.1, html-4.2.0, smart-rerun-0.1.3, base-url-2.1.0, rerunfailures-16.1
collected 2 items

tests/orangehrm/components/pim/test_emergency_contacts.py ..             [100%]

Executing Global Teardown
PulseReport: JSON report written to /Users/arghajitsingha/playwright-python/pulse-report/playwright-pulse-report.json

============================== 2 passed in 56.89s ==============================
```

> [!TIP]
> **Key Technical Discoveries**:
> 1. **Query Param Glob Matching**: The page requests GET `**/emergency-contacts?limit=50&offset=0`. Adding a trailing wildcard `*` to the glob pattern ensures Playwright's `expect_response` captures it correctly.
> 2. **Emergency Contacts API Keys**: Unlike other components, the emergency contacts API uses `"homePhone"`, `"mobilePhone"`, and `"officePhone"`. Updating the component map to target these exact response keys resolved string mismatches.
> 3. **First-Match XPath Wrap**: By wrapping dynamic selectors inside `(...)[1]`, the locators are completely immune to strict mode violations even if duplicate test data exists in the test database environment.
