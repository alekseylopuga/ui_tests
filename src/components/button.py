from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser


class Button:

    def __init__(self):
        pass

    def click_on_the_button(self, name):
        button = browser.element(by.xpath(f"//*[contains(@ng-click, '{name}')]")).with_(Config(timeout=5))
        button.click()

    def button_should_be_visible(self, name):
        button = browser.element(by.xpath(f"//*[contains(@ng-click, '{name}')]")).with_(Config(timeout=5))
        button.should_be(visible)

    def button_should_not_be_visible(self, name):
        button = browser.element(by.xpath(f"//*[contains(@ng-click, '{name}')]")).with_(Config(timeout=5))
        button.should_be(visible.not_)

    def click_on_the_submit_button(self, name):
        button = browser.element(by.xpath(
            f"//button[@type='submit'][contains(text(), '{name}')]")).with_(Config(timeout=5))
        button.click()

    def sumbit_button_should_be_visible(self, name):
        button = browser.element(by.xpath(
            f"//button[@type='submit'][contains(text(), '{name}')]")).with_(Config(timeout=5))
        button.should_be(visible)

    def submit_button_should_not_be_visible(self, name):
        button = browser.element(by.xpath(
            f"//button[@type='submit'][contains(text(), '{name}')]")).with_(Config(timeout=5))
        button.should_be(visible.not_)
