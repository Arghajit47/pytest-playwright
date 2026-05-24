import pytest
from pages.components.dashboard.help_components import HelpComponents
from pytest_pulse import pulse_step

pytestmark = pytest.mark.usefixtures(
    "login_via_api", "login_via_cookies", "request_setup"
)


@pytest.mark.pulse_severity("Minor")
@pytest.mark.pulse_tag("Regression")
@pytest.mark.pulse_tag("Dashboard")
@pytest.mark.pulse_tag("Help")
def test_help_component(page, request_setup, login_via_api):
    with pulse_step("Instantiate Help Component"):
        help_component = HelpComponents(page)
        help_component.verify_help_icon_is_visible()
        help_component.click_help_button()
        help_component.verify_help_url()
