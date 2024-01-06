import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import be, browser
import allure


results = []

def test_sample_app(ios_set):
    with allure.step('Check the text elements'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'UI Elements')).should(be.visible)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text')).should(be.visible)
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Alert')).should(be.visible)