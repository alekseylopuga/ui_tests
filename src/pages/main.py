import time

from selene import by, Config
from selene.support.conditions.be import visible
from selene.support.shared import browser

from src.components.button import Button
from src.components.select import Select
from src.components.text import Text
from src.components.input import Input


class Main:

    def __init__(self, user_name):
        self.home_button = Button().button_should_be_visible('home')
        self.logout_button = Button().button_should_be_visible('byebye')
        self.transaction_button = Button().button_should_be_visible('transactions')
        self.deposit_button = Button().button_should_be_visible('deposit')
        self.withdrawal_button = Button().button_should_be_visible('withdrawl')
        self.bank_name = Text().header_should_be_visible()
        self.user_name = browser.element(by.xpath(
            f"//*[contains(@class, 'fontBig')][text()='{user_name}']")).with_(Config(timeout=5))
        self.user_name.should_be(visible)

    def make_transaction(self, account_number, currency, type_of_transaction, amount_field, amount, submit,
                         expected_message):
        Select().open_dropdown('accountSelect')
        Select().select_option(account_number)
        account = browser.element(
            by.xpath(f"//*[@class='center'][contains(text(), 'Account Number')]//strong[contains(text(), "
                     f"'{account_number}')]")).with_(Config(timeout=5))
        account.should_be(visible)
        currency_value = browser.element(
            by.xpath(f"//*[@class='center'][contains(text(), 'Account Number')]//strong[contains(text(), "
                     f"'{currency}')]")).with_(Config(timeout=5))
        currency_value.should_be(visible)
        Button().click_on_the_button(type_of_transaction)
        Input().enter_text(amount_field, amount)
        Button().click_on_the_submit_button(submit)
        message = browser.element(by.xpath(f"//span[contains(text(), '{expected_message}')]")).with_(Config(timeout=5))
        message.should_be(visible)
        time.sleep(1)

    def balance_should_be_correct(self, user_balance):
        balance = browser.element(
            by.xpath(f"//*[@class='center']//strong[2][contains(text(),'')]")).with_(Config(timeout=5))
        assert int(balance.text) == user_balance

    def click_on_the_button(self, button_name):
        Button().click_on_the_button(button_name)
