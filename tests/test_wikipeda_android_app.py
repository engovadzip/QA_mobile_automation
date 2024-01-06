import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_search_string_click(android_set):
    with allure.step('Click search string'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()


def test_type_search_request(android_set):
    with allure.step('Type "John Cena"'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('John Cena')


def test_open_article(android_set):
    with allure.step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('John Cena'))

    with allure.step("Open John Cena's article"):
        results.first.click()


@pytest.mark.xfail
def test_verify_article(android_set):
    with allure.step('Verify article'):
        browser.all((AppiumBy.ACCESSIBILITY_ID, "John Cena")).should(have.size_greater_than(0))
