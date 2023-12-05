import pytest

from selene import Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope='function')
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'
    #browser.config.hold_driver_at_exit = True
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    options = Options()
    selenoid_capabilities = {
        'browserName': 'chrome',
        'browserVersion': '100.0',
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f'https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser = Browser(Config(driver))

    yield

    browser.quit()
