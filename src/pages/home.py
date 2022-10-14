from src.components.button import Button
from src.components.text import Text


class Home:

    def __init__(self):
        self.home_button = Button().button_should_be_visible('home')
        self.customer_login = Button().button_should_be_visible('customer')
        self.manager_login = Button().button_should_be_visible('manager')
        self.bank_name = Text().header_should_be_visible()

    def open_page(self, name):
        Button().click_on_the_button(name)
