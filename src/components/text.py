from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser


class Text:

    def __init__(self):
        pass

    def header_should_be_visible(self):
        button = browser.element(by.xpath(f"//*[@class='mainHeading'][text()='XYZ Bank']")).with_(Config(timeout=5))
        button.should_be(visible)
