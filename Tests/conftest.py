import pytest
from selene import browser


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.hold_driver_at_exit = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield

    browser.quit()
