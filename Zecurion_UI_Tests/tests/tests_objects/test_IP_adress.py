import time

from pages.login_page import LoginPage
from pages.Objects.ip_adress import IP_adress

def test_create_ip_object(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.click_on_add_new_object()
    ip_adress.input_ip().send_keys('1.1.1.1')
    ip_adress.click_on_save_IP()
    ip_adress.input_fast_search().send_keys('Новый IP-адрес')
    ip_adress.get_author()
    assert ip_adress.get_name_of_ip_object() == 'Новый IP-адрес'

def test_change_name_ip_object(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('Новый IP-адрес')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.click_on_pencil_edit_icon()
    ip_adress.input_edit_name().send_keys('selenium_test_edit_IP_name')
    ip_adress.click_on_save_IP()
    ip_adress.click_on_clear_search()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    ip_adress.get_author()
    assert ip_adress.get_name_of_ip_object() == 'selenium_test_edit_IP_name'

def test_change_description(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.input_description_field().send_keys('selenium_test_edit_description')
    ip_adress.click_on_save_IP()
    ip_adress.click_on_statistics()
    ip_adress.click_last_change()
    assert ip_adress.get_description() == 'selenium_test_edit_description'

def test_change_ip_adress(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.clear_ip_field()
    ip_adress.input_ip_field().send_keys('192.168.0.160')
    ip_adress.click_on_save_IP()
    ip_adress.click_on_statistics()
    ip_adress.click_last_change()
    assert ip_adress.get_ip() == '192.168.0.160'

def test_empty_ip_adress(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.clear_ip_field()
    ip_adress.click_on_save_IP()
    assert ip_adress.get_error_empty_ip() == 'IP-адрес - обязательно для заполнения'

def test_incorrect_ip_adress(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.input_ip_field().clear()
    ip_adress.input_ip_field().send_keys('192.168.0.160.')
    ip_adress.click_on_save_IP()
    assert ip_adress.get_error_empty_ip() == 'IP-адрес - Некорректное значение'

def test_add_multiple_ip_adress(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.add_new_ip_field()
    ip_adress.input_second_ip().send_keys('192.168.0.161')
    ip_adress.click_on_save_IP()
    ip_adress.click_on_statistics()
    ip_adress.click_last_change()
    assert ip_adress.get_ip() == '192.168.0.160, 192.168.0.161'

def test_delete_ip_adress(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.click_on_ip_clear_button()
    ip_adress.click_on_save_IP()
    ip_adress.click_on_statistics()
    ip_adress.click_last_change()
    assert ip_adress.get_ip() == '192.168.0.161'

def test_delete_ip_object(driver):
    login_page = LoginPage(driver)
    ip_adress = IP_adress(driver)
    login_page.login()
    ip_adress.click_on_object_button()
    ip_adress.click_on_ip_adress_button()
    ip_adress.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_adress.get_author()
    time.sleep(1)
    ip_adress.click_name_of_ip_object()
    ip_adress.delete_object()
    ip_adress.accept_delete_object()
    assert ip_adress.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
