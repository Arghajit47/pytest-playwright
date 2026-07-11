from pages.base_page import BasePage
from locators.components.buzz.buzz_locators import BuzzLocators
from constants.components.buzz.buzz_constants import BuzzConstants
from pytest_pulse import step, pulse_step


class BuzzPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.base_page = BasePage(page)

    # ------------------------------------------------------------------
    # Navigation
    # ------------------------------------------------------------------

    @step("Navigate to Buzz page")
    def navigate_to_page(self):
        with pulse_step("Navigating to Buzz page via direct URL"):
            self.navigateToUrl(BuzzConstants.BUZZ_URL)
            self.base_page.wait_for_fully_page_loaded()

    @step("Verify Buzz page is loaded")
    def verify_page_loaded(self):
        with pulse_step("Verifying Buzz page heading is visible"):
            self.verify_element_is_visible(BuzzLocators.PAGE_HEADING)

    # ------------------------------------------------------------------
    # Modular UI getters (return data, no assertions)
    # ------------------------------------------------------------------

    def is_element_present(self, locator: str, timeout_ms: int = 5000, retries: int = 5) -> bool:
        """Polls for element presence. Returns True/False, never raises."""
        count = self._wait_for_elements(locator, timeout_ms, retries)
        return count > 0

    def get_element_count_safe(self, locator: str, timeout_ms: int = 5000, retries: int = 5) -> int:
        """Waits for elements then returns count. Returns 0 if none found."""
        return self._wait_for_elements(locator, timeout_ms, retries)

    def is_heading_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.PAGE_HEADING)

    def is_newsfeed_title_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.NEWSFEED_TITLE)

    def is_post_input_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.POST_INPUT)

    def is_post_button_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.POST_BUTTON)

    def is_share_photos_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.SHARE_PHOTOS_BUTTON)

    def is_share_video_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.SHARE_VIDEO_BUTTON)

    def is_most_recent_filter_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.MOST_RECENT_POSTS_BUTTON)

    def is_most_liked_filter_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.MOST_LIKED_POSTS_BUTTON)

    def is_most_commented_filter_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.MOST_COMMENTED_POSTS_BUTTON)

    def get_post_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.BUZZ_POST)

    def wait_for_post_count(self, expected_count: int, timeout_ms: int = 10000, retries: int = 10) -> int:
        """Polls until UI post count matches expected, or retries exhausted."""
        return self._wait_for_elements(
            BuzzLocators.BUZZ_POST, timeout_ms, retries, expected_count=expected_count
        )

    def get_post_employee_name_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.POST_EMPLOYEE_NAME)

    def get_post_body_text_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.POST_BODY_TEXT)

    def get_like_button_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.LIKE_BUTTON)

    def get_comment_button_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.COMMENT_BUTTON)

    def get_share_button_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.SHARE_BUTTON)

    def get_post_stats_row_count(self) -> int:
        return self.get_element_count_safe(BuzzLocators.POST_STATS_ROW)

    def is_no_posts_available_visible(self) -> bool:
        return self.is_element_present(BuzzLocators.NO_POSTS_AVAILABLE)

    def get_all_post_body_texts(self) -> list:
        """Returns list of post body text strings. Raises ValueError if no posts."""
        return self.base_page.get_all_element_texts(BuzzLocators.POST_BODY_TEXT)

    # ------------------------------------------------------------------
    # Modular API helpers (return extracted data, no assertions)
    # ------------------------------------------------------------------

    @staticmethod
    def get_api_post_count(response: dict) -> int:
        """Returns the number of posts in the API response data array."""
        data = response.get("data", [])
        return len(data) if isinstance(data, list) else 0

    @staticmethod
    def get_api_total_count(response: dict) -> int | None:
        """Returns the 'meta.total' from the API response, or None if absent."""
        meta = response.get("meta", {})
        if isinstance(meta, dict):
            return meta.get("total")
        return None

    @staticmethod
    def get_created_post_id(response: dict):
        """Returns the post id from a create-post API response, or None."""
        data = response.get("data", {})
        if not isinstance(data, dict):
            return None
        post = data.get("post", {})
        if not isinstance(post, dict):
            return None
        return post.get("id")

    @staticmethod
    def get_deleted_share_id(response: dict):
        """Returns the shareId from a delete-post API response, or None."""
        data = response.get("data", {})
        if not isinstance(data, dict):
            return None
        return data.get("shareId")

    @staticmethod
    def is_text_in_post_list(post_texts: list, expected_text: str) -> bool:
        """Returns True if expected_text is found in any of the post_texts."""
        return any(expected_text in t for t in post_texts)

    # ------------------------------------------------------------------
    # API-intercepting action methods (return raw API response)
    # ------------------------------------------------------------------

    @step("Get live Buzz feed via API")
    def get_live_buzz_feed(self) -> dict:
        """Navigates to Buzz page and intercepts the initial feed response.

        Uses page.goto() directly (without wait_for_fully_page_loaded) inside
        the expect_response block to avoid the response body being garbage-collected
        before response.json() is called.
        """
        response = self.base_page.wait_for_api_call(
            lambda: self.page.goto(BuzzConstants.BUZZ_URL),
            BuzzConstants.BUZZ_FEED_API_ENDPOINT,
        )
        self.base_page.wait_for_fully_page_loaded()
        return response

    @step("Click Most Liked Posts filter and intercept API")
    def click_most_liked_posts(self) -> dict:
        with pulse_step("Clicking Most Liked Posts filter button"):
            response = self.base_page.wait_for_api_call(
                lambda: self.click(BuzzLocators.MOST_LIKED_POSTS_BUTTON),
                BuzzConstants.BUZZ_FEED_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    @step("Click Most Commented Posts filter and intercept API")
    def click_most_commented_posts(self) -> dict:
        with pulse_step("Clicking Most Commented Posts filter button"):
            response = self.base_page.wait_for_api_call(
                lambda: self.click(BuzzLocators.MOST_COMMENTED_POSTS_BUTTON),
                BuzzConstants.BUZZ_FEED_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    @step("Click Most Recent Posts filter and intercept API")
    def click_most_recent_posts(self) -> dict:
        with pulse_step("Clicking Most Recent Posts filter button"):
            response = self.base_page.wait_for_api_call(
                lambda: self.click(BuzzLocators.MOST_RECENT_POSTS_BUTTON),
                BuzzConstants.BUZZ_FEED_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    # ------------------------------------------------------------------
    # Post creation
    # ------------------------------------------------------------------

    @step("Create a post via the UI and intercept the API response")
    def create_post(self, post_text: str) -> dict:
        """Types text into the Buzz post input, clicks Post, and intercepts the POST API response."""
        with pulse_step("Filling post input with test text"):
            self.fill(BuzzLocators.POST_INPUT, post_text)

        with pulse_step("Clicking Post button and intercepting create-post API"):
            response = self.base_page.wait_for_api_call(
                lambda: self.click(BuzzLocators.POST_BUTTON),
                BuzzConstants.BUZZ_CREATE_POST_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    # ------------------------------------------------------------------
    # Post deletion
    # ------------------------------------------------------------------

    @step("Delete the most recent post via the UI and intercept the API response")
    def delete_most_recent_post(self) -> dict:
        """Opens the three-dots menu on the first post, selects Delete Post,
        confirms in the dialog, and intercepts the DELETE API response."""
        with pulse_step("Opening the post config (three-dots) menu for the first post"):
            self.click(BuzzLocators.POST_CONFIG_BUTTON, index=0)
            self.wait_for_timeout(1000)

        with pulse_step("Clicking 'Delete Post' menu item"):
            self.click(BuzzLocators.DELETE_POST_MENU_ITEM)

        with pulse_step("Clicking Yes, Delete in the confirmation dialog and intercepting DELETE API"):
            self.wait_for_timeout(500)
            response = self.base_page.wait_for_api_call(
                lambda: self.click(BuzzLocators.DELETE_DIALOG_BUTTON),
                BuzzConstants.BUZZ_DELETE_POST_API_ENDPOINT,
            )
        self.base_page.wait_for_fully_page_loaded()
        return response

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _wait_for_elements(self, locator, timeout_ms=5000, retries=5, expected_count=None):
        """Wait for elements to render by polling with wait_for_timeout.

        If expected_count is provided, waits until the count matches (or retries exhausted).
        Otherwise, waits until any elements appear (> 0).
        """
        for _ in range(retries):
            count = self.get_element_count(locator)
            if expected_count is not None:
                if count == expected_count:
                    return count
            elif count > 0:
                return count
            self.wait_for_timeout(timeout_ms // retries)
        return self.get_element_count(locator)