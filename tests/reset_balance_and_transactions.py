from src.pages.home import Home
from src.pages.customer_login import CustomerLogin
from src.pages.main import Main
from src.pages.transactions import Transactions


def test_reset_balance_and_transactions(open_browser):
    Home().open_page('customer')
    CustomerLogin().select_name_and_login('Ron Weasly', 'Login')
    main = Main('Ron Weasly')
    main.balance_should_be_correct(0)
    main.make_transaction('1007', 'Dollar', 'deposit', 'Deposit', 10, 'Deposit', 'Deposit Successful')
    main.click_on_the_button('transactions')
    transactions = Transactions()
    transactions.transaction_should_be_visible(0, 10, 'Credit')
    transactions.click_on_the_button('back')
    main.balance_should_be_correct(10)
    main.click_on_the_button('transactions')
    transactions.click_on_the_button('reset')
    transactions.table_should_be_empty_before_re_opening()
    transactions.click_on_the_button('back')
    main.balance_should_be_correct(0)
    main.click_on_the_button('transactions')
    transactions.table_should_be_empty_after_re_opening()
