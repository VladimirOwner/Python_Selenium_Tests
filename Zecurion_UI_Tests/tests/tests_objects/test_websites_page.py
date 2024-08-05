from pages.login_page import LoginPage
from pages.Objects.websites_page import WebsitesPage


def test_create_webcategories(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_on_add_button()
    websites_page.click_on_save_button()

