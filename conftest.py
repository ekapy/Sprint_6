import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    ff_driver = webdriver.Firefox()
    ff_driver.maximize_window()

    yield ff_driver

    ff_driver.quit()
