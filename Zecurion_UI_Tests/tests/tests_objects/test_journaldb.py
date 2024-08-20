import pytest
from pages.login_page import LoginPage
from pages.Objects.journal_db import JournalDB
import allure


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_journal_db(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.click_on_add_button()
    journal.input_enter_db().send_keys('ngfw_log')
    journal.click_on_save_button()
    assert journal.get_name_object() == 'Новое журналирование в базы данных'


def test_update_name(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.click_on_pencil_button()
    journal.input_pencil_field().send_keys('БД')
    journal.click_on_save_button()
    assert journal.get_name_object() == 'БД'


def test_add_description(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.input_description().send_keys('База данных NGFW')
    journal.click_on_save_button()
    assert journal.get_description_on_main_frame() == 'База данных NGFW'


def test_check_connection_button(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.click_on_check_connection_button()
    assert journal.get_connection_text() == 'Соединение успешно'


def test_change_activity(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.click_on_active_drop_down()
    journal.choose_list_activity().click()
    journal.click_on_save_button()
    journal.click_on_statistic_button()
    journal.click_on_history_button()
    assert journal.get_history_activity() == 'Выключено'


def test_obligatory_to_fill_db(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.click_on_add_button()
    journal.click_on_save_button()
    assert journal.get_error_text_modal() == 'База данных - обязательно для заполнения'


def test_create_postgres_without_obligatory_input(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.click_on_type_server()
    journal.click_on_postgres_db()
    journal.input_enter_db().clear()
    journal.click_on_save_button()
    assert journal.get_error_text_user() == 'Пользователь - обязательно для заполнения' and journal.get_error_text_server() == 'Сервер - обязательно для заполнения' and \
        journal.get_error_text_password() == 'Пароль - обязательно для заполнения' and journal.get_error_text_bd() == 'База данных - обязательно для заполнения'



def test_create_postgre(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    journal.click_on_type_server()
    journal.click_on_postgres_db()
    journal.input_server().send_keys('192.168.1.165:5432')
    journal.input_user().send_keys('postgres')
    journal.input_password().send_keys('flvw003003')
    journal.click_on_save_button()
    journal.click_on_statistic_button()
    journal.click_on_history_button()
    assert journal.get_history_type_server() == 'PostgreSQL'


def test_cancel_changing(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    value = journal.input_description().get_attribute('value')
    journal.input_description().clear()
    journal.click_on_cancel_button()
    journal.click_on_confirm_cancel_button()
    assert value == 'База данных NGFW'


def test_history_changing_information(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    journal.choose_object_in_main_frame().click()
    db = journal.input_enter_db().get_attribute('value')
    name = journal.get_name_object()
    description = journal.input_description().get_attribute('value')
    user = journal.input_user().get_attribute('value')
    server = journal.input_server().get_attribute('value')
    journal.click_on_statistic_button()
    journal.click_on_history_button()
    assert journal.get_history_db() == db and journal.get_history_name() == name and \
        journal.get_history_description() == description and journal.get_history_user() == user and journal.get_history_server() == server


def test_delete_db(driver):
    login(driver)
    journal = JournalDB(driver)
    journal.click_on_object_button()
    journal.click_on_journaldb_button()
    count = journal.get_count_object()
    journal.choose_object_in_main_frame().click()
    journal.click_on_delete_button()
    journal.click_on_confirm_delete_button()
    if count > 1:
        assert journal.get_count_object() == count-1
    elif count == 1:
        assert journal.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

