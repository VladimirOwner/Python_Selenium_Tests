import time
from test_tegs import test_create_teg as create_teg, test_delete_teg as del_teg
from pages.login_page import LoginPage
from pages.Objects.adblock import Adblock
import allure

def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_adblock(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.click_on_add_button()
    adblok.input_sites_block().send_keys('https://raw.githubusercontent.com/Zalexanninev15/NoADS_RU/main/ads_list_extended.txt')
    adblok.click_on_save_button()
    adblok.get_sucsses_icon()
    assert adblok.get_name_object() == 'Новое правило AdBlock'

def test_update_name(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.click_on_pencil_button()
    adblok.input_pencil_field().send_keys('AdBlock')
    adblok.click_on_save_button()
    assert adblok.get_name_object() == 'AdBlock'

def test_add_description(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.input_description().send_keys('Защита от рекламы')
    adblok.click_on_save_button()
    assert adblok.get_description_on_main_frame() == 'Защита от рекламы'

def test_cancel_changing(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    description = adblok.get_description_on_main_frame()
    adblok.input_description().clear()
    adblok.click_on_cancel_button()
    adblok.click_on_confirm_cancel_button()
    assert adblok.get_description_on_main_frame() == description

def test_change_activity(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.click_on_active_drop_down()
    adblok.choose_list_activity().click()
    adblok.click_on_save_button()
    adblok.click_on_statistic_button()
    adblok.click_on_history_button()
    assert adblok.get_history_activity() == 'Выключено'


def test_checkbox_block_traffic(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.click_checkbox_block_traffic()
    adblok.click_on_save_button()
    adblok.click_on_statistic_button()
    adblok.click_on_history_button()
    assert adblok.get_history_block_traffic() == 'Нет'

def test_add_invalid_site_rule(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    count = adblok.count_input_sites()
    adblok.click_on_plus_sites()
    adblok.input_sites_block().send_keys('1')
    adblok.click_on_save_button()
    adblok.get_error_icon()
    assert adblok.count_input_sites() == count+1

def test_delete_input_site(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    count = adblok.count_input_sites()
    adblok.click_on_delete_input_site()
    adblok.click_on_save_button()
    assert adblok.count_input_sites() == count-1

def test_add_teg(driver):
    create_teg(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.click_on_tegs_plus_button()
    adblok.choose_teg_in_modal()
    adblok.click_on_apply_button()
    adblok.click_on_save_button()
    name_tag = adblok.get_tag_on_main_frame()
    adblok.click_on_statistic_button()
    adblok.click_on_history_button()
    assert adblok.get_history_teg() == name_tag

def test_obligatory_to_fill(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.click_on_add_button()
    adblok.click_on_save_button()
    assert adblok.get_error_text_modal() == 'Справочники сайтов AdBlock - обязательно для заполнения'

def test_check_statistic_button(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    name = adblok.get_name_object()
    description = adblok.get_description_on_main_frame()
    activity = adblok.get_value_activity()
    tag = adblok.get_tag_on_main_frame()
    adblok.click_on_statistic_button()
    adblok.click_on_history_button()
    assert adblok.get_history_block_traffic() == 'Нет' and adblok.get_history_name() == name and adblok.get_history_description() == description and \
        adblok.get_history_teg() == tag and adblok.get_history_activity() == activity


def test_delete_tag(driver):
    login(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    adblok.click_on_delete_tag()
    adblok.click_on_save_button()
    assert adblok.get_text_none_tag() == 'Не установлено'


def test_delete_adblock(driver):
    del_teg(driver)
    adblok = Adblock(driver)
    adblok.click_on_object_button()
    adblok.click_on_adblock_button()
    adblok.choose_object_in_main_frame().click()
    count = adblok.get_count_object()
    adblok.click_on_delete_button()
    adblok.click_on_confirm_delete_button()
    if count > 1:
        assert adblok.get_count_object() == count-1
    elif count == 1:
        assert adblok.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'









