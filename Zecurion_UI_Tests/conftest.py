from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import pytest

@pytest.fixture()
def driver():
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Chrome(options=options)
    return browser