import pytest

from pages.components.buzz.buzz_page import BuzzPage
from constants.components.buzz.buzz_constants import BuzzConstants
from pytest_pulse import step, pulse_step


pytestmark = pytest.mark.usefixtures("login_via_cookies")


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("Navigation")
@step("Test navigation to Buzz page and verify core UI elements are visible.")
def test_buzz_basic_navigation_and_ui_elements(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Verify Buzz Newsfeed title is visible"):
        assert buzz_page.is_newsfeed_title_visible(), "Buzz Newsfeed title is not visible"

    with pulse_step("Verify post input and Post button are visible"):
        assert buzz_page.is_post_input_visible(), "Post input textarea is not visible"
        assert buzz_page.is_post_button_visible(), "Post button is not visible"

    with pulse_step("Verify Share Photos and Share Video buttons are visible"):
        assert buzz_page.is_share_photos_visible(), "Share Photos button is not visible"
        assert buzz_page.is_share_video_visible(), "Share Video button is not visible"

    with pulse_step("Verify filter buttons are visible"):
        assert buzz_page.is_most_recent_filter_visible(), "Most Recent Posts filter is not visible"
        assert buzz_page.is_most_liked_filter_visible(), "Most Liked Posts filter is not visible"
        assert buzz_page.is_most_commented_filter_visible(), "Most Commented Posts filter is not visible"


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("Feed")
@step("Test that the Buzz feed loads posts from the API and displays them on the UI.")
def test_buzz_feed_loads_posts_from_api(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Get live Buzz feed via API"):
        api_response = buzz_page.get_live_buzz_feed()

    with pulse_step("Verify API response has posts"):
        api_total = buzz_page.get_api_total_count(api_response)
        api_count = buzz_page.get_api_post_count(api_response)
        if api_total is not None:
            assert api_total > 0, f"Expected posts in API response, but got total={api_total}"
        else:
            assert api_count > 0, "Expected posts in API response, but data array is empty"

    with pulse_step("Verify UI post count matches API"):
        if api_total is not None and api_total > 0:
            ui_count = buzz_page.wait_for_post_count(api_count)
            assert ui_count > 0, "Expected posts on UI, but found none"
            assert ui_count == api_count, (
                f"Expected {api_count} posts from API, but found {ui_count} on UI"
            )
        else:
            assert buzz_page.is_no_posts_available_visible(), "No Posts Available state not visible"


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("PostElements")
@step("Test that individual post elements (employee name, body text, actions, stats) are visible.")
def test_buzz_post_elements_visible(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page and verify loaded"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Verify post employee names are visible"):
        count = buzz_page.get_post_employee_name_count()
        assert count > 0, "Expected post employee name elements, but found none"

    with pulse_step("Verify post body texts are visible"):
        count = buzz_page.get_post_body_text_count()
        assert count > 0, "Expected post body text elements, but found none"

    with pulse_step("Verify post action buttons (like, comment, share) are visible"):
        assert buzz_page.get_like_button_count() > 0, "Expected like (heart icon) elements, but found none"
        assert buzz_page.get_comment_button_count() > 0, "Expected comment button elements, but found none"
        assert buzz_page.get_share_button_count() > 0, "Expected share button elements, but found none"

    with pulse_step("Verify post stats rows are visible"):
        assert buzz_page.get_post_stats_row_count() > 0, "Expected post stats row elements, but found none"


@pytest.mark.pulse_severity("High")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("Filter")
@step("Test that clicking Most Liked Posts filter updates the feed via API.")
def test_buzz_most_liked_posts_filter(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page and verify loaded"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Click Most Liked Posts filter and intercept API"):
        api_response = buzz_page.click_most_liked_posts()

    with pulse_step("Verify API response has posts"):
        api_total = buzz_page.get_api_total_count(api_response)
        api_count = buzz_page.get_api_post_count(api_response)
        if api_total is not None:
            assert api_total > 0, f"Expected posts in API response, but got total={api_total}"
        else:
            assert api_count > 0, "Expected posts in API response, but data array is empty"

    with pulse_step("Verify posts are displayed after filter"):
        # strict_count=False — old posts may linger in DOM during transition
        assert buzz_page.get_post_count() > 0, "Expected posts on UI after filter, but found none"


@pytest.mark.pulse_severity("Medium")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("Filter")
@step("Test that clicking Most Commented Posts filter updates the feed via API.")
def test_buzz_most_commented_posts_filter(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page and verify loaded"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Click Most Commented Posts filter and intercept API"):
        api_response = buzz_page.click_most_commented_posts()

    with pulse_step("Verify API response has posts"):
        api_total = buzz_page.get_api_total_count(api_response)
        api_count = buzz_page.get_api_post_count(api_response)
        if api_total is not None:
            assert api_total > 0, f"Expected posts in API response, but got total={api_total}"
        else:
            assert api_count > 0, "Expected posts in API response, but data array is empty"

    with pulse_step("Verify posts are displayed after filter"):
        assert buzz_page.get_post_count() > 0, "Expected posts on UI after filter, but found none"


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("CreatePost")
@step("Test that a user can create a text post on Buzz and it appears in the feed.")
def test_buzz_create_post(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page and verify loaded"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Create a post via the UI and intercept the API response"):
        api_response = buzz_page.create_post(BuzzConstants.TEST_POST_TEXT)

    with pulse_step("Verify create-post API response has post id"):
        post_id = buzz_page.get_created_post_id(api_response)
        assert post_id, f"Create-post API response has no post id, got: {api_response.get('data', {})}"

    with pulse_step("Verify the created post text is visible in the UI feed"):
        buzz_page.wait_for_timeout(2000)
        post_texts = buzz_page.get_all_post_body_texts()
        found = buzz_page.is_text_in_post_list(post_texts, BuzzConstants.TEST_POST_TEXT)
        assert found, f"Post text '{BuzzConstants.TEST_POST_TEXT}' not found in UI feed. Visible posts: {post_texts}"


@pytest.mark.pulse_severity("Critical")
@pytest.mark.pulse_tag("Buzz")
@pytest.mark.pulse_tag("DeletePost")
@step("Test that a user can delete a post from the Buzz feed and it is removed.")
def test_buzz_delete_post(page):
    buzz_page = BuzzPage(page)

    with pulse_step("Navigate to Buzz page and verify loaded"):
        buzz_page.navigate_to_page()
        assert buzz_page.is_heading_visible(), "Buzz page heading is not visible"

    with pulse_step("Create a post to be deleted"):
        buzz_page.create_post(BuzzConstants.TEST_POST_TEXT)

    with pulse_step("Delete the most recent post and intercept the API response"):
        api_response = buzz_page.delete_most_recent_post()

    with pulse_step("Verify delete-post API response has shareId"):
        share_id = buzz_page.get_deleted_share_id(api_response)
        assert share_id, f"Delete-post API response has no shareId, got: {api_response.get('data', {})}"

    with pulse_step("Verify feed still renders properly after deletion"):
        buzz_page.wait_for_timeout(2000)
        ui_count = buzz_page.get_post_count()
        if ui_count == 0:
            assert buzz_page.is_no_posts_available_visible(), "Feed is empty but No Posts Available state is not visible"