import pytest
from playwright.sync_api import sync_playwright
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False, slow_mo=100)
        yield browser
        browser.close()

@pytest.fixture()
def page(browser):
    page = browser.new_page()
    yield page
    page.close()