# Repository Codebase RAG Context Reference Model

This document provides a complete, structured mapping of all code components in the repository, 
including classes, methods, functions, variables, and imports. Use it as a context model for RAG.

## Table of Contents

- [Core & Fixtures](#core--fixtures)
  - [conftest.py](#conftestpy)
  - [first_test.py](#first_testpy)
  - [test_sample.py](#test_samplepy)
- [API Client Models](#api-client-models)
  - [api/base_api.py](#apibase_apipy)
  - [api/orangehrm_api_auth.py](#apiorangehrm_api_authpy)
- [Constants](#constants)
  - [constants/about_me_constants.py](#constantsabout_me_constantspy)
  - [constants/api_constants.py](#constantsapi_constantspy)
  - [constants/common_constants.py](#constantscommon_constantspy)
  - [constants/components/admin/system_user_filter_constants.py](#constantscomponentsadminsystem_user_filter_constantspy)
  - [constants/components/claim/claim_constants.py](#constantscomponentsclaimclaim_constantspy)
  - [constants/components/dashboard/help_constants.py](#constantscomponentsdashboardhelp_constantspy)
  - [constants/components/dashboard/latest_posts_constants.py](#constantscomponentsdashboardlatest_posts_constantspy)
  - [constants/components/dashboard/leaves_constants.py](#constantscomponentsdashboardleaves_constantspy)
  - [constants/components/dashboard/locations_constants.py](#constantscomponentsdashboardlocations_constantspy)
  - [constants/components/dashboard/my_actions_constants.py](#constantscomponentsdashboardmy_actions_constantspy)
  - [constants/components/dashboard/quick_launch_constants.py](#constantscomponentsdashboardquick_launch_constantspy)
  - [constants/components/dashboard/subunits_constants.py](#constantscomponentsdashboardsubunits_constantspy)
  - [constants/components/leave/leave_list_constants.py](#constantscomponentsleaveleave_list_constantspy)
  - [constants/components/performance/performance_reviews_constants.py](#constantscomponentsperformanceperformance_reviews_constantspy)
  - [constants/components/recruitment/candidates_constants.py](#constantscomponentsrecruitmentcandidates_constantspy)
  - [constants/components/time/time_sheet_constants.py](#constantscomponentstimetime_sheet_constantspy)
  - [constants/dashboard_page_constants.py](#constantsdashboard_page_constantspy)
  - [constants/directory_constants.py](#constantsdirectory_constantspy)
  - [constants/login_page_constants.py](#constantslogin_page_constantspy)
  - [constants/my_info_constants.py](#constantsmy_info_constantspy)
- [Locators](#locators)
  - [locators/about_me_locators.py](#locatorsabout_me_locatorspy)
  - [locators/components/admin/system_user_filter_locators.py](#locatorscomponentsadminsystem_user_filter_locatorspy)
  - [locators/components/claim/claim_locators.py](#locatorscomponentsclaimclaim_locatorspy)
  - [locators/components/dashboard/help_locators.py](#locatorscomponentsdashboardhelp_locatorspy)
  - [locators/components/dashboard/latest_posts_locators.py](#locatorscomponentsdashboardlatest_posts_locatorspy)
  - [locators/components/dashboard/leaves_locators.py](#locatorscomponentsdashboardleaves_locatorspy)
  - [locators/components/dashboard/location_locators.py](#locatorscomponentsdashboardlocation_locatorspy)
  - [locators/components/dashboard/my_actions_locators.py](#locatorscomponentsdashboardmy_actions_locatorspy)
  - [locators/components/dashboard/quick_launch_locators.py](#locatorscomponentsdashboardquick_launch_locatorspy)
  - [locators/components/dashboard/subunit_locators.py](#locatorscomponentsdashboardsubunit_locatorspy)
  - [locators/components/leave/leave_list_locators.py](#locatorscomponentsleaveleave_list_locatorspy)
  - [locators/components/my_info/contact_details_locators.py](#locatorscomponentsmy_infocontact_details_locatorspy)
  - [locators/components/my_info/emergency_contacts_locators.py](#locatorscomponentsmy_infoemergency_contacts_locatorspy)
  - [locators/components/my_info/personal_details_locators.py](#locatorscomponentsmy_infopersonal_details_locatorspy)
  - [locators/components/performance/performance_reviews_locators.py](#locatorscomponentsperformanceperformance_reviews_locatorspy)
  - [locators/components/recruitment/candidates_locators.py](#locatorscomponentsrecruitmentcandidates_locatorspy)
  - [locators/dashboard_locators.py](#locatorsdashboard_locatorspy)
  - [locators/directory_locators.py](#locatorsdirectory_locatorspy)
  - [locators/orangeHRM_login_locators.py](#locatorsorangeHRM_login_locatorspy)
  - [locators/timesheet_locators.py](#locatorstimesheet_locatorspy)
- [Page Objects (POM)](#page-objects-pom)
  - [pages/about_me_page.py](#pagesabout_me_pagepy)
  - [pages/base_page.py](#pagesbase_pagepy)
  - [pages/components/admin/system_user_filter_components.py](#pagescomponentsadminsystem_user_filter_componentspy)
  - [pages/components/claim/assign_claim_page.py](#pagescomponentsclaimassign_claim_pagepy)
  - [pages/components/dashboard/help_components.py](#pagescomponentsdashboardhelp_componentspy)
  - [pages/components/dashboard/latest_posts_components.py](#pagescomponentsdashboardlatest_posts_componentspy)
  - [pages/components/dashboard/leaves_components.py](#pagescomponentsdashboardleaves_componentspy)
  - [pages/components/dashboard/location_components.py](#pagescomponentsdashboardlocation_componentspy)
  - [pages/components/dashboard/my_actions_components.py](#pagescomponentsdashboardmy_actions_componentspy)
  - [pages/components/dashboard/quick_launch_components.py](#pagescomponentsdashboardquick_launch_componentspy)
  - [pages/components/dashboard/subunit_components.py](#pagescomponentsdashboardsubunit_componentspy)
  - [pages/components/leave/leave_list_page.py](#pagescomponentsleaveleave_list_pagepy)
  - [pages/components/my_info/contact_details_components.py](#pagescomponentsmy_infocontact_details_componentspy)
  - [pages/components/my_info/emergency_contacts_components.py](#pagescomponentsmy_infoemergency_contacts_componentspy)
  - [pages/components/my_info/personal_details_components.py](#pagescomponentsmy_infopersonal_details_componentspy)
  - [pages/components/performance/performance_reviews_page.py](#pagescomponentsperformanceperformance_reviews_pagepy)
  - [pages/components/recruitment/candidates_page.py](#pagescomponentsrecruitmentcandidates_pagepy)
  - [pages/components/time/timesheet_page.py](#pagescomponentstimetimesheet_pagepy)
  - [pages/dashboard_page.py](#pagesdashboard_pagepy)
  - [pages/directory_page.py](#pagesdirectory_pagepy)
  - [pages/orangeHRM_login_page.py](#pagesorangeHRM_login_pagepy)
- [Pytest Suites](#pytest-suites)
  - [tests/orangehrm/components/admin/test_admin_filter.py](#testsorangehrmcomponentsadmintest_admin_filterpy)
  - [tests/orangehrm/components/claim/test_assign_claim.py](#testsorangehrmcomponentsclaimtest_assign_claimpy)
  - [tests/orangehrm/components/dashboard/test_help.py](#testsorangehrmcomponentsdashboardtest_helppy)
  - [tests/orangehrm/components/dashboard/test_latest_posts.py](#testsorangehrmcomponentsdashboardtest_latest_postspy)
  - [tests/orangehrm/components/dashboard/test_leaves.py](#testsorangehrmcomponentsdashboardtest_leavespy)
  - [tests/orangehrm/components/dashboard/test_location.py](#testsorangehrmcomponentsdashboardtest_locationpy)
  - [tests/orangehrm/components/dashboard/test_my_actions.py](#testsorangehrmcomponentsdashboardtest_my_actionspy)
  - [tests/orangehrm/components/dashboard/test_quick_launch.py](#testsorangehrmcomponentsdashboardtest_quick_launchpy)
  - [tests/orangehrm/components/dashboard/test_subunit.py](#testsorangehrmcomponentsdashboardtest_subunitpy)
  - [tests/orangehrm/components/leave/test_leave_list.py](#testsorangehrmcomponentsleavetest_leave_listpy)
  - [tests/orangehrm/components/performance/test_performance_reviews.py](#testsorangehrmcomponentsperformancetest_performance_reviewspy)
  - [tests/orangehrm/components/pim/test_contact_details.py](#testsorangehrmcomponentspimtest_contact_detailspy)
  - [tests/orangehrm/components/pim/test_emergency_contacts.py](#testsorangehrmcomponentspimtest_emergency_contactspy)
  - [tests/orangehrm/components/pim/test_personal_details.py](#testsorangehrmcomponentspimtest_personal_detailspy)
  - [tests/orangehrm/components/recruitment/test_candidates.py](#testsorangehrmcomponentsrecruitmenttest_candidatespy)
  - [tests/orangehrm/components/time/test_timesheet.py](#testsorangehrmcomponentstimetest_timesheetpy)
  - [tests/orangehrm/test_about_me.py](#testsorangehrmtest_about_mepy)
  - [tests/orangehrm/test_api.py](#testsorangehrmtest_apipy)
  - [tests/orangehrm/test_dashboard.py](#testsorangehrmtest_dashboardpy)
  - [tests/orangehrm/test_directory.py](#testsorangehrmtest_directorypy)
  - [tests/orangehrm/test_login.py](#testsorangehrmtest_loginpy)
  - [tests/test_dummyjson_api.py](#teststest_dummyjson_apipy)
  - [tests/test_fail.py](#teststest_failpy)
  - [tests/test_flaky.py](#teststest_flakypy)
  - [tests/test_pulse_report.py](#teststest_pulse_reportpy)
- [Utilities](#utilities)
  - [utils/ui_helpers.py](#utilsui_helperspy)

---

## Core & Fixtures

### `conftest.py` <a id='conftestpy'></a>

**Source File**: [conftest.py](file:///Users/arghajitsingha/playwright-python/conftest.py)

<details>
<summary>Imports</summary>

```python
from api.base_api import BaseAPI
from constants.api_constants import APIEndpoints
from api.orangehrm_api_auth import OrangeHRMAPI
from constants.common_constants import Cookies
from pages.base_page import BasePage
from pages import base_page
from constants.dashboard_page_constants import DashboardPageConstants
from pages.orangeHRM_login_page import LoginPage
pytest
os
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv
from pytest_pulse import pulse_step, step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`login`](file:///Users/arghajitsingha/playwright-python/conftest.py#L32) | `page` | - | - |
| [`logout`](file:///Users/arghajitsingha/playwright-python/conftest.py#L46) | `page` | - | - |
| [`login_via_cookies`](file:///Users/arghajitsingha/playwright-python/conftest.py#L55) | `page, login_via_api` | - | - |
| [`login_via_api`](file:///Users/arghajitsingha/playwright-python/conftest.py#L77) | `` | - | - |
| [`request_setup`](file:///Users/arghajitsingha/playwright-python/conftest.py#L87) | `playwright` | - | - |
| [`base_api_setup`](file:///Users/arghajitsingha/playwright-python/conftest.py#L97) | `request_setup` | - | - |
| [`authentication_token`](file:///Users/arghajitsingha/playwright-python/conftest.py#L104) | `request_setup, base_api_setup` | - | - |
| [`api_client`](file:///Users/arghajitsingha/playwright-python/conftest.py#L119) | `base_api_setup` | - | - |
| [`pytest_sessionstart`](file:///Users/arghajitsingha/playwright-python/conftest.py#L124) | `session` | - | Called after the Session object has been created and before performing collection and entering the run test loop. |
| [`pytest_sessionfinish`](file:///Users/arghajitsingha/playwright-python/conftest.py#L134) | `session, exitstatus` | - | Called after whole test run finished, right before returning the exit status to the system. |


---

### `first_test.py` <a id='first_testpy'></a>

**Source File**: [first_test.py](file:///Users/arghajitsingha/playwright-python/first_test.py)

<details>
<summary>Imports</summary>

```python
from playwright.sync_api import sync_playwright
```
</details>

---

### `test_sample.py` <a id='test_samplepy'></a>

**Source File**: [test_sample.py](file:///Users/arghajitsingha/playwright-python/test_sample.py)

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_example`](file:///Users/arghajitsingha/playwright-python/test_sample.py#L4) | `page` | - | - |


---

## API Client Models

### `api/base_api.py` <a id='apibase_apipy'></a>

**Source File**: [base_api.py](file:///Users/arghajitsingha/playwright-python/api/base_api.py)

<details>
<summary>Imports</summary>

```python
from pytest_pulse import step
```
</details>

#### Classes

##### class `BaseAPI`
Link: [BaseAPI](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L3)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L4) | `self, context_or_page` | - | - |
| [`_get_request_context`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L7) | `self, request_setup` | - | - |
| [`get_response`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L15) | `self, request_setup = None, url = None, headers = None, queryParams = None` | - | - |
| [`post_response`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L24) | `self, request_setup = None, url = None, headers = None, data = None` | - | - |
| [`delete_response`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L33) | `self, request_setup = None, url = None, headers = None` | - | - |
| [`put_response`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L45) | `self, request_setup = None, url = None, headers = None, data = None` | - | - |
| [`patch_response`](file:///Users/arghajitsingha/playwright-python/api/base_api.py#L54) | `self, request_setup = None, url = None, headers = None, data = None` | - | - |


---

### `api/orangehrm_api_auth.py` <a id='apiorangehrm_api_authpy'></a>

**Source File**: [orangehrm_api_auth.py](file:///Users/arghajitsingha/playwright-python/api/orangehrm_api_auth.py)

<details>
<summary>Imports</summary>

```python
requests
re
```
</details>

#### Classes

##### class `OrangeHRMAPI`
Link: [OrangeHRMAPI](file:///Users/arghajitsingha/playwright-python/api/orangehrm_api_auth.py#L4)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/api/orangehrm_api_auth.py#L5) | `self, base_url` | - | - |
| [`login`](file:///Users/arghajitsingha/playwright-python/api/orangehrm_api_auth.py#L14) | `self, username, password` | - | - |


---

## Constants

### `constants/about_me_constants.py` <a id='constantsabout_me_constantspy'></a>

**Source File**: [about_me_constants.py](file:///Users/arghajitsingha/playwright-python/constants/about_me_constants.py)

<details>
<summary>Imports</summary>

```python
from enum import Enum
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `ABOUT_ME_MODAL_HEADER_TEXT` | `'About'` |


#### Classes

##### class `AboutMeKeys(Enum)`
Link: [AboutMeKeys](file:///Users/arghajitsingha/playwright-python/constants/about_me_constants.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `COMPANY_NAME` | `'Company Name:'` |
| `VERSION` | `'Version:'` |
| `ACTIVE_EMPLOYEES` | `'Active Employees:'` |
| `EMPLOYEES_TERMINATED` | `'Employees Terminated:'` |

</details>

##### class `AboutMeAPIResponseKeys(Enum)`
Link: [AboutMeAPIResponseKeys](file:///Users/arghajitsingha/playwright-python/constants/about_me_constants.py#L14)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `COMPANY_NAME` | `'companyName'` |
| `PRODUCT_NAME` | `'productName'` |
| `VERSION` | `'version'` |
| `ACTIVE_EMPLOYEES` | `'numberOfActiveEmployee'` |
| `EMPLOYEES_TERMINATED` | `'numberOfPastEmployee'` |

</details>

---

### `constants/api_constants.py` <a id='constantsapi_constantspy'></a>

**Source File**: [api_constants.py](file:///Users/arghajitsingha/playwright-python/constants/api_constants.py)

#### Classes

##### class `APIEndpoints`
Link: [APIEndpoints](file:///Users/arghajitsingha/playwright-python/constants/api_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `USERS_ENDPOINT` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/admin/users?limit=50&offset=0&sortField=u.userName&so...` |
| `BASE_URL` | `'https://opensource-demo.orangehrmlive.com'` |
| `ACTION_ITEMS_ENDPOINT` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/action-summary'` |
| `SHORTCUTS_ENDPOINT` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/shortcuts'` |
| `DUMMYJSON_AUTHENTICATION_ENDPOINT` | `'https://dummyjson.com/auth/me'` |
| `DUMMYJSON_LOGIN_ENDPOINT` | `'https://dummyjson.com/auth/login'` |
| `ABOUT_ME_API_ENDPOINT` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/core/about'` |
| `DASHBOARD_LEAVES_ENDPOINT` | `lambda date: f'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/leaves?date={date}'` |
| `DASHBOARD_EMPLOYEE_SUBUNIT` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/subunit'` |
| `DASHBOARD_EMPLOYEE_BY_LOCATION` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/dashboard/employees/locations'` |
| `DASHBOARD_LATEST_POSTS` | `'https://opensource-demo.orangehrmlive.com/web/index.php/api/v2/buzz/feed?limit=5&offset=0&sortOrder=DESC&sortField=s...` |

</details>

---

### `constants/common_constants.py` <a id='constantscommon_constantspy'></a>

**Source File**: [common_constants.py](file:///Users/arghajitsingha/playwright-python/constants/common_constants.py)

<details>
<summary>Imports</summary>

```python
from enum import Enum
```
</details>

#### Classes

##### class `Attributes(Enum)`
Link: [Attributes](file:///Users/arghajitsingha/playwright-python/constants/common_constants.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `SRC` | `'src'` |
| `HREF` | `'href'` |

</details>

##### class `Cookies(Enum)`
Link: [Cookies](file:///Users/arghajitsingha/playwright-python/constants/common_constants.py#L9)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ORANGEHRM_COOKIE` | `'orangehrm'` |
| `ORANGEHRM_COOKIE_VALUE` | `'aj1pd2da3d30f7ogml1s75tah3'` |
| `ORANGEHRM_COOKIE_DOMAIN` | `'opensource-demo.orangehrmlive.com'` |
| `ORANGEHRM_COOKIE_PATH` | `'/web'` |
| `ORANGEHRM_COOKIE_HTTPONLY` | `True` |
| `ORANGEHRM_COOKIE_SECURE` | `True` |
| `ORANGEHRM_COOKIE_SAMESITE` | `'Lax'` |

</details>

##### class `Keys(Enum)`
Link: [Keys](file:///Users/arghajitsingha/playwright-python/constants/common_constants.py#L19)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ARROW_DOWN` | `'ArrowDown'` |
| `ENTER` | `'Enter'` |

</details>

---

### `constants/components/admin/system_user_filter_constants.py` <a id='constantscomponentsadminsystem_user_filter_constantspy'></a>

**Source File**: [system_user_filter_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/admin/system_user_filter_constants.py)

#### Classes

##### class `SystemUserFilterConstants`
Link: [SystemUserFilterConstants](file:///Users/arghajitsingha/playwright-python/constants/components/admin/system_user_filter_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ADMIN_OPTION_TEXT` | `'Admin'` |
| `ADMIN_PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers'` |

</details>

---

### `constants/components/claim/claim_constants.py` <a id='constantscomponentsclaimclaim_constantspy'></a>

**Source File**: [claim_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/claim/claim_constants.py)

<details>
<summary>Imports</summary>

```python
from enum import Enum
```
</details>

#### Classes

##### class `ClaimConstants`
Link: [ClaimConstants](file:///Users/arghajitsingha/playwright-python/constants/components/claim/claim_constants.py#L3)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `CLAIM_TAB_TEXT` | `'Claim'` |
| `ASSIGN_CLAIM_TAB_TEXT` | `'Assign Claim'` |
| `CLAIM_CREATE_SUCCESS_MESSAGE` | `'Successfully Saved'` |
| `TEST_REMARKS` | `'Business travel expenses'` |
| `CLAIM_DETAILS_URL_PATTERN` | `'.*/claim/assignClaim/id/\\d+'` |
| `TEST_EMPLOYEE_NAME` | `'Peter Mac Anderson'` |

</details>

##### class `ClaimEvent(Enum)`
Link: [ClaimEvent](file:///Users/arghajitsingha/playwright-python/constants/components/claim/claim_constants.py#L13)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `TRAVEL_ALLOWANCE` | `'Travel Allowance'` |
| `ACCOMMODATION` | `'Accommodation'` |
| `MEAL_ALLOWANCE` | `'Meal Allowance'` |

</details>

##### class `ClaimCurrency(Enum)`
Link: [ClaimCurrency](file:///Users/arghajitsingha/playwright-python/constants/components/claim/claim_constants.py#L18)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `AFGHANISTAN_AFGHANI` | `'Afghanistan Afghani'` |
| `EURO` | `'Euro'` |
| `US_DOLLAR` | `'US Dollar'` |

</details>

##### class `Api_Endpoints(Enum)`
Link: [Api_Endpoints](file:///Users/arghajitsingha/playwright-python/constants/components/claim/claim_constants.py#L23)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `CLAIM_ENDPOINT` | `'**/api/v2/claim/employees/*/requests'` |

</details>

---

### `constants/components/dashboard/help_constants.py` <a id='constantscomponentsdashboardhelp_constantspy'></a>

**Source File**: [help_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/help_constants.py)

#### Classes

##### class `HelpConstants`
Link: [HelpConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/help_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `HELP_BUTTON_TEXT` | `'Help'` |
| `HELP_URL` | `'https://starterhelp.orangehrm.com/hc/en-us'` |

</details>

---

### `constants/components/dashboard/latest_posts_constants.py` <a id='constantscomponentsdashboardlatest_posts_constantspy'></a>

**Source File**: [latest_posts_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/latest_posts_constants.py)

#### Classes

##### class `LatestPostsConstants`
Link: [LatestPostsConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/latest_posts_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LATEST_POSTS_WIDGET_TEXT` | `'Buzz Latest Posts'` |

</details>

---

### `constants/components/dashboard/leaves_constants.py` <a id='constantscomponentsdashboardleaves_constantspy'></a>

**Source File**: [leaves_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/leaves_constants.py)

#### Classes

##### class `LeavesConstants`
Link: [LeavesConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/leaves_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LEAVES_WIDGET_TITLE` | `'Employees on Leave Today'` |
| `NO_CONTENT_IMAGE` | `'/web/images/dashboard_empty_widget_watermark.png'` |
| `NO_CONTENT_TEXT` | `'No Employees are on Leave Today'` |

</details>

---

### `constants/components/dashboard/locations_constants.py` <a id='constantscomponentsdashboardlocations_constantspy'></a>

**Source File**: [locations_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/locations_constants.py)

#### Classes

##### class `LocationsPageConstants`
Link: [LocationsPageConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/locations_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LOCATIONS_WIDGET_TEXT` | `'Employee Distribution by Location'` |

</details>

---

### `constants/components/dashboard/my_actions_constants.py` <a id='constantscomponentsdashboardmy_actions_constantspy'></a>

**Source File**: [my_actions_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/my_actions_constants.py)

#### Classes

##### class `MyActionsPageConstants`
Link: [MyActionsPageConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/my_actions_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `MY_ACTIONS_WIDGET_TEXT` | `'My Actions'` |

</details>

---

### `constants/components/dashboard/quick_launch_constants.py` <a id='constantscomponentsdashboardquick_launch_constantspy'></a>

**Source File**: [quick_launch_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/quick_launch_constants.py)

#### Classes

##### class `QuickLaunchPageConstants`
Link: [QuickLaunchPageConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/quick_launch_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `QUICK_LAUNCH_WIDGET_TEXT` | `'Quick Launch'` |

</details>

---

### `constants/components/dashboard/subunits_constants.py` <a id='constantscomponentsdashboardsubunits_constantspy'></a>

**Source File**: [subunits_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/subunits_constants.py)

#### Classes

##### class `SubunitsPageConstants`
Link: [SubunitsPageConstants](file:///Users/arghajitsingha/playwright-python/constants/components/dashboard/subunits_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `SUBUNIT_WIDGET_TEXT` | `'Employee Distribution by Sub Unit'` |

</details>

---

### `constants/components/leave/leave_list_constants.py` <a id='constantscomponentsleaveleave_list_constantspy'></a>

**Source File**: [leave_list_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/leave/leave_list_constants.py)

#### Classes

##### class `LeaveListConstants`
Link: [LeaveListConstants](file:///Users/arghajitsingha/playwright-python/constants/components/leave/leave_list_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/leave/viewLeaveList'` |
| `SIDE_PANEL_MENU` | `'Leave'` |
| `TOP_NAV_LINK` | `'Leave List'` |
| `DEFAULT_FROM_DATE` | `'2026-01-01'` |
| `TEST_STATUS_PENDING` | `'Pending Approval'` |
| `TEST_DATE` | `'2026-05-01'` |
| `TEST_STATUS` | `'Pending Approval'` |
| `TEST_EMPLOYEE_NAME` | `'Unknown_User_Random_999'` |
| `LEAVE_REQUESTS_URL` | `'**/leave/employees/leave-requests*'` |

</details>

---

### `constants/components/performance/performance_reviews_constants.py` <a id='constantscomponentsperformanceperformance_reviews_constantspy'></a>

**Source File**: [performance_reviews_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/performance/performance_reviews_constants.py)

#### Classes

##### class `PerformanceReviewsConstants`
Link: [PerformanceReviewsConstants](file:///Users/arghajitsingha/playwright-python/constants/components/performance/performance_reviews_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `PERFORMANCE_REVIEWS_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/performance/searchEvaluatePerformanceReview'` |
| `PERFORMANCE_REVIEWS_PAGE_TITLE` | `'OrangeHRM'` |
| `PERFORMANCE_REVIEWS_HEADING` | `'Employee Reviews'` |
| `PERFORMANCE_REVIEWS_API_ENDPOINT` | `'**/api/v2/performance/employees/reviews*'` |

</details>

---

### `constants/components/recruitment/candidates_constants.py` <a id='constantscomponentsrecruitmentcandidates_constantspy'></a>

**Source File**: [candidates_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/recruitment/candidates_constants.py)

#### Classes

##### class `RecruitmentCandidatesConstants`
Link: [RecruitmentCandidatesConstants](file:///Users/arghajitsingha/playwright-python/constants/components/recruitment/candidates_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates'` |
| `SIDE_PANEL_MENU` | `'Recruitment'` |
| `TOP_NAV_LINK` | `'Candidates'` |
| `TEST_CANDIDATE_NAME` | `'NonExistentCandidate_Unknown_User_999'` |
| `TEST_RESET_NAME` | `'Random_Candidate_Search_Value'` |
| `CANDIDATES_REQUESTS_URL` | `'**/recruitment/candidates*'` |

</details>

---

### `constants/components/time/time_sheet_constants.py` <a id='constantscomponentstimetime_sheet_constantspy'></a>

**Source File**: [time_sheet_constants.py](file:///Users/arghajitsingha/playwright-python/constants/components/time/time_sheet_constants.py)

#### Classes

##### class `TimeSheetConstants`
Link: [TimeSheetConstants](file:///Users/arghajitsingha/playwright-python/constants/components/time/time_sheet_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `TIMESHEETS_PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet'` |
| `TIMESHEETS_PAGE_TITLE` | `'OrangeHRM'` |
| `SELECT_EMPLOYEE_HEADING` | `'Select Employee'` |
| `TIMESHEETS_PENDING_ACTION_HEADING` | `'Timesheets Pending Action'` |
| `VIEW_BUTTON_TEXT` | `'View'` |
| `TIMESHEET_API_URL_ENDPOINT` | `'**/api/v2/time/timesheets/default**'` |

</details>

---

### `constants/dashboard_page_constants.py` <a id='constantsdashboard_page_constantspy'></a>

**Source File**: [dashboard_page_constants.py](file:///Users/arghajitsingha/playwright-python/constants/dashboard_page_constants.py)

#### Classes

##### class `DashboardPageConstants`
Link: [DashboardPageConstants](file:///Users/arghajitsingha/playwright-python/constants/dashboard_page_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `DASHBOARD_PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'` |
| `DASHBOARD_PAGE_TITLE` | `'OrangeHRM'` |
| `DASHBOARD_PAGE_HEADER` | `'Dashboard'` |
| `DASHBOARD_PAGE_HEADER_CLASS` | `'oxd-topbar-header-breadcrumb h6'` |
| `UPGRADE_BTN_TEXT` | `'Upgrade'` |
| `DASHBOARD_WIDGETS_COUNT` | `7` |
| `DASHBOARD_WIDGETS_TITLES` | `['Time at Work', 'My Actions', 'Quick Launch', 'Buzz Latest Posts', 'Employees on Leave Today', 'Employee Distributio...` |

</details>

---

### `constants/directory_constants.py` <a id='constantsdirectory_constantspy'></a>

**Source File**: [directory_constants.py](file:///Users/arghajitsingha/playwright-python/constants/directory_constants.py)

#### Classes

##### class `DirectoryConstants`
Link: [DirectoryConstants](file:///Users/arghajitsingha/playwright-python/constants/directory_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `DIRECTORY_OPTION_TEXT` | `'Directory'` |
| `DIRECTORY_PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/directory/viewDirectory'` |
| `FILTER_LABELS_LIST` | `['Employee Name', 'Job Title', 'Location']` |
| `API_PATTERN` | `'**/api/v2/directory/employees**'` |

</details>

---

### `constants/login_page_constants.py` <a id='constantslogin_page_constantspy'></a>

**Source File**: [login_page_constants.py](file:///Users/arghajitsingha/playwright-python/constants/login_page_constants.py)

#### Classes

##### class `LoginPageConstants`
Link: [LoginPageConstants](file:///Users/arghajitsingha/playwright-python/constants/login_page_constants.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LOGIN_PAGE_URL` | `'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'` |

</details>

---

### `constants/my_info_constants.py` <a id='constantsmy_info_constantspy'></a>

**Source File**: [my_info_constants.py](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py)

<details>
<summary>Imports</summary>

```python
from enum import Enum
time
```
</details>

#### Classes

##### class `MyInfoConstants`
Link: [MyInfoConstants](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `MY_INFO_TAB_OPTION` | `'My Info'` |
| `PERSONAL_DETAILS_TAB_TEXT` | `'Personal Details'` |
| `CONTACT_DETAILS_TAB_TEXT` | `'Contact Details'` |
| `EMERGENCY_CONTACT_TAB_TEXT` | `'Emergency Contacts'` |
| `DEPENDENTS_TAB_TEXT` | `'Dependents'` |
| `IMMIGRATION_TAB_TEXT` | `'Immigration'` |
| `JOB_TAB_TEXT` | `'Job'` |
| `SALARY_TAB_TEXT` | `'Salary'` |
| `REPORT_TO_TAB_TEXT` | `'Report-to'` |
| `QUALIFICATIONS_TAB_TEXT` | `'Qualifications'` |
| `MEMBERSHIPS_TAB_TEXT` | `'Memberships'` |

</details>

##### class `PersonalDetails(Enum)`
Link: [PersonalDetails](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L18)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `EMPLOYEE_FULL_NAME` | `'Employee Full Name'` |
| `EMPLOYEE_ID` | `'Employee Id'` |
| `OTHER_ID` | `'Other Id'` |
| `DRIVER_LICENSE_NUMBER` | `"Driver's License Number"` |
| `LICENSE_EXPIRY_DATE` | `'License Expiry Date'` |
| `NATIONALITY` | `'Nationality'` |
| `MARITIAL_STATUS` | `'Maritial Status'` |
| `DATE_OF_BIRTH` | `'Date of Birth'` |
| `GENDER` | `'Gender'` |
| `MILITARY_SERVICE` | `'Military Service'` |
| `SMOKER` | `'Smoker'` |
| `CUSTOM_FIELDS` | `'Custom Fields'` |
| `BLOOD_TYPE` | `'Blood Type'` |
| `TEST_FIELD` | `'Test_Field'` |
| `ATTACHMENTS` | `'Attachments'` |

</details>

##### class `ContactDetails(Enum)`
Link: [ContactDetails](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L36)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `STREET_1` | `'Street 1'` |
| `STREET_2` | `'Street 2'` |
| `CITY` | `'City'` |
| `STATE` | `'State/Province'` |
| `POSTAL_CODE` | `'Zip/Postal Code'` |
| `COUNTRY` | `'Country'` |
| `HOME` | `'Home'` |
| `MOBILE` | `'Mobile'` |
| `WORK` | `'Work'` |
| `WORK_EMAIL` | `'Work Email'` |
| `OTHER_EMAIL` | `'Other Email'` |

</details>

##### class `PersonalDetailsCustomFields(Enum)`
Link: [PersonalDetailsCustomFields](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L49)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `BLOOD_GROUP` | `'Blood Group'` |
| `TEST_FIELD` | `'Test_Field'` |

</details>

##### class `EmergencyContacts(Enum)`
Link: [EmergencyContacts](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L53)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `NAME` | `'Name'` |
| `RELATIONSHIP` | `'Relationship'` |
| `HOME_TELEPHONE` | `'Home Telephone'` |
| `MOBILE` | `'Mobile'` |
| `WORK_TELEPHONE` | `'Work Telephone'` |

</details>

##### class `EmergencyContactsTestData`
Link: [EmergencyContactsTestData](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L60)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `RELATIONSHIP` | `'Brother'` |
| `HOME_TELEPHONE` | `'123-456-7890'` |
| `MOBILE` | `'987-654-3210'` |
| `WORK_TELEPHONE` | `'555-555-5555'` |

</details>

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`get_dynamic_contact_name`](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L67) | `cls` | `str` | - |


##### class `Api_Endpoints(Enum)`
Link: [Api_Endpoints](file:///Users/arghajitsingha/playwright-python/constants/my_info_constants.py#L70)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `CONTACT_DETAILS_ENDPOINT` | `'**/contact-details'` |
| `PERSONAL_DETAILS_ENDPOINT` | `'**/personal-details'` |
| `PERSONAL_DETAILS_CUSTOM_FIELDS_ENDPOINT` | `'**/custom-fields?screen=personal'` |
| `EMERGENCY_CONTACTS_ENDPOINT` | `'**/emergency-contacts*'` |

</details>

---

## Locators

### `locators/about_me_locators.py` <a id='locatorsabout_me_locatorspy'></a>

**Source File**: [about_me_locators.py](file:///Users/arghajitsingha/playwright-python/locators/about_me_locators.py)

#### Classes

##### class `AboutMeLocators`
Link: [AboutMeLocators](file:///Users/arghajitsingha/playwright-python/locators/about_me_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ABOUT_ME_BUTTON` | `'//a[@class="oxd-userdropdown-link"][contains(@href, "#")]'` |
| `ABOUT_ME_MODAL` | `"div[role='document']"` |
| `ABOUT_ME_MODAL_HEADER` | `"div[role='document'] h6"` |
| `ABOUT_ME_MODAL_KEY_FIELDS` | `"div[role='document'] p.orangehrm-about-title"` |
| `ABOUT_ME_MODAL_VALUE_FIELDS` | `"div[role='document'] p.orangehrm-about-text"` |
| `ABOUT_ME_MODAL_CLOSE_BTN` | `"div[role='document'] button.oxd-dialog-close-button-position"` |

</details>

---

### `locators/components/admin/system_user_filter_locators.py` <a id='locatorscomponentsadminsystem_user_filter_locatorspy'></a>

**Source File**: [system_user_filter_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/admin/system_user_filter_locators.py)

#### Classes

##### class `SystemUserFilterLocators`
Link: [SystemUserFilterLocators](file:///Users/arghajitsingha/playwright-python/locators/components/admin/system_user_filter_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ADMIN_OPTION` | `"//a[contains(@href, 'viewAdminModule')]/child::span"` |
| `USER_LIST_COUNT` | `"div[class='orangehrm-horizontal-padding orangehrm-vertical-padding'] span"` |
| `USER_LIST_ROWS` | `"//div[@class='oxd-table-body']//div[@role='row']"` |
| `USER_LIST_CELLS` | `lambda row, col: f"(//div[@class='oxd-table-body']//div[@role='row'])[{row}]//div[@role='cell'][{col}]/div"` |

</details>

---

### `locators/components/claim/claim_locators.py` <a id='locatorscomponentsclaimclaim_locatorspy'></a>

**Source File**: [claim_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/claim/claim_locators.py)

<details>
<summary>Imports</summary>

```python
from playwright.sync_api import Locator
from enum import Enum
```
</details>

#### Classes

##### class `ClaimLocators`
Link: [ClaimLocators](file:///Users/arghajitsingha/playwright-python/locators/components/claim/claim_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `CLAIM_TAB` | `lambda name: f"//li//a//span[text()='{name}']"` |
| `ASSIGN_CLAIM_SUB_MENU` | `lambda name: f"//nav[@role='navigation']//a[text()='{name}']"` |
| `EMPLOYEE_NAME_INPUT` | `"//label[normalize-space(text())='Employee Name']/following::input[1]"` |
| `EVENT_INPUT` | `"//label[normalize-space(text())='Event']/following::div[contains(@class, 'oxd-select-text')][1]"` |
| `CURRENCY_INPUT` | `"//label[normalize-space(text())='Currency']/following::div[contains(@class, 'oxd-select-text')][1]"` |
| `REMARKS_TEXTAREA` | `"//label[normalize-space(text())='Remarks']/following::textarea[1]"` |
| `CREATE_BUTTON` | `"button[type='submit']"` |
| `SUCCESS_MESSAGE` | `'div.oxd-toast.oxd-toast--success.oxd-toast-container'` |
| `DROPDOWN_OPTION` | `lambda option: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"` |

</details>

---

### `locators/components/dashboard/help_locators.py` <a id='locatorscomponentsdashboardhelp_locatorspy'></a>

**Source File**: [help_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/help_locators.py)

#### Classes

##### class `HelpLocators`
Link: [HelpLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/help_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `HELP_BUTTON` | `"//button[@title='Help']"` |
| `HELP_ICON` | `'i.bi-question-lg'` |

</details>

---

### `locators/components/dashboard/latest_posts_locators.py` <a id='locatorscomponentsdashboardlatest_posts_locatorspy'></a>

**Source File**: [latest_posts_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/latest_posts_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.components.dashboard.latest_posts_constants import LatestPostsConstants
```
</details>

#### Classes

##### class `LatestPostsLocators`
Link: [LatestPostsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/latest_posts_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `HEADER` | `f".orangehrm-dashboard-widget-header:has-text('{LatestPostsConstants.LATEST_POSTS_WIDGET_TEXT}') p"` |
| `POSTS_CONTAINER` | `'div.orangehrm-buzz-widget-card'` |
| `POSTS_IMAGE` | `'img.orangehrm-buzz-widget-picture'` |
| `POSTS_USER_IMAGE` | `"div.orangehrm-buzz-profile-image img[alt='profile picture']"` |
| `POSTS_USER_NAME` | `'p.orangehrm-buzz-widget-header-emp'` |
| `POSTS_CREATION_TIME` | `'p.orangehrm-buzz-widget-header-time'` |
| `POSTS_BODY` | `'p.orangehrm-buzz-widget-body'` |

</details>

---

### `locators/components/dashboard/leaves_locators.py` <a id='locatorscomponentsdashboardleaves_locatorspy'></a>

**Source File**: [leaves_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/leaves_locators.py)

#### Classes

##### class `LeavesLocators`
Link: [LeavesLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/leaves_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LEAVES_WIDGET_TEXT` | `'svg.oxd-icon ~ p'` |
| `NO_CONTENT_IMAGE` | `"div.emp-leave-chart img[alt='No Content']"` |
| `NO_CONTENT_TEXT` | `'div.emp-leave-chart img ~ p'` |
| `CONFIGURATION_ICONS` | `'i.bi-gear-fill'` |

</details>

---

### `locators/components/dashboard/location_locators.py` <a id='locatorscomponentsdashboardlocation_locatorspy'></a>

**Source File**: [location_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/location_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.components.dashboard.locations_constants import LocationsPageConstants
```
</details>

#### Classes

##### class `LocationsPageLocators`
Link: [LocationsPageLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/location_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LOCATIONS_WIDGET_TEXT` | `f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') p"` |
| `LOCATIONS_LEGENDS` | `lambda location_name: f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') span[t...` |
| `LOCATIONS_PIE_CHART` | `f".orangehrm-dashboard-widget:has-text('{LocationsPageConstants.LOCATIONS_WIDGET_TEXT}') canvas"` |

</details>

---

### `locators/components/dashboard/my_actions_locators.py` <a id='locatorscomponentsdashboardmy_actions_locatorspy'></a>

**Source File**: [my_actions_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/my_actions_locators.py)

#### Classes

##### class `MyActionsLocators`
Link: [MyActionsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/my_actions_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `MY_ACTIONS_WIDGET_TEXT` | `'.bi-list-check ~ p'` |
| `MY_ACTION_LIST_ITEMS` | `'.orangehrm-todo-list-item > p'` |

</details>

---

### `locators/components/dashboard/quick_launch_locators.py` <a id='locatorscomponentsdashboardquick_launch_locatorspy'></a>

**Source File**: [quick_launch_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/quick_launch_locators.py)

#### Classes

##### class `QuickLaunchLocators`
Link: [QuickLaunchLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/quick_launch_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `QUICK_LAUNCH_WIDGET_TEXT` | `'.bi-lightning-charge-fill ~ p'` |
| `ASSIGN_LEAVE` | `"div[title='Assign Leave']"` |
| `LEAVE_LIST` | `"div[title='Leave List']"` |
| `MY_TIMESHEETS` | `"div[title='Timesheets']"` |
| `APPLY_LEAVES` | `"div[title='Apply Leave']"` |
| `MY_LEAVE` | `"div[title='My Leave']"` |
| `MY_TIMESHEET` | `"div[title='My Timesheet']"` |

</details>

---

### `locators/components/dashboard/subunit_locators.py` <a id='locatorscomponentsdashboardsubunit_locatorspy'></a>

**Source File**: [subunit_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/subunit_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.components.dashboard.subunits_constants import SubunitsPageConstants
```
</details>

#### Classes

##### class `SubunitLocators`
Link: [SubunitLocators](file:///Users/arghajitsingha/playwright-python/locators/components/dashboard/subunit_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `SUBUNIT_WIDGET_TEXT` | `f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') p"` |
| `SUBUNIT_LEGENDS` | `lambda subunit_name: f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') span[title...` |
| `SUBUNIT_PIE_CHART` | `f".orangehrm-dashboard-widget:has-text('{SubunitsPageConstants.SUBUNIT_WIDGET_TEXT}') canvas"` |

</details>

---

### `locators/components/leave/leave_list_locators.py` <a id='locatorscomponentsleaveleave_list_locatorspy'></a>

**Source File**: [leave_list_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/leave/leave_list_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.components.leave.leave_list_constants import LeaveListConstants
from enum import Enum
```
</details>

#### Classes

##### class `LeaveListLocators`
Link: [LeaveListLocators](file:///Users/arghajitsingha/playwright-python/locators/components/leave/leave_list_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `LEAVE_OPTION` | `f"//li//a//span[text()='{LeaveListConstants.SIDE_PANEL_MENU}']"` |
| `LEAVE_LIST_ACCORDIAN` | `f"//a[text()='{LeaveListConstants.TOP_NAV_LINK}']"` |
| `PAGE_TITLE` | `".oxd-text--h5:has-text('Leave List')"` |
| `FROM_DATE` | `"//label[contains(text(), 'From Date')]/following::input[1]"` |
| `TO_DATE` | `"//label[contains(text(), 'To Date')]/following::input[1]"` |
| `STATUS_DROPDOWN` | `"//label[contains(text(), 'Show Leave with Status')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `LEAVE_TYPE_DROPDOWN` | `"//label[contains(text(), 'Leave Type')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `EMPLOYEE_NAME` | `"//label[contains(text(), 'Employee Name')]/following::input[1]"` |
| `SUB_UNIT_DROPDOWN` | `"//label[contains(text(), 'Sub Unit')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `INCLUDE_PAST_EMPLOYEES_CHECKBOX` | `"//label[contains(text(), 'Include Past Employees')]/following::input[1]"` |
| `RESET_BUTTON` | `"button.oxd-button--ghost:has-text('Reset')"` |
| `SEARCH_BUTTON` | `"button.oxd-button--secondary:has-text('Search')"` |
| `RESULTS_TABLE` | `'.oxd-table'` |
| `NO_RECORDS_TEXT` | `"//span[text()='No Records Found']"` |
| `TABLE_HEADER_DATE` | `"th:has-text('Date')"` |
| `TABLE_HEADER_EMPLOYEE` | `"th:has-text('Employee Name')"` |
| `TABLE_HEADER_STATUS` | `"th:has-text('Status')"` |
| `DROPDOWN_OPTIONS` | `lambda status: f"//div[contains(@class, 'oxd-select-option') and contains(., '{status}')]"` |

</details>

---

### `locators/components/my_info/contact_details_locators.py` <a id='locatorscomponentsmy_infocontact_details_locatorspy'></a>

**Source File**: [contact_details_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/contact_details_locators.py)

#### Classes

##### class `ContactDetailsLocators`
Link: [ContactDetailsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/contact_details_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `CONTACT_DETAILS_INPUT_FIELDS` | `lambda fieldLabel: f"(//label[normalize-space(text())='{fieldLabel}']/following::input)[1]"` |
| `CONTACT_DETAILS_DROPDOWN_FIELDS` | `"(//div[@class='oxd-select-text-input'])[1]"` |

</details>

---

### `locators/components/my_info/emergency_contacts_locators.py` <a id='locatorscomponentsmy_infoemergency_contacts_locatorspy'></a>

**Source File**: [emergency_contacts_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/emergency_contacts_locators.py)

#### Classes

##### class `EmergencyContactsLocators`
Link: [EmergencyContactsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/emergency_contacts_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `ADD_CONTACT_BUTTON` | `"//button[contains(., 'Add')]"` |
| `INPUT_FIELDS` | `lambda fieldLabel: f"(//label[normalize-space(text())='{fieldLabel}']/following::input)[1]"` |
| `SAVE_BUTTON` | `"button[type='submit']"` |
| `CANCEL_BUTTON` | `"//button[contains(., 'Cancel')]"` |
| `TABLE_CARD` | `'div.oxd-table-card'` |
| `RECORD_ROW_BY_NAME` | `lambda name: f"(//div[@class='oxd-table-card' and contains(., '{name}')])[1]"` |
| `RECORD_CELL` | `lambda name, col_idx: f"(//div[@class='oxd-table-card' and contains(., '{name}')])[1]//div[contains(@class, 'oxd-tabl...` |
| `RECORD_DELETE_BUTTON` | `lambda name: f"(//div[@class='oxd-table-card' and contains(., '{name}')])[1]//button[contains(@class, 'oxd-table-cell...` |
| `RECORD_EDIT_BUTTON` | `lambda name: f"(//div[@class='oxd-table-card' and contains(., '{name}')])[1]//button[contains(@class, 'oxd-table-cell...` |

</details>

---

### `locators/components/my_info/personal_details_locators.py` <a id='locatorscomponentsmy_infopersonal_details_locatorspy'></a>

**Source File**: [personal_details_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/personal_details_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.my_info_constants import MyInfoConstants
from constants.my_info_constants import PersonalDetails
```
</details>

#### Classes

##### class `PersonalDetailsLocators`
Link: [PersonalDetailsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/my_info/personal_details_locators.py#L3)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `MY_INFO_OPTION` | `f"//li//a//span[text()='{MyInfoConstants.MY_INFO_TAB_OPTION}']"` |
| `TAB` | `lambda tabText: f"//div[@class='orangehrm-tabs-wrapper']/a[text()='{tabText}']"` |
| `EMPLOYEE_NAME` | `'div.orangehrm-edit-employee-name h6'` |
| `EMPLOYEE_IMAGE` | `'div.orangehrm-edit-employee-image img'` |
| `SECTION_HEADERS` | `lambda headerText: f"//h6[contains(@class,'orangehrm-main-title') and text()='{headerText}']"` |
| `LABEL_HEADERS` | `lambda labelText: f"//label[contains(@class, 'oxd-label') and contains(text(), '{labelText}')]"` |
| `FIRST_NAME` | `"input[name='firstName']"` |
| `MIDDLE_NAME` | `"input[name='middleName']"` |
| `LAST_NAME` | `"input[name='lastName']"` |
| `NICKNAME` | `"(//label[normalize-space(text())='Nickname']/following::input)[1]"` |
| `EMPLOYEE_ID` | `f'(//label[normalize-space(text())="{PersonalDetails.EMPLOYEE_ID.value}"]/following::input)[1]'` |
| `OTHER_ID` | `f'(//label[normalize-space(text())="{PersonalDetails.OTHER_ID.value}"]/following::input)[1]'` |
| `DRIVER_LICENCE_NUMBER` | `f'(//label[normalize-space(text())="{PersonalDetails.DRIVER_LICENSE_NUMBER.value}"]/following::input)[1]'` |
| `DRIVER_LICENSE_NUMBER` | `DRIVER_LICENCE_NUMBER` |
| `LICENSE_EXPIRY_DATE` | `f'(//label[normalize-space(text())="{PersonalDetails.LICENSE_EXPIRY_DATE.value}"]/following::input)[1]'` |
| `NATIONALITY` | `"(//div[@class='oxd-select-text-input'])[1]"` |
| `MARITAL_STATUS` | `"(//div[@class='oxd-select-text-input'])[2]"` |
| `DATE_OF_BIRTH` | `f'(//label[normalize-space(text())="{PersonalDetails.DATE_OF_BIRTH.value}"]/following::input)[1]'` |
| `GENDER_MALE` | `f'(//label[normalize-space(text())="{PersonalDetails.GENDER.value}"]/following::input)[1]'` |
| `GENDER_FEMALE` | `f'(//label[normalize-space(text())="{PersonalDetails.GENDER.value}"]/following::input)[2]'` |
| `BLOOD_GROUP` | `"(//div[@class='oxd-select-text-input'])[3]"` |
| `TEST_FIELD` | `f'(//label[contains(text(), "{PersonalDetails.TEST_FIELD.value}")]/following::input)[1]'` |
| `MILITARY_SERVICE` | `f'(//label[normalize-space(text())="{PersonalDetails.MILITARY_SERVICE.value}"]/following::input)[1]'` |
| `SMOKER_STATUS` | `f'(//label[normalize-space(text())="{PersonalDetails.SMOKER.value}"]/following::input)[1]'` |

</details>

---

### `locators/components/performance/performance_reviews_locators.py` <a id='locatorscomponentsperformanceperformance_reviews_locatorspy'></a>

**Source File**: [performance_reviews_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/performance/performance_reviews_locators.py)

#### Classes

##### class `PerformanceReviewsLocators`
Link: [PerformanceReviewsLocators](file:///Users/arghajitsingha/playwright-python/locators/components/performance/performance_reviews_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `PAGE_TITLE` | `".oxd-text--h5:has-text('Employee Reviews')"` |
| `EMPLOYEE_NAME` | `"//label[text()='Employee Name']/following::input[1]"` |
| `JOB_TITLE_DROPDOWN` | `"//label[text()='Job Title']/following::div[contains(@class, 'oxd-select-text')][1]"` |
| `SUB_UNIT_DROPDOWN` | `"//label[text()='Sub Unit']/following::div[contains(@class, 'oxd-select-text')][1]"` |
| `STATUS_DROPDOWN` | `"//label[text()='Status']/following::div[contains(@class, 'oxd-select-text')][1]"` |
| `SEARCH_BUTTON` | `"button[type='submit']:has-text('Search')"` |
| `RESET_BUTTON` | `"button:has-text('Reset')"` |
| `RESULTS_TABLE` | `'.oxd-table'` |
| `RESULTS_ROWS` | `'.oxd-table-row'` |
| `NO_RECORDS_TEXT` | `"//span[text()='No Records Found']"` |
| `DROPDOWN_OPTIONS` | `lambda option: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"` |

</details>

---

### `locators/components/recruitment/candidates_locators.py` <a id='locatorscomponentsrecruitmentcandidates_locatorspy'></a>

**Source File**: [candidates_locators.py](file:///Users/arghajitsingha/playwright-python/locators/components/recruitment/candidates_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants
```
</details>

#### Classes

##### class `RecruitmentCandidatesLocators`
Link: [RecruitmentCandidatesLocators](file:///Users/arghajitsingha/playwright-python/locators/components/recruitment/candidates_locators.py#L3)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `RECRUITMENT_OPTION` | `f"//li//a//span[text()='{RecruitmentCandidatesConstants.SIDE_PANEL_MENU}']"` |
| `CANDIDATES_LINK` | `f"//a[text()='{RecruitmentCandidatesConstants.TOP_NAV_LINK}']"` |
| `PAGE_TITLE` | `".oxd-text--h5:has-text('Candidates')"` |
| `JOB_TITLE_DROPDOWN` | `"//label[contains(text(), 'Job Title')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `VACANCY_DROPDOWN` | `"//label[contains(text(), 'Vacancy')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `HIRING_MANAGER_DROPDOWN` | `"//label[contains(text(), 'Hiring Manager')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `STATUS_DROPDOWN` | `"//label[contains(text(), 'Status')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `CANDIDATE_NAME` | `"//label[contains(text(), 'Candidate Name')]/following::input[1]"` |
| `KEYWORDS` | `"//label[contains(text(), 'Keywords')]/following::input[1]"` |
| `DATE_FROM` | `"//label[contains(text(), 'Date of Application')]/following::input[1]"` |
| `DATE_TO` | `"//label[contains(text(), 'Date of Application')]/following::input[2]"` |
| `METHOD_DROPDOWN` | `"//label[contains(text(), 'Method of Application')]/following::div[contains(@class, 'oxd-select-text')]"` |
| `RESET_BUTTON` | `"button.oxd-button--ghost:has-text('Reset')"` |
| `SEARCH_BUTTON` | `"button.oxd-button--secondary:has-text('Search')"` |
| `ADD_BUTTON` | `"button.oxd-button--secondary:has-text('Add')"` |
| `RESULTS_TABLE` | `'.oxd-table'` |
| `RECORD_COUNT_TEXT` | `".oxd-text--body:has-text('Records Found')"` |
| `NO_RECORDS_TEXT` | `"//span[text()='No Records Found']"` |
| `TABLE_HEADER_CANDIDATE` | `"th:has-text('Candidate')"` |
| `TABLE_HEADER_STATUS` | `"th:has-text('Status')"` |
| `DROPDOWN_OPTIONS` | `lambda option: f"//div[contains(@class, 'oxd-select-option') and contains(., '{option}')]"` |

</details>

---

### `locators/dashboard_locators.py` <a id='locatorsdashboard_locatorspy'></a>

**Source File**: [dashboard_locators.py](file:///Users/arghajitsingha/playwright-python/locators/dashboard_locators.py)

#### Classes

##### class `DashboardLocators`
Link: [DashboardLocators](file:///Users/arghajitsingha/playwright-python/locators/dashboard_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `PAGE_HEADER` | `'.oxd-topbar-header-breadcrumb h6'` |
| `UPGRADE_BUTTON` | `'button.orangehrm-upgrade-button'` |
| `DASHBOARD_WIDGETS` | `'div.orangehrm-dashboard-widget.oxd-sheet'` |
| `DASHBOARD_WIDGETS_TITLE` | `'div.orangehrm-dashboard-widget.oxd-sheet .orangehrm-dashboard-widget-name > p'` |
| `DASHBOARD_PROFILE_DROPDOWN_IMAGE` | `'img[alt="profile picture"].oxd-userdropdown-img'` |
| `TIME_AT_WORK_USER_IMAGE` | `'.orangehrm-attendance-card-profile-image img[alt="profile picture"].employee-image'` |

</details>

---

### `locators/directory_locators.py` <a id='locatorsdirectory_locatorspy'></a>

**Source File**: [directory_locators.py](file:///Users/arghajitsingha/playwright-python/locators/directory_locators.py)

<details>
<summary>Imports</summary>

```python
from constants.directory_constants import DirectoryConstants
```
</details>

#### Classes

##### class `DirectoryPageLocators`
Link: [DirectoryPageLocators](file:///Users/arghajitsingha/playwright-python/locators/directory_locators.py#L4)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `DIRECTORY_OPTION` | `f"//li//a//span[text()='{DirectoryConstants.DIRECTORY_OPTION_TEXT}']"` |
| `DIRECTORY_PAGE_HEADER_TITLE` | `'h6.oxd-topbar-header-breadcrumb-module'` |
| `DIRECTORY_PAGE_HEADER` | `'h5.oxd-table-filter-title'` |
| `FILTER_LABELS` | `'label.oxd-label'` |
| `EMPLOYEE_NAME_DROPDOWN` | `"//input[@placeholder='Type for hints...']"` |
| `DROPDOWN_SELECT_OPTION` | `'div.oxd-select-dropdown'` |
| `DROPDOWN_OPTIONS` | `lambda value: f"div.oxd-select-dropdown div.oxd-select-option span:has-text('{value}')"` |
| `SELECT_DROPDOWN` | `'div.oxd-select-text'` |
| `RESET_BUTTON` | `"button[type='reset']"` |
| `SEARCH_BUTTON` | `"button[type='submit']"` |
| `DIRECTORY_CARD` | `'.orangehrm-directory-card'` |
| `PROFILE_PICTURE` | `'.orangehrm-profile-picture-img'` |
| `CARD_SUBTITLE` | `'.orangehrm-directory-card-subtitle'` |
| `CARD_BODY` | `'.orangehrm-directory-card-body'` |
| `CARD_DESCRIPTION` | `'.orangehrm-directory-card-description'` |
| `MEMBER_CARD_CONTAINER` | `'.orangehrm-container'` |

</details>

---

### `locators/orangeHRM_login_locators.py` <a id='locatorsorangeHRM_login_locatorspy'></a>

**Source File**: [orangeHRM_login_locators.py](file:///Users/arghajitsingha/playwright-python/locators/orangeHRM_login_locators.py)

#### Classes

##### class `LoginPageLocators`
Link: [LoginPageLocators](file:///Users/arghajitsingha/playwright-python/locators/orangeHRM_login_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `COMPANY_LOGO` | `"img[alt='company-branding']"` |
| `USERNAME_LOCATOR` | `'.orangehrm-login-error .oxd-text:nth-of-type(1)'` |
| `PASSWORD_LOCATOR` | `'.orangehrm-login-error .oxd-text:nth-of-type(2)'` |
| `USER_DROPDOWN` | `'.oxd-userdropdown-tab'` |
| `LOGOUT_BUTTON` | `'//a[@class="oxd-userdropdown-link"][contains(@href, "logout")]'` |

</details>

---

### `locators/timesheet_locators.py` <a id='locatorstimesheet_locatorspy'></a>

**Source File**: [timesheet_locators.py](file:///Users/arghajitsingha/playwright-python/locators/timesheet_locators.py)

#### Classes

##### class `TimeSheetLocators`
Link: [TimeSheetLocators](file:///Users/arghajitsingha/playwright-python/locators/timesheet_locators.py#L1)

<details>
<summary>Class Variables</summary>

| Variable | Value |
| :--- | :--- |
| `SELECT_EMPLOYEE_HEADING` | `"h5:has-text('Select Employee'), h6:has-text('Select Employee'), .oxd-text:has-text('Select Employee')"` |
| `TIMESHEETS_PENDING_ACTION_HEADING` | `"h5:has-text('Timesheets Pending Action'), h6:has-text('Timesheets Pending Action'), .oxd-text:has-text('Timesheets P...` |
| `EMPLOYEE_NAME_INPUT` | `"//input[@placeholder='Type for hints...']"` |
| `VIEW_BUTTON` | `"button[type='submit']:has-text('View')"` |
| `TIMESHEET_TABLE` | `'.oxd-table'` |
| `TIMESHEET_ROWS` | `'.oxd-table-row'` |
| `EMPLOYEE_NAME_CELL` | `'.oxd-table-cell:nth-child(1)'` |
| `TIMESHEET_PERIOD_CELL` | `'.oxd-table-cell:nth-child(2)'` |
| `ACTIONS_CELL` | `'.oxd-table-cell:nth-child(3)'` |
| `VIEW_ACTION_BUTTON` | `"button:has-text('View')"` |
| `RECORDS_FOUND_TEXT` | `"//*[contains(text(), 'Records Found')]"` |
| `NO_RECORDS_TEXT` | `"//span[text()='No Records Found']"` |

</details>

---

## Page Objects (POM)

### `pages/about_me_page.py` <a id='pagesabout_me_pagepy'></a>

**Source File**: [about_me_page.py](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py)

<details>
<summary>Imports</summary>

```python
from constants.about_me_constants import AboutMeAPIResponseKeys
from constants.api_constants import APIEndpoints
from constants.about_me_constants import ABOUT_ME_MODAL_HEADER_TEXT
from constants.about_me_constants import AboutMeKeys
from locators.about_me_locators import AboutMeLocators
from locators.orangeHRM_login_locators import LoginPageLocators
from pages.base_page import BasePage
from api.base_api import BaseAPI
from utils.ui_helpers import UIHelpers
from pytest_pulse import step, pulse_step
```
</details>

#### Classes

##### class `AboutMePage`
Link: [AboutMePage](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py#L13)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py#L15) | `self, page` | - | - |
| [`click_on_user_avatar`](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py#L22) | `self` | - | - |
| [`verify_about_me_modal_details`](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py#L33) | `self, request_setup, login_via_api` | - | - |
| [`close_about_me_modal`](file:///Users/arghajitsingha/playwright-python/pages/about_me_page.py#L77) | `self` | - | - |


---

### `pages/base_page.py` <a id='pagesbase_pagepy'></a>

**Source File**: [base_page.py](file:///Users/arghajitsingha/playwright-python/pages/base_page.py)

<details>
<summary>Imports</summary>

```python
from playwright.sync_api import expect, Locator
from pytest_pulse import pulse_step, step
time
```
</details>

#### Classes

##### class `BasePage`
Link: [BasePage](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L5)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L7) | `self, page` | - | - |
| [`strict_wait`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L10) | `self` | - | - |
| [`wait_for_fully_page_loaded`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L14) | `self` | - | - |
| [`navigateToUrl`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L19) | `self, url: str` | - | - |
| [`click`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L24) | `self, locator: str | Locator, index: int = 0` | - | - |
| [`fill`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L34) | `self, locator: str | Locator, text: str, index: int = 0` | - | - |
| [`verify_page_title`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L44) | `self, title: str` | - | - |
| [`verify_element_is_visible`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L48) | `self, locator: str | Locator` | - | - |
| [`verify_element_is_not_visible`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L57) | `self, locator: str | Locator` | - | - |
| [`verify_element_is_enabled`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L65) | `self, locator: str | Locator` | - | - |
| [`verify_element_is_disabled`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L73) | `self, locator: str | Locator` | - | - |
| [`verify_element_is_checked`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L81) | `self, locator: str | Locator` | - | - |
| [`verify_element_text`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L89) | `self, locator: str | Locator, text: str, index: int = 0` | - | - |
| [`verify_page_url`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L97) | `self, url` | - | - |
| [`wait_for_timeout`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L102) | `self, timeout_ms: int` | - | - |
| [`press_key`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L106) | `self, locator: str | Locator, key: str, index: int = 0` | - | - |
| [`get_element_count`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L115) | `self, locator: str | Locator` | `int` | - |
| [`verify_element_count`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L123) | `self, locator: str | Locator, count: int` | - | - |
| [`get_all_element_texts`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L133) | `self, locator: str | Locator` | - | - |
| [`verify_all_element_texts`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L143) | `self, locator: str | Locator, expected_texts: list[str]` | - | - |
| [`verify_element_texts_contains`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L150) | `self, locator: str | Locator, expected_texts: str` | - | - |
| [`verify_equal`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L159) | `self, actual, expected` | - | - |
| [`expect_contains`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L163) | `self, actual: str, expected: str` | - | - |
| [`get_attribute`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L167) | `self, locator: str | Locator, attribute: str, index: int = 0` | - | - |
| [`verify_element_text_ignore_case`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L174) | `self, locator: str | Locator, text: str, index: int = 0` | - | - |
| [`verify_element_text_contains`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L185) | `self, locator: str | Locator, expected_text: str, index: int = 0` | - | - |
| [`capture_screenshot`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L197) | `self, path: str = 'screenshots'` | - | - |
| [`verify_attribute_value_contains`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L201) | `self, locator: str | Locator, attribute: str, expected_value: str, index: int = 0` | - | - |
| [`wait_for_api_call`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L214) | `self, action, url: str, success_status: int = 200` | - | - |
| [`autocomplete_dropdown`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L233) | `self, locator, text` | - | - |
| [`verify_element_value`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L268) | `self, locator, expectedValue, index = 0` | - | - |
| [`verify_element_is_not_checked`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L272) | `self, locator, index = 0` | - | - |
| [`refresh_page`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L276) | `self` | - | - |
| [`get_element_inner_text`](file:///Users/arghajitsingha/playwright-python/pages/base_page.py#L280) | `self, locator: str | Locator, index: int = 0` | - | - |


---

### `pages/components/admin/system_user_filter_components.py` <a id='pagescomponentsadminsystem_user_filter_componentspy'></a>

**Source File**: [system_user_filter_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py)

<details>
<summary>Imports</summary>

```python
from utils.ui_helpers import UIHelpers
from constants.api_constants import APIEndpoints
from constants.components.admin.system_user_filter_constants import SystemUserFilterConstants
from locators.components.admin.system_user_filter_locators import SystemUserFilterLocators
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `SystemUserFilterComponents`
Link: [SystemUserFilterComponents](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L13)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L15) | `self, page` | - | - |
| [`verify_and_click_on_admin_option`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L21) | `self` | - | - |
| [`verify_admin_page_url`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L29) | `self` | - | - |
| [`verify_user_list_length`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L33) | `self, response` | - | - |
| [`get_user_list`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L51) | `self, request_setup, login_via_api` | - | - |
| [`verify_user_list`](file:///Users/arghajitsingha/playwright-python/pages/components/admin/system_user_filter_components.py#L60) | `self, response` | - | - |


---

### `pages/components/claim/assign_claim_page.py` <a id='pagescomponentsclaimassign_claim_pagepy'></a>

**Source File**: [assign_claim_page.py](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py)

<details>
<summary>Imports</summary>

```python
from constants.components.claim.claim_constants import ClaimConstants, ClaimEvent, ClaimCurrency, Api_Endpoints
from locators.components.claim.claim_locators import ClaimLocators
from pages.base_page import BasePage
from constants.common_constants import Keys
from pytest_pulse import step, pulse_step
re
```
</details>

#### Classes

##### class `AssignClaimPage`
Link: [AssignClaimPage](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L10) | `self, page` | - | - |
| [`click_on_claim_tab`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L15) | `self` | - | - |
| [`navigate_to_assign_claim_page`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L23) | `self` | - | - |
| [`assign_valid_claim`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L30) | `self` | - | - |
| [`assign_claim`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L40) | `self, employee_name, event: ClaimEvent, currency: ClaimCurrency, remarks = None` | - | - |
| [`verify_claim_assignment_success_message`](file:///Users/arghajitsingha/playwright-python/pages/components/claim/assign_claim_page.py#L66) | `self` | - | - |


---

### `pages/components/dashboard/help_components.py` <a id='pagescomponentsdashboardhelp_componentspy'></a>

**Source File**: [help_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py)

<details>
<summary>Imports</summary>

```python
from playwright.sync_api import Page, expect
from locators.components.dashboard.help_locators import HelpLocators
from constants.components.dashboard.help_constants import HelpConstants
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `HelpComponents(BasePage)`
Link: [HelpComponents](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py#L7)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py#L8) | `self, page: Page` | - | - |
| [`click_help_button`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py#L14) | `self` | - | - |
| [`verify_help_icon_is_visible`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py#L22) | `self` | - | - |
| [`verify_help_url`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/help_components.py#L27) | `self` | - | - |


---

### `pages/components/dashboard/latest_posts_components.py` <a id='pagescomponentsdashboardlatest_posts_componentspy'></a>

**Source File**: [latest_posts_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py)

<details>
<summary>Imports</summary>

```python
from pytest_pulse import step, pulse_step
from utils.ui_helpers import UIHelpers
from constants.api_constants import APIEndpoints
from constants.components.dashboard.latest_posts_constants import LatestPostsConstants
from locators.components.dashboard.latest_posts_locators import LatestPostsLocators
from pages.base_page import BasePage
```
</details>

#### Classes

##### class `LatestPostsComponent`
Link: [LatestPostsComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L10) | `self, page` | - | - |
| [`is_widget_visible`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L15) | `self` | - | - |
| [`verify_latest_posts_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L19) | `self` | - | - |
| [`get_latest_posts_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L26) | `self, request_setup, login_via_api` | - | - |
| [`validate_posts_user_name`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L34) | `self, data, post_locator` | - | - |
| [`validate_posts_user_image`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L51) | `self, data, post_locator` | - | - |
| [`validate_posts_creation_date_time`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L64) | `self, data, post_locator` | - | - |
| [`validate_latest_posts_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L75) | `self, response_json` | - | - |
| [`validate_posts_content`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/latest_posts_components.py#L95) | `self, data, post_locator` | - | - |


---

### `pages/components/dashboard/leaves_components.py` <a id='pagescomponentsdashboardleaves_componentspy'></a>

**Source File**: [leaves_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/leaves_components.py)

<details>
<summary>Imports</summary>

```python
from utils.ui_helpers import UIHelpers
from api.base_api import BaseAPI
from constants.components.dashboard.leaves_constants import LeavesConstants
from locators.components.dashboard.leaves_locators import LeavesLocators
from constants.api_constants import APIEndpoints
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `LeavesComponent`
Link: [LeavesComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/leaves_components.py#L10)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/leaves_components.py#L12) | `self, page` | - | - |
| [`verify_leaves_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/leaves_components.py#L19) | `self` | - | - |
| [`validate_no_content_in_leaves_widget`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/leaves_components.py#L27) | `self, request_setup, login_via_api` | - | - |


---

### `pages/components/dashboard/location_components.py` <a id='pagescomponentsdashboardlocation_componentspy'></a>

**Source File**: [location_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py)

<details>
<summary>Imports</summary>

```python
from pytest_pulse import pulse_step
from constants.api_constants import APIEndpoints
from constants.components.dashboard.locations_constants import LocationsPageConstants
from locators.components.dashboard.location_locators import LocationsPageLocators
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `LocationComponent`
Link: [LocationComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py#L10) | `self, page` | - | - |
| [`verify_locations_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py#L15) | `self` | - | - |
| [`get_locations_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py#L22) | `self, request_setup, login_via_api` | - | - |
| [`validate_locations_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/location_components.py#L30) | `self, response` | - | - |


---

### `pages/components/dashboard/my_actions_components.py` <a id='pagescomponentsdashboardmy_actions_componentspy'></a>

**Source File**: [my_actions_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py)

<details>
<summary>Imports</summary>

```python
re
from constants.api_constants import APIEndpoints
from constants.components.dashboard.my_actions_constants import MyActionsPageConstants
from locators.components.dashboard.my_actions_locators import MyActionsLocators
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `MyActionsComponent`
Link: [MyActionsComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L11) | `self, page` | - | - |
| [`verify_my_actions_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L16) | `self` | - | - |
| [`get_my_action_items_from_api`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L23) | `self, request_setup, login_via_api` | - | - |
| [`singularize`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L32) | `self, data` | - | - |
| [`validate_my_action_items`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/my_actions_components.py#L39) | `self, response` | - | - |


---

### `pages/components/dashboard/quick_launch_components.py` <a id='pagescomponentsdashboardquick_launch_componentspy'></a>

**Source File**: [quick_launch_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py)

<details>
<summary>Imports</summary>

```python
from constants.api_constants import APIEndpoints
from pages.base_page import BasePage
from constants.components.dashboard.quick_launch_constants import QuickLaunchPageConstants
from locators.components.dashboard.quick_launch_locators import QuickLaunchLocators
from pytest_pulse import step
```
</details>

#### Classes

##### class `QuickLaunchComponent`
Link: [QuickLaunchComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py#L10)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py#L12) | `self, page` | - | - |
| [`verify_quick_launch_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py#L17) | `self` | - | - |
| [`get_quick_launch_items`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py#L24) | `self, request_setup, login_via_api` | - | - |
| [`validate_quick_launch_items`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/quick_launch_components.py#L33) | `self, response` | - | - |


---

### `pages/components/dashboard/subunit_components.py` <a id='pagescomponentsdashboardsubunit_componentspy'></a>

**Source File**: [subunit_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py)

<details>
<summary>Imports</summary>

```python
from pytest_pulse import pulse_step
from constants.api_constants import APIEndpoints
from constants.components.dashboard.subunits_constants import SubunitsPageConstants
from locators.components.dashboard.subunit_locators import SubunitLocators
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `SubunitComponent`
Link: [SubunitComponent](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py#L10) | `self, page` | - | - |
| [`verify_subunit_widget_text`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py#L15) | `self` | - | - |
| [`get_subunit_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py#L22) | `self, request_setup, login_via_api` | - | - |
| [`validate_subunit_data`](file:///Users/arghajitsingha/playwright-python/pages/components/dashboard/subunit_components.py#L30) | `self, response` | - | - |


---

### `pages/components/leave/leave_list_page.py` <a id='pagescomponentsleaveleave_list_pagepy'></a>

**Source File**: [leave_list_page.py](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py)

<details>
<summary>Imports</summary>

```python
from constants.components.leave.leave_list_constants import LeaveListConstants
from pages.base_page import BasePage
from locators.components.leave.leave_list_locators import LeaveListLocators
from pytest_pulse import pulse_step, step
```
</details>

#### Classes

##### class `LeaveListPage(BasePage)`
Link: [LeaveListPage](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L6)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L7) | `self, page` | - | - |
| [`navigate_via_menu`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L12) | `self` | - | - |
| [`verify_page_loaded`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L18) | `self` | - | - |
| [`filter_leaves`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L22) | `self, from_date = None, to_date = None, status = None, leave_type = None, employee_name = None, sub_unit = None, include_past = False` | - | - |
| [`reset_filters`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L50) | `self` | - | - |
| [`verify_no_records_found`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L54) | `self, response` | - | - |
| [`verify_records_exist`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L59) | `self, response` | - | - |
| [`verify_date_reset`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L68) | `self, date_locator, expected_date_value` | - | - |
| [`fetch_leave_list_data`](file:///Users/arghajitsingha/playwright-python/pages/components/leave/leave_list_page.py#L74) | `self` | - | - |


---

### `pages/components/my_info/contact_details_components.py` <a id='pagescomponentsmy_infocontact_details_componentspy'></a>

**Source File**: [contact_details_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py)

<details>
<summary>Imports</summary>

```python
from constants.my_info_constants import Api_Endpoints, MyInfoConstants, ContactDetails
from utils.ui_helpers import UIHelpers
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from pages.components.my_info.personal_details_components import PersonalDetailsComponent
from pages.base_page import BasePage
from locators.components.my_info.contact_details_locators import ContactDetailsLocators
from pytest_pulse import step, pulse_step
```
</details>

#### Classes

##### class `ContactDetailsComponent`
Link: [ContactDetailsComponent](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py#L10)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py#L11) | `self, page` | - | - |
| [`click_on_contact_details_tab`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py#L18) | `self` | - | - |
| [`fetch_contact_details_from_api`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py#L24) | `self` | - | - |
| [`verify_contact_details`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/contact_details_components.py#L29) | `self, response` | - | - |


---

### `pages/components/my_info/emergency_contacts_components.py` <a id='pagescomponentsmy_infoemergency_contacts_componentspy'></a>

**Source File**: [emergency_contacts_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py)

<details>
<summary>Imports</summary>

```python
from constants.my_info_constants import Api_Endpoints, MyInfoConstants, EmergencyContacts
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from locators.components.my_info.emergency_contacts_locators import EmergencyContactsLocators
from pages.components.my_info.personal_details_components import PersonalDetailsComponent
from pages.base_page import BasePage
from pytest_pulse import step, pulse_step
```
</details>

#### Classes

##### class `EmergencyContactsComponent`
Link: [EmergencyContactsComponent](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L9)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L10) | `self, page` | - | - |
| [`click_on_emergency_contacts_tab`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L16) | `self` | - | - |
| [`fetch_emergency_contacts_from_api`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L22) | `self` | - | - |
| [`verify_emergency_contacts_ui`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L27) | `self, response` | - | - |
| [`add_emergency_contact`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L45) | `self, name, relationship, home_phone = None, mobile = None, work_phone = None` | - | - |
| [`delete_emergency_contact`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/emergency_contacts_components.py#L67) | `self, name` | - | - |


---

### `pages/components/my_info/personal_details_components.py` <a id='pagescomponentsmy_infopersonal_details_componentspy'></a>

**Source File**: [personal_details_components.py](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py)

<details>
<summary>Imports</summary>

```python
from constants.my_info_constants import Api_Endpoints
from utils.ui_helpers import UIHelpers
from constants.my_info_constants import MyInfoConstants
from locators.components.my_info.personal_details_locators import PersonalDetailsLocators
from pytest_pulse import pulse_step, step
from pages.base_page import BasePage
```
</details>

#### Classes

##### class `PersonalDetailsComponent`
Link: [PersonalDetailsComponent](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L7)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L8) | `self, page` | `None` | - |
| [`click_on_my_info_tab`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L14) | `self` | - | - |
| [`verify_employee_details`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L20) | `self` | - | - |
| [`fetch_employee_details_from_api`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L29) | `self` | - | - |
| [`verify_gender`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L34) | `self, gender` | - | - |
| [`verify_smoker_status`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L42) | `self, smoker` | - | - |
| [`validate_employee_details`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L50) | `self, response_json` | - | - |
| [`validate_custom_fields`](file:///Users/arghajitsingha/playwright-python/pages/components/my_info/personal_details_components.py#L90) | `self` | - | - |


---

### `pages/components/performance/performance_reviews_page.py` <a id='pagescomponentsperformanceperformance_reviews_pagepy'></a>

**Source File**: [performance_reviews_page.py](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py)

<details>
<summary>Imports</summary>

```python
from pages.base_page import BasePage
from locators.components.performance.performance_reviews_locators import PerformanceReviewsLocators
from constants.components.performance.performance_reviews_constants import PerformanceReviewsConstants
from pytest_pulse import step, pulse_step
```
</details>

#### Classes

##### class `PerformanceReviewsPage(BasePage)`
Link: [PerformanceReviewsPage](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L6)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L7) | `self, page` | - | - |
| [`navigate_to_page`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L12) | `self` | - | - |
| [`verify_page_loaded`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L16) | `self` | - | - |
| [`verify_search_inputs_and_action_buttons`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L21) | `self` | - | Verifies that all core search filter inputs and action buttons are fully visible. |
| [`get_live_performance_reviews`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L32) | `self` | `dict` | Navigates to page and intercepts the initial reviews response list payload. |
| [`get_first_employee_name_from_live_reviews`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L41) | `self` | `str` | Fetches live reviews and extracts the full name of the first employee if present. |
| [`fetch_performance_reviews_data`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L54) | `self, employee_name: str` | `dict` | Performs employee search and intercepts the dynamic reviews search response. |
| [`verify_records_exist`](file:///Users/arghajitsingha/playwright-python/pages/components/performance/performance_reviews_page.py#L66) | `self, response: dict` | - | Verify UI matches API response following the high-reliability blueprint |


---

### `pages/components/recruitment/candidates_page.py` <a id='pagescomponentsrecruitmentcandidates_pagepy'></a>

**Source File**: [candidates_page.py](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py)

<details>
<summary>Imports</summary>

```python
from pages.base_page import BasePage
from locators.components.recruitment.candidates_locators import RecruitmentCandidatesLocators
from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants
from pytest_pulse import pulse_step, step
```
</details>

#### Classes

##### class `RecruitmentCandidatesPage(BasePage)`
Link: [RecruitmentCandidatesPage](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L6)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L7) | `self, page` | - | - |
| [`navigate_via_menu`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L12) | `self` | - | - |
| [`verify_page_loaded`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L16) | `self` | - | - |
| [`fetch_candidates_data`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L21) | `self` | - | - |
| [`filter_candidates`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L29) | `self, job_title = None, vacancy = None, hiring_manager = None, status = None, candidate_name = None, keywords = None, date_from = None, date_to = None, method = None` | - | - |
| [`reset_filters`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L63) | `self` | - | - |
| [`verify_no_records_found`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L67) | `self, response` | - | - |
| [`verify_records_exist`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L72) | `self, response` | - | - |
| [`verify_candidate_reset`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L81) | `self, locator, value` | - | - |
| [`get_record_count_text`](file:///Users/arghajitsingha/playwright-python/pages/components/recruitment/candidates_page.py#L86) | `self` | - | - |


---

### `pages/components/time/timesheet_page.py` <a id='pagescomponentstimetimesheet_pagepy'></a>

**Source File**: [timesheet_page.py](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py)

<details>
<summary>Imports</summary>

```python
from locators.timesheet_locators import TimeSheetLocators
from constants.components.time.time_sheet_constants import TimeSheetConstants
from pages.base_page import BasePage
from pytest_pulse import step, pulse_step
time
```
</details>

#### Classes

##### class `TimeSheetPage`
Link: [TimeSheetPage](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L8)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L10) | `self, page` | - | - |
| [`navigate_to_timesheet_page`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L36) | `self` | - | - |
| [`verify_timesheet_page_loaded`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L41) | `self` | - | - |
| [`enter_employee_name`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L58) | `self, employee_name: str` | - | - |
| [`click_view_button`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L63) | `self` | - | - |
| [`get_records_count`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L68) | `self` | - | - |
| [`get_records_found_text`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L73) | `self` | - | - |
| [`verify_records_exist`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L78) | `self, api_response` | - | Verify UI matches API response - following blueprint pattern |
| [`click_view_first_timesheet`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L99) | `self` | - | Click the View button for the first timesheet in the table |
| [`verify_view_button_visible`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L111) | `self` | - | - |
| [`verify_employee_name_input_visible`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L116) | `self` | - | - |
| [`fetch_timesheet_data`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L122) | `self, employee_name: str` | `dict` | Performs search and returns API response using wait_for_api_call. This method encapsulates the action and API interce... |
| [`get_live_timesheet_employees`](file:///Users/arghajitsingha/playwright-python/pages/components/time/timesheet_page.py#L138) | `self` | `dict` | Navigates to timesheet page and captures the initial timesheets list response. |


---

### `pages/dashboard_page.py` <a id='pagesdashboard_pagepy'></a>

**Source File**: [dashboard_page.py](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py)

<details>
<summary>Imports</summary>

```python
from constants.common_constants import Attributes
from locators.dashboard_locators import DashboardLocators
from pages.base_page import BasePage
from constants.dashboard_page_constants import DashboardPageConstants
from pytest_pulse import step, pulse_step
```
</details>

#### Classes

##### class `DashboardPage`
Link: [DashboardPage](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L8)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L10) | `self, page` | - | - |
| [`verify_dashboard_page_url_title`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L15) | `self` | - | - |
| [`verify_dashboard_page_header`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L20) | `self` | - | - |
| [`verify_upgrade_button_is_visible`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L27) | `self` | - | - |
| [`verify_dashboard_widgets_count`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L35) | `self` | - | - |
| [`verify_dashboard_widgets_texts`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L42) | `self` | - | - |
| [`verify_profile_image_src`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L56) | `self` | - | - |
| [`capture_dashboard_screenshot_and_attach_to_report`](file:///Users/arghajitsingha/playwright-python/pages/dashboard_page.py#L74) | `self, pulse_attach, path: str = 'screenshots'` | - | - |


---

### `pages/directory_page.py` <a id='pagesdirectory_pagepy'></a>

**Source File**: [directory_page.py](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py)

<details>
<summary>Imports</summary>

```python
re
from playwright.sync_api import expect
from pytest_pulse import pulse_step
from constants.directory_constants import DirectoryConstants
from locators.directory_locators import DirectoryPageLocators
from utils.ui_helpers import UIHelpers
from pages.base_page import BasePage
from pytest_pulse import step
```
</details>

#### Classes

##### class `DirectoryPage`
Link: [DirectoryPage](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L11)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L12) | `self, page` | - | - |
| [`navigate_to_directory_page`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L18) | `self` | - | - |
| [`search_employee_by_name`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L35) | `self, name` | - | - |
| [`select_dropdown_for_job_title`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L43) | `self, job_title` | - | - |
| [`select_dropdown_for_location`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L57) | `self, location_name` | - | - |
| [`reset_search_form`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L71) | `self` | - | - |
| [`click_search_button`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L75) | `self` | - | - |
| [`get_live_directory_data`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L79) | `self` | `list` | Navigates to the directory page, captures the live API response, and returns the list of employee data dictionaries. |
| [`verify_single_employee_card`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L91) | `self, employee` | - | Takes a single employee's live API data and verifies that their specific UI card renders perfectly, including conditi... |
| [`verify_directory_card`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L116) | `self, expected_full_name: str, emp_number: str | int, live_job_title: str | None, live_subunit: str | None, live_location: str | None, card_locator_str: str, profile_img_locator_str: str, job_title_locator_str: str, card_body_locator_str: str, description_locator_str: str` | - | - |
| [`verify_employee_details_with_api_data`](file:///Users/arghajitsingha/playwright-python/pages/directory_page.py#L183) | `self, live_employees` | - | - |


---

### `pages/orangeHRM_login_page.py` <a id='pagesorangeHRM_login_pagepy'></a>

**Source File**: [orangeHRM_login_page.py](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py)

<details>
<summary>Imports</summary>

```python
from constants.dashboard_page_constants import DashboardPageConstants
from constants.login_page_constants import LoginPageConstants
from pages.base_page import BasePage
from locators.orangeHRM_login_locators import LoginPageLocators
from locators.orangeHRM_login_locators import LoginPageLocators
from playwright.sync_api import Page
os
from pytest_pulse import step
```
</details>

#### Classes

##### class `LoginPage`
Link: [LoginPage](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L11)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L13) | `self, page: Page` | - | - |
| [`login`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L21) | `self, username: str = os.getenv('USERNAME'), password: str = os.getenv('PASSWORD')` | - | - |
| [`enter_username`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L32) | `self, username: str` | - | - |
| [`enter_password`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L36) | `self, password: str` | - | - |
| [`fetch_demo_credentials`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L40) | `self` | - | - |
| [`go_to_login_page`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L56) | `self` | - | - |
| [`verify_orangehrm_logo_is_visible`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L60) | `self` | - | - |
| [`verify_page_header`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L64) | `self` | - | - |
| [`click_logout_button`](file:///Users/arghajitsingha/playwright-python/pages/orangeHRM_login_page.py#L72) | `self` | - | - |


---

## Pytest Suites

### `tests/orangehrm/components/admin/test_admin_filter.py` <a id='testsorangehrmcomponentsadmintest_admin_filterpy'></a>

**Source File**: [test_admin_filter.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/admin/test_admin_filter.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.admin.system_user_filter_components import SystemUserFilterComponents
from pytest_pulse import step, pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_admin_filter`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/admin/test_admin_filter.py#L17) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/claim/test_assign_claim.py` <a id='testsorangehrmcomponentsclaimtest_assign_claimpy'></a>

**Source File**: [test_assign_claim.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/claim/test_assign_claim.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.claim.assign_claim_page import AssignClaimPage
from pytest_pulse import step, pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_assign_claim_with_valid_data`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/claim/test_assign_claim.py#L16) | `page` | - | - |


---

### `tests/orangehrm/components/dashboard/test_help.py` <a id='testsorangehrmcomponentsdashboardtest_helppy'></a>

**Source File**: [test_help.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_help.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.dashboard.help_components import HelpComponents
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_help_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_help.py#L14) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_latest_posts.py` <a id='testsorangehrmcomponentsdashboardtest_latest_postspy'></a>

**Source File**: [test_latest_posts.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_latest_posts.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.dashboard.latest_posts_components import LatestPostsComponent
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_latest_posts_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_latest_posts.py#L15) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_leaves.py` <a id='testsorangehrmcomponentsdashboardtest_leavespy'></a>

**Source File**: [test_leaves.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_leaves.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.dashboard.leaves_components import LeavesComponent
```
</details>

#### Classes

##### class `TestLeaves`
Link: [TestLeaves](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_leaves.py#L6)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_about_me_ui_api_validation`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_leaves.py#L11) | `self, page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_location.py` <a id='testsorangehrmcomponentsdashboardtest_locationpy'></a>

**Source File**: [test_location.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_location.py)

<details>
<summary>Imports</summary>

```python
from pages.components.dashboard.location_components import LocationComponent
pytest
from pytest_pulse import pulse_step, step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_location_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_location.py#L15) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_my_actions.py` <a id='testsorangehrmcomponentsdashboardtest_my_actionspy'></a>

**Source File**: [test_my_actions.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_my_actions.py)

<details>
<summary>Imports</summary>

```python
from pages.components.dashboard.my_actions_components import MyActionsComponent
pytest
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_my_actions_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_my_actions.py#L14) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_quick_launch.py` <a id='testsorangehrmcomponentsdashboardtest_quick_launchpy'></a>

**Source File**: [test_quick_launch.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_quick_launch.py)

<details>
<summary>Imports</summary>

```python
from pages.components.dashboard.quick_launch_components import QuickLaunchComponent
pytest
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_quick_launch_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_quick_launch.py#L14) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/dashboard/test_subunit.py` <a id='testsorangehrmcomponentsdashboardtest_subunitpy'></a>

**Source File**: [test_subunit.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_subunit.py)

<details>
<summary>Imports</summary>

```python
from pages.components.dashboard.subunit_components import SubunitComponent
pytest
from pytest_pulse import pulse_step, step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_subunit_component`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/dashboard/test_subunit.py#L15) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/leave/test_leave_list.py` <a id='testsorangehrmcomponentsleavetest_leave_listpy'></a>

**Source File**: [test_leave_list.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/leave/test_leave_list.py)

<details>
<summary>Imports</summary>

```python
from constants.components.leave.leave_list_constants import LeaveListConstants
pytest
from pages.components.leave.leave_list_page import LeaveListPage
from locators.components.leave.leave_list_locators import LeaveListLocators
from pytest_pulse import pulse_step, step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_leave_list_no_records_with_random_filter`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/leave/test_leave_list.py#L11) | `page` | - | - |
| [`test_leave_list_reset_filters`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/leave/test_leave_list.py#L32) | `page` | - | - |
| [`test_leave_list_filter_by_status`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/leave/test_leave_list.py#L53) | `page` | - | - |


---

### `tests/orangehrm/components/performance/test_performance_reviews.py` <a id='testsorangehrmcomponentsperformancetest_performance_reviewspy'></a>

**Source File**: [test_performance_reviews.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/performance/test_performance_reviews.py)

<details>
<summary>Imports</summary>

```python
from constants.components.performance.performance_reviews_constants import PerformanceReviewsConstants
pytest
from pages.components.performance.performance_reviews_page import PerformanceReviewsPage
from locators.components.performance.performance_reviews_locators import PerformanceReviewsLocators
from pytest_pulse import pulse_step, step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_cookies')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_performance_reviews_basic_navigation_and_ui_elements`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/performance/test_performance_reviews.py#L13) | `page` | - | - |
| [`test_performance_reviews_records_display_based_on_api_response`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/performance/test_performance_reviews.py#L27) | `page` | - | - |


---

### `tests/orangehrm/components/pim/test_contact_details.py` <a id='testsorangehrmcomponentspimtest_contact_detailspy'></a>

**Source File**: [test_contact_details.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_contact_details.py)

<details>
<summary>Imports</summary>

```python
from pages.components.my_info.contact_details_components import ContactDetailsComponent
pytest
from pytest_pulse import step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_contact_details_ui_api_validation`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_contact_details.py#L13) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/pim/test_emergency_contacts.py` <a id='testsorangehrmcomponentspimtest_emergency_contactspy'></a>

**Source File**: [test_emergency_contacts.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_emergency_contacts.py)

<details>
<summary>Imports</summary>

```python
from pages.components.my_info.emergency_contacts_components import EmergencyContactsComponent
from constants.my_info_constants import EmergencyContactsTestData
pytest
from pytest_pulse import step, pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login', 'logout')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_emergency_contacts_ui_api_validation`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_emergency_contacts.py#L13) | `page, request_setup, login_via_api` | - | - |
| [`test_add_and_verify_emergency_contact`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_emergency_contacts.py#L23) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/pim/test_personal_details.py` <a id='testsorangehrmcomponentspimtest_personal_detailspy'></a>

**Source File**: [test_personal_details.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_personal_details.py)

<details>
<summary>Imports</summary>

```python
from pages.components.my_info.personal_details_components import PersonalDetailsComponent
pytest
from pytest_pulse import step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_personal_details_ui_api_validation`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/pim/test_personal_details.py#L13) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/components/recruitment/test_candidates.py` <a id='testsorangehrmcomponentsrecruitmenttest_candidatespy'></a>

**Source File**: [test_candidates.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/recruitment/test_candidates.py)

<details>
<summary>Imports</summary>

```python
from constants.components.recruitment.candidates_constants import RecruitmentCandidatesConstants
pytest
from pages.components.recruitment.candidates_page import RecruitmentCandidatesPage
from locators.components.recruitment.candidates_locators import RecruitmentCandidatesLocators
from pytest_pulse import pulse_step, step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_recruitment_candidates_no_records_with_random_filter`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/recruitment/test_candidates.py#L11) | `page` | - | - |
| [`test_recruitment_candidates_reset_filters`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/recruitment/test_candidates.py#L31) | `page` | - | - |


---

### `tests/orangehrm/components/time/test_timesheet.py` <a id='testsorangehrmcomponentstimetest_timesheetpy'></a>

**Source File**: [test_timesheet.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/time/test_timesheet.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.components.time.timesheet_page import TimeSheetPage
from pytest_pulse import pulse_step, step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'login_via_cookies', 'request_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_timesheet_page_basic_navigation_and_ui_elements`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/time/test_timesheet.py#L15) | `page` | - | - |
| [`test_timesheet_records_display_based_on_api_response`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/components/time/test_timesheet.py#L35) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/test_about_me.py` <a id='testsorangehrmtest_about_mepy'></a>

**Source File**: [test_about_me.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_about_me.py)

<details>
<summary>Imports</summary>

```python
from pytest_pulse import pulse_step, step
pytest
from pages.about_me_page import AboutMePage
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_about_me_ui_api_validation`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_about_me.py#L11) | `page, request_setup, login_via_api` | - | - |


---

### `tests/orangehrm/test_api.py` <a id='testsorangehrmtest_apipy'></a>

**Source File**: [test_api.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_api.py)

<details>
<summary>Imports</summary>

```python
from constants.api_constants import APIEndpoints
pytest
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_api', 'request_setup', 'base_api_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_api_orangehrm`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_api.py#L10) | `request_setup, login_via_api, base_api_setup` | - | - |


---

### `tests/orangehrm/test_dashboard.py` <a id='testsorangehrmtest_dashboardpy'></a>

**Source File**: [test_dashboard.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_dashboard.py)

<details>
<summary>Imports</summary>

```python
pytest
from pages.dashboard_page import DashboardPage
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_cookies')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_dashboard_page`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_dashboard.py#L10) | `page` | `None` | - |


---

### `tests/orangehrm/test_directory.py` <a id='testsorangehrmtest_directorypy'></a>

**Source File**: [test_directory.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_directory.py)

<details>
<summary>Imports</summary>

```python
from pages.base_page import BasePage
pytest
from pages.directory_page import DirectoryPage
from pytest_pulse import pulse_step, step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login_via_cookies')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_directory_page`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_directory.py#L13) | `page` | `None` | - |
| [`test_employee_directory_live_sync`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_directory.py#L34) | `page` | - | - |


---

### `tests/orangehrm/test_login.py` <a id='testsorangehrmtest_loginpy'></a>

**Source File**: [test_login.py](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_login.py)

<details>
<summary>Imports</summary>

```python
from pages.dashboard_page import DashboardPage
pytest
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('login', 'logout')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_login`](file:///Users/arghajitsingha/playwright-python/tests/orangehrm/test_login.py#L11) | `page, pulse_attach` | `None` | - |


---

### `tests/test_dummyjson_api.py` <a id='teststest_dummyjson_apipy'></a>

**Source File**: [test_dummyjson_api.py](file:///Users/arghajitsingha/playwright-python/tests/test_dummyjson_api.py)

<details>
<summary>Imports</summary>

```python
from constants.api_constants import APIEndpoints
pytest
from pytest_pulse import pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `pytestmark` | `pytest.mark.usefixtures('authentication_token', 'request_setup', 'base_api_setup')` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_api_authenticated_user`](file:///Users/arghajitsingha/playwright-python/tests/test_dummyjson_api.py#L12) | `request_setup, authentication_token, base_api_setup` | - | - |


---

### `tests/test_fail.py` <a id='teststest_failpy'></a>

**Source File**: [test_fail.py](file:///Users/arghajitsingha/playwright-python/tests/test_fail.py)

<details>
<summary>Imports</summary>

```python
pytest
from pytest_pulse import step
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`test_failed_action`](file:///Users/arghajitsingha/playwright-python/tests/test_fail.py#L9) | `page, pulse_step` | - | - |


---

### `tests/test_flaky.py` <a id='teststest_flakypy'></a>

**Source File**: [test_flaky.py](file:///Users/arghajitsingha/playwright-python/tests/test_flaky.py)

<details>
<summary>Imports</summary>

```python
pytest
os
from playwright.sync_api import Page
from pytest_pulse import step, pulse_step
```
</details>

#### Module-level Variables / Constants

| Name | Value |
| :--- | :--- |
| `COUNTER_FILE` | `'flaky_counter.tmp'` |


#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`get_and_increment_attempt`](file:///Users/arghajitsingha/playwright-python/tests/test_flaky.py#L10) | `` | - | - |
| [`test_flaky_orangehrm_social_link`](file:///Users/arghajitsingha/playwright-python/tests/test_flaky.py#L28) | `page: Page` | - | - |


---

### `tests/test_pulse_report.py` <a id='teststest_pulse_reportpy'></a>

**Source File**: [test_pulse_report.py](file:///Users/arghajitsingha/playwright-python/tests/test_pulse_report.py)

<details>
<summary>Imports</summary>

```python
re
pytest
from playwright.sync_api import expect
```
</details>

#### Module Functions

| Function | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`wait_for_fully_page_loaded`](file:///Users/arghajitsingha/playwright-python/tests/test_pulse_report.py#L6) | `page` | - | - |
| [`test_pulse_report_search`](file:///Users/arghajitsingha/playwright-python/tests/test_pulse_report.py#L17) | `page` | - | - |


---

## Utilities

### `utils/ui_helpers.py` <a id='utilsui_helperspy'></a>

**Source File**: [ui_helpers.py](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py)

<details>
<summary>Imports</summary>

```python
from datetime import datetime
from datetime import date
from babel import Locale
```
</details>

#### Classes

##### class `UIHelpers`
Link: [UIHelpers](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L6)

| Method | Signature | Return Type | Docstring |
| :--- | :--- | :--- | :--- |
| [`__init__`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L7) | `self, page` | - | - |
| [`convert_true_to_enable`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L10) | `self, status` | - | - |
| [`get_current_date`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L17) | `self` | - | - |
| [`convert_to_12_hour`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L21) | `self, time_24h: str` | `str` | Converts a 24-hour time string (HH:MM) to a 12-hour format with AM/PM.  Args:     time_24h (str): The time in 24-hour... |
| [`convert_date`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L43) | `self, date_str: str` | `str` | Converts a date string from yyyy-mm-dd to dd-mm-yyyy. |
| [`convert_date_to_dropdown_format`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L53) | `self, date_str: str` | `str` | Converts a date string from yyyy-mm-dd to yyyy-dd-mm. |
| [`get_country_name`](file:///Users/arghajitsingha/playwright-python/utils/ui_helpers.py#L63) | `self, country_code: str, locale_code: str = 'en'` | `str` | Get country name from country code. |


---
