from constants.components.dashboard import latest_posts_locators
from playwright.sync_api import expect, Locator
from pytest_pulse import pulse_step, step


class BasePage:

    def __init__(self, page):
        self.page = page

    def waitForFullyPageLoad(self):
        with pulse_step("Wait for full page load"):
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_load_state("load")

    def navigateToUrl(self, url: str):
        with pulse_step("Navigate to the url"):
            self.page.goto(url)
            self.waitForFullyPageLoad()

    def click(self, locator: str | Locator, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and Clicking on it"):
                self.page.locator(locator).nth(index).click()
                self.waitForFullyPageLoad()
        else:
            with pulse_step("Got Direct Locator, Clicking on it"):
                locator.nth(index).click()
                self.waitForFullyPageLoad()

    def fill(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and Filling it"):
                self.page.locator(locator).nth(index).fill(text)
                self.waitForFullyPageLoad()
        else:
            with pulse_step("Got Direct Locator, Filling it"):
                locator.nth(index).fill(text)
                self.waitForFullyPageLoad()

    def verify_page_title(self, title: str):
        with pulse_step("Verifying page title"):
            expect(self.page).to_have_title(title)

    def verify_element_is_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_visible()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_visible()

    def verify_element_is_not_visible(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_hidden()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_hidden()

    def verify_element_is_enabled(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_enabled()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_enabled()

    def verify_element_is_disabled(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_disabled()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_disabled()

    def verify_element_is_checked(self, locator: str | Locator):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator)).to_be_checked()
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator).to_be_checked()

    def verify_element_text(self, locator: str | Locator, text: str, index: int = 0):
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and verifying it"):
                expect(self.page.locator(locator).nth(index)).to_have_text(text)
        else:
            with pulse_step("Got Direct Locator, Verifying it"):
                expect(locator.nth(index)).to_have_text(text)

    def verify_page_url(self, url: str):
        with pulse_step("Verify page url"):
            self.waitForFullyPageLoad()
            expect(self.page).to_have_url(url)

    def get_element_count(self, locator: str | Locator) -> int:
        if isinstance(locator, str):
            with pulse_step("Generating Locator from string and getting element count"):
                return self.page.locator(locator).count()
        else:
            with pulse_step("Got Direct Locator, Getting element count"):
                return locator.count()

    def verify_element_count(self, locator: str | Locator, count: int):
        if isinstance(locator, str):
            with pulse_step(
                "Generating Locator from string and verifying element count"
            ):
                expect(self.page.locator(locator)).to_have_count(count)
        else:
            with pulse_step("Got Direct Locator, Verifying element count"):
                expect(locator).to_have_count(count)

    def get_all_element_texts(self, locator: str | Locator):
        with pulse_step("Getting all element texts"):
            count = self.get_element_count(locator)
            if count == 0:
                raise ValueError("No elements found with the given locator")
            texts = []
            for i in range(count):
                texts.append(self.page.locator(locator).nth(i).inner_text())
        return texts

    def verify_all_element_texts(
        self, locator: str | Locator, expected_texts: list[str]
    ):
        with pulse_step("Generating Locator from string and verifying element texts"):
            actual_texts = self.get_all_element_texts(locator)
            self.verify_equal(actual_texts, expected_texts)

    def verify_element_texts_contains(
        self, locator: str | Locator, expected_texts: str
    ):
        with pulse_step(
            "Generating Locator from string and verifying element texts contains"
        ):
            actual_texts = self.get_all_element_texts(locator)
            self.verify_equal(actual_texts, expected_texts)

    def verify_equal(self, actual, expected):
        with pulse_step("Verifying equal"):
            assert actual == expected, f"{actual} != {expected}"

    def expect_contains(self, actual: str, expected: str):
        with pulse_step("Expecting text contains"):
            assert expected in actual, f"Expected '{expected}' to be in '{actual}'"

    def get_attribute(self, locator: str | Locator, attribute: str, index: int = 0):
        with pulse_step("Getting attribute"):
            if isinstance(locator, str):
                return self.page.locator(locator).nth(index).get_attribute(attribute)
            else:
                return locator.nth(index).get_attribute(attribute)

    def verify_element_text_ignore_case(
        self, locator: str | Locator, text: str, index: int = 0
    ):
        with pulse_step("Verifying element text ignore case"):
            if isinstance(locator, str):
                expect(self.page.locator(locator).nth(index)).to_have_text(
                    text, ignore_case=True
                )
            else:
                expect(locator.nth(index)).to_have_text(text, ignore_case=True)

    def verify_element_text_contains(
        self, locator: str | Locator, expected_text: str, index: int = 0
    ):
        with pulse_step("Get actual text"):
            if isinstance(locator, str):
                actual_text = self.page.locator(locator).nth(index).inner_text()
            else:
                actual_text = locator.nth(index).inner_text()

        with pulse_step("Verify text contains"):
            self.expect_contains(actual_text, expected_text)

    def capture_screenshot(self, path: str = "screenshots"):
        with pulse_step("Capturing full pagescreenshot"):
            self.page.screenshot(path=path, full_page=True)

    def verify_attribute_value_contains(
        self,
        locator: str | Locator,
        attribute: str,
        expected_value: str,
        index: int = 0,
    ):
        with pulse_step("Get actual attribute value"):
            actual_value = self.get_attribute(locator, attribute, index)

        with pulse_step("Verify attribute value contains"):
            self.expect_contains(actual_value, expected_value)

    def wait_for_api_call(self, action, url: str, success_status: int = 200):
        with pulse_step("Start waiting for the specific API call"):
            with self.page.expect_response(url) as response_info:
                # Perform the action that triggers the API
                if callable(action):
                    action()
                else:
                    action

        # Extract the response object once it completes
        response = response_info.value

        # Perform assertions on the real response
        assert response.status == success_status
        res_json = response.json()
        if "success" in res_json:
            assert res_json["success"] is True
        return res_json

    def autocomplete_dropdown(self, locator, text):
        autocomplete_input = self.page.locator(locator)
        autocomplete_input.click()

        # 3. Type the text sequentially.
        # Using press_sequentially instead of fill() is crucial for autocompletes,
        # as it simulates real keystrokes which triggers the frontend to fetch the hints.
        autocomplete_input.press_sequentially(text, delay=100)

        # 4. Wait for the loading spinner to disappear (if applicable)
        # expect(page.locator(".oxd-autocomplete-spinner")).not_to_be_visible()

        # 5. Locate the dropdown option that appears and click it.
        # We use get_by_role here because modern frameworks use ARIA roles for dropdowns.
        # If role="option" isn't used by the HTML, you can use a text locator.
        target_option = self.page.locator(".oxd-autocomplete-dropdown").get_by_text(
            text
        )

        # Ensure it's visible before clicking
        expect(target_option).to_be_visible()
        target_option.click()

        # 6. Verification (Optional): Check that the input now contains the selected value
        import re

        expect(autocomplete_input).to_have_value(re.compile(text))

    def verify_directory_card(
        self,
        expected_full_name: str,
        emp_number: str | int,
        live_job_title: str | None,
        live_subunit: str | None,
        live_location: str | None,
        card_locator_str: str,
        profile_img_locator_str: str,
        job_title_locator_str: str,
        card_body_locator_str: str,
        description_locator_str: str,
    ):
        with pulse_step(f"Verifying card details for {expected_full_name}"):
            # 1. Scope to Specific Card
            card = self.page.locator(card_locator_str).filter(has_text=expected_full_name)
            expect(card).to_be_visible()

            # 2. Profile Picture Verification
            profile_img = card.locator(profile_img_locator_str)
            import re
            expect(profile_img).to_have_attribute(
                "src", re.compile(f"empNumber/{emp_number}")
            )

            # 3. Conditional Rendering: Job Title
            job_title_locator = card.locator(job_title_locator_str)
            if live_job_title:
                expect(job_title_locator).to_be_visible()
                expect(job_title_locator).to_have_text(live_job_title)
            else:
                expect(job_title_locator).to_be_hidden()

            # 4. Conditional Rendering: Subunit and Location
            card_body = card.locator(card_body_locator_str)

            # If both are null, the entire body container is hidden in the DOM
            if not live_subunit and not live_location:
                expect(card_body).to_be_hidden()
            else:
                # The body container must be visible if at least one exists
                expect(card_body).to_be_visible()

                # Check Subunit
                if live_subunit:
                    subunit_desc = card_body.locator(
                        description_locator_str, has_text=live_subunit
                    )
                    expect(subunit_desc).to_be_visible()

                # Check Location
                if live_location:
                    location_desc = card_body.locator(
                        description_locator_str, has_text=live_location
                    )
                    expect(location_desc).to_be_visible()
