from src.pages.home import Home
from src.pages.customer_login import CustomerLogin
from src.pages.main import Main
from src.pages.transactions import Transactions


# @pytest.mark.parametrize('search_field, text_1, text_2, colour_1, colour_2', [
#     ('autoCompleteMultipleInput', 'bl', 'g', 'Black', 'Green'),
#     ('autoCompleteSingleInput', 're', 'white', 'Red', 'White'),
# ])
def test_make_valid_deposit_and_valid_withdrawal(open_browser):
    Home().open_page('customer')
    CustomerLogin().select_name_and_login('Ron Weasly', 'Login')
    main = Main('Ron Weasly')
    main.balance_should_be_correct(0)
    main.make_transaction('1007', 'Dollar', 'deposit', 'Deposit', 10, 'Deposit', 'Deposit Successful')
    main.click_on_the_button('transactions')
    Transactions().transaction_should_be_visible(0, 10, 'Credit')
    Transactions().click_on_the_button('back')
    main.balance_should_be_correct(10)
    main.make_transaction('1007', 'Dollar', 'withdrawl', 'Withdrawn', 5, 'Withdraw', 'Transaction successful')
    main.click_on_the_button('transactions')
    Transactions().transaction_should_be_visible(1, 5, 'Debit')
    Transactions().click_on_the_button('back')
    main.balance_should_be_correct(5)
    main.click_on_the_button('transactions')
    Transactions().click_on_the_button('reset')
    Transactions().table_should_be_empty_before_re_opening()
    Transactions().click_on_the_button('back')
    main.click_on_the_button('transactions')
    Transactions().table_should_be_empty_after_re_opening()
