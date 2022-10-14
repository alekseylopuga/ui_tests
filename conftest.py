import os

import pytest

from selene.support.shared import browser


@pytest.fixture(autouse=False)
def open_browser():
    url = os.environ.get('BASE_URL', 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login')
    browser.open(url)
    browser.driver.fullscreen_window()


@pytest.fixture(scope='function', autouse=False)
def close_browser():
    yield
    browser.quit()
