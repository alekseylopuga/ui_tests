from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser

from src.components.button import Button
from src.components.text import Text

START_DATE = browser.element(
    by.xpath(f"//input[@id='start']")).with_(Config(timeout=5))
END_DATE = browser.element(
            by.xpath(f"//input[@id='end']")).with_(Config(timeout=5))
TABLE_TRANSACTIONS = browser.element(
            by.xpath(f"//tbody//tr")).with_(Config(timeout=5))


class Transactions:

    def __init__(self):
        self.home_button = Button().button_should_be_visible('home')
        self.logout_button = Button().button_should_be_visible('byebye')
        self.back_button = Button().button_should_be_visible('back')
        self.bank_name = Text().header_should_be_visible()
        self.data = browser.element(by.xpath(
            f"//a[contains(text(), 'Date-Time')]")).with_(Config(timeout=5))
        self.data.should_be(visible)
        self.amount = browser.element(by.xpath(
            f"//a[contains(text(), 'Amount')]")).with_(Config(timeout=5))
        self.amount.should_be(visible)
        self.transaction_type = browser.element(by.xpath(
            f"//a[contains(text(), 'Transaction Type')]")).with_(Config(timeout=5))
        self.transaction_type.should_be(visible)

    def transaction_should_be_visible(self, index_field, amount, transaction_type):
        Button().button_should_be_visible('reset')
        Button().button_should_be_visible('scrollRight')
        START_DATE.should_be(visible)
        END_DATE.should_be(visible)
        amount_field = browser.element(
            by.xpath(f"//tr[@id='anchor{index_field}']//td[2][text()= '{amount}']")).with_(Config(timeout=5))
        amount_field.should_be(visible)
        transaction_type_field = browser.element(
            by.xpath(f"//tr[@id='anchor{index_field}']//td[3][text()= '{transaction_type}']")).with_(Config(timeout=5))
        transaction_type_field.should_be(visible)

    def table_should_be_empty_before_re_opening(self):
        Button().button_should_be_visible('reset')
        Button().button_should_be_visible('scrollRight')
        TABLE_TRANSACTIONS.should_be(visible.not_)
        START_DATE.should_be(visible)
        END_DATE.should_be(visible)

    def table_should_be_empty_after_re_opening(self):
        Button().button_should_not_be_visible('reset')
        Button().button_should_not_be_visible('scrollRight')
        START_DATE.should_be(visible.not_)
        END_DATE.should_be(visible.not_)
        TABLE_TRANSACTIONS.should_be(visible.not_)

    def click_on_the_button(self, button_name):
        Button().click_on_the_button(button_name)
