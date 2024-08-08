import time

from pages.login_page import LoginPage
from pages.Objects.protocols import Protocols

def test_create_protocol(driver):
    login_page = LoginPage(driver)
    protocols = Protocols(driver)
    login_page.login()
    protocols.click_on_object_button()
    protocols.click_on_protocol_button()
    protocols.click_on_add_new_protocol()
    protocols.click_on_save_protocol()
    protocols.input_fast_search().send_keys('Новый протокол')
    protocols.get_author()
    assert protocols.get_name_protocol() == 'Новый протокол'

def test_change_name_protocol(driver):
    login_page = LoginPage(driver)
    protocols = Protocols(driver)
    login_page.login()
    protocols.click_on_object_button()
    protocols.click_on_protocol_button()
    protocols.input_fast_search().send_keys('Новый протокол')
    protocols.get_author()
    protocols.click_name_protocol()
    protocols.click_on_pencil_edit_icon()
    protocols.input_edit_name().send_keys('selenium_test_edit_protocol_name')
    protocols.click_on_save_protocol()
    protocols.click_on_clear_search()
    protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    assert protocols.get_name_protocol() == 'selenium_test_edit_protocol_name'

def test_description_field(driver):
    login_page = LoginPage(driver)
    protocols = Protocols(driver)
    login_page.login()
    protocols.click_on_object_button()
    protocols.click_on_protocol_button()
    protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.click_name_protocol()
    protocols.input_description_field().send_keys('selenium_test')
    protocols.click_on_save_protocol()
    protocols.click_on_statistics()
    protocols.click_last_change()
    assert protocols.get_description() == 'selenium_test'

def test_add_dpi_protocol(driver):
    login_page = LoginPage(driver)
    protocols = Protocols(driver)
    login_page.login()
    protocols.click_on_object_button()
    protocols.click_on_protocol_button()
    protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.click_name_protocol()
    protocols.click_dpi_protocol()
    protocols.click_on_checkbox_media()
    protocols.save_dpi_modal()
    assert protocols.get_dpi_protocol() == 'Media'

def test_delete_protocol(driver):
    login_page = LoginPage(driver)
    protocols = Protocols(driver)
    login_page.login()
    protocols.click_on_object_button()
    protocols.click_on_protocol_button()
    protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.click_name_protocol()
    protocols.click_delete_protocol()
    protocols.click_accept_delete_protocol()
    assert protocols.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'