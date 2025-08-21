import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


@pytest.fixture(scope="class")
def browser():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def page(request, browser):
    page = MainPage(browser)
    page.open()
    return page
