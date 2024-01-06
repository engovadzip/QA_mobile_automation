import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
from selenium import webdriver
from dotenv import load_dotenv
import os


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()

    username = os.getenv('USER')
    userkey = os.getenv('KEY')
    remote_url = os.getenv('URL')

    return username, userkey, remote_url


@pytest.fixture(scope='session')
def android_set(load_env):
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "13.0",
        "deviceName": "Samsung Galaxy S23 Ultra",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Mobile autotests",
            "buildName": "android_wiki_build",
            "sessionName": "Android wiki autotest",

            "userName": load_env[0],
            "accessKey": load_env[1]
        }
    })

    browser.config.driver = webdriver.Remote(load_env[2], options=options)

    yield

    browser.quit()

@pytest.fixture(scope='session')
def ios_set(load_env):
    options = XCUITestOptions().load_capabilities({
        "platformName": "ios",
        "platformVersion": "17.0",
        "deviceName": "iPhone 15 Pro Max",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "Mobile autotests",
            "buildName": "ios_sample_build",
            "sessionName": "iOS sample app autotest",

            "userName": load_env[0],
            "accessKey": load_env[1]
        }
    })

    browser.config.driver = webdriver.Remote(load_env[2], options=options)

    yield

    browser.quit()