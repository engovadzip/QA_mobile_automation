import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function')
def android_set():
    username = os.getenv('USER')
    userkey = os.getenv('KEY')
    remote_url = os.getenv('URL')

    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Mobile autotests",
            "buildName": "android_wiki_build",
            "sessionName": "Android wiki autotest",

            "userName": username,
            "accessKey": userkey
        }
    })

    browser.config.driver_remote_url = remote_url
    browser.config.driver_options = options

    yield

    browser.quit()

@pytest.fixture(scope='function')
def ios_set():
    username = os.getenv('USER')
    userkey = os.getenv('KEY')
    remote_url = os.getenv('URL')

    options = XCUITestOptions().load_capabilities({
        "platformName": "ios",
        "platformVersion": "17.0",
        "deviceName": "iPhone 15 Pro Max",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Mobile autotests",
            "buildName": "ios_sample_build",
            "sessionName": "iOS sample app autotest",

            "userName": username,
            "accessKey": userkey
        }
    })

    browser.config.driver_remote_url = remote_url
    browser.config.driver_options = options

    yield

    browser.quit()

