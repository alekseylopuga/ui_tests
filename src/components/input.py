from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser


class Input:

    def __init__(self):
        pass

    def enter_text(self, name, text):
        field = browser.element(by.xpath(
            f"//label[contains(text(), 'Amount to be {name}')]/../input")).with_(Config(timeout=5))
        field.type(text)

    def field_should_be_visible(self, name):
        field = browser.element(by.xpath(
            f"//label[contains(text(), 'Amount to be {name}')]/../input")).with_(Config(timeout=5))
        field.should_be(visible)

    def field_should_not_be_visible(self, name):
        field = browser.element(by.xpath(
            f"//label[contains(text(), 'Amount to be {name}')]/../input")).with_(Config(timeout=5))
        field.should_be(visible.not_)
