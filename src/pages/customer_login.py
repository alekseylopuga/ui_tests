from src.components.button import Button
from src.components.select import Select
from src.components.text import Text


class CustomerLogin:

    def __init__(self):
        self.home_button = Button().button_should_be_visible('home')
        self.bank_name = Text().header_should_be_visible()

    def select_name_and_login(self, name, button):
        Button().submit_button_should_not_be_visible(button)
        Select().open_dropdown('userSelect')
        Select().select_option(name)
        Button().click_on_the_submit_button(button)
