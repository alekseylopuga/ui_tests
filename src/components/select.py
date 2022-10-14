from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser


class Select:

    def __init__(self):
        pass

    def open_dropdown(self, name):
        field = browser.element(by.xpath(f"//select[@id='{name}']")).with_(Config(timeout=5))
        field.click()

    def select_option(self, name):
        field = browser.element(by.xpath(f"//option[contains(text(), '{name}')]")).with_(Config(timeout=5))
        field.click()

    def dropdown_should_be_visible(self, name):
        field = browser.element(by.xpath(f"//input[@id='{name}']")).with_(Config(timeout=5))
        field.should_be(visible)

    def dropdown_should_not_be_visible(self, name):
        field = browser.element(by.xpath(f"//input[@id='{name}']")).with_(Config(timeout=5))
        field.should_be(visible.not_)
