import time
import pytest
from pages.login_page import LoginPage
from pages.Objects.content_protection import ContentProtection
from test_tegs import test_create_teg as create_teg, test_delete_teg as del_teg
import allure


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_protection(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.click_on_add_button()
    protection.click_on_save_button()
    assert protection.get_name_object() == 'Новое правило защиты контента'


def test_update_name(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_pencil_button()
    protection.input_pencil_field().send_keys('Защита данных')
    protection.click_on_save_button()
    assert protection.get_name_object() == 'Защита данных'


def test_add_description(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.input_description().send_keys('Защита паспортных данных')
    protection.click_on_save_button()
    assert protection.get_description_on_main_frame() == 'Защита паспортных данных'

def test_add_tag(driver):
    create_teg(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_tegs_plus_button()
    protection.choose_teg_in_modal()
    name_tag = protection.get_name_tag_in_modal()
    protection.click_on_apply_button()
    protection.click_on_save_button()
    assert protection.get_tag_on_main_frame() == name_tag




def test_cancel_changing(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    name = protection.get_name_object()
    protection.click_on_pencil_button()
    protection.input_pencil_field().send_keys('Измененная защита данных')
    protection.click_on_cancel_button()
    protection.click_on_confirm_cancel_button()
    assert protection.get_name_object() == name


def test_change_activity(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_active_drop_down()
    protection.choose_list_activity().click()
    protection.click_on_save_button()
    protection.click_on_statistic_button()
    protection.click_on_history_button()
    assert protection.get_history_activity() == 'Выключено'


def test_checkbox_block_traffic(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_checkbox_block_traffic()
    protection.click_on_save_button()
    protection.click_on_statistic_button()
    protection.click_on_history_button()
    assert protection.get_history_block_traffic() == 'Нет'


def test_add_mask(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_mask_plus()
    protection.input_mask().send_keys('\\d{4}\\s\\d{6}')
    protection.click_on_save_button()
    assert protection.input_mask().get_attribute('value') == '\\d{4}\\s\\d{6}'


def test_download_mask_file(driver):
    with open('creds.txt', 'r') as f:
        for line in f:
            if line.__contains__('MASK'):
                mask_path = line.split('=')
                mask_path = mask_path[-1].strip()
    file = mask_path
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_mask_plus()
    protection.input_download_mask().send_keys(file)
    protection.click_on_save_button()
    name_file = file.split('/')
    name_file = name_file[-1]
    assert protection.get_file_name() == name_file


def test_without_fill_mask(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_mask_plus()
    protection.click_on_save_button()
    assert protection.get_error_text_modal() == 'Маски - обязательно для заполнения'


def test_delete_input_mask(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    count = protection.get_count_mask()
    protection.click_on_close_mask_button()
    protection.click_on_save_button()
    assert protection.get_count_mask() == count-1

def test_delete_tag(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_on_delete_tag()
    protection.click_on_save_button()
    assert protection.get_text_none_tag() == 'Не установлено'


def test_choose_all_checkbox(driver):
    login(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    protection.click_checkbox_phi()
    protection.click_checkbox_personal_data()
    protection.click_checkbox_gdbpr()
    protection.click_checkbox_pii()
    protection.click_checkbox_glba()
    protection.click_checkbox_hipaa()
    protection.click_checkbox_gdpr_restricted()
    protection.click_checkbox_financial_records()
    protection.click_checkbox_psi_dss()
    protection.click_on_save_button()
    protection.click_on_statistic_button()
    protection.click_on_history_button()
    assert protection.get_history_gdpr_restricted() == 'Да' and protection.get_history_gdbpr() == 'Да' and protection.get_history_hipaa() == 'Да' and \
        protection.get_history_personal_data() == 'Да' and protection.get_history_financial_records() == 'Да' and protection.get_history_phi() == 'Да' and \
        protection.get_history_glba() == 'Да' and protection.get_history_pci_dss() == 'Да'


def test_delete_content_protection(driver):
    del_teg(driver)
    protection = ContentProtection(driver)
    protection.click_on_object_button()
    protection.click_on_protection_button()
    protection.choose_object_in_main_frame().click()
    count = protection.get_count_object()
    protection.click_on_delete_button()
    protection.click_on_confirm_delete_button()
    if count > 1:
        assert protection.get_count_object() == count-1
    elif count == 1:
        assert protection.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'