import time
from faker import Faker
from test_tegs import test_create_teg as create_teg, test_delete_teg as del_teg
from pages.login_page import LoginPage
from pages.Objects.mime_type import MimeType
import allure
faker = Faker()

def login(driver):
    login_page = LoginPage(driver)
    login_page.login()

def test_create_mime_type(driver):
    mime_type = faker.word()
    name_mime = faker.word()
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_on_add_button()
    mime.input_mime_type().send_keys(mime_type)
    mime.click_on_pencil_button()
    mime.input_pencil_field().send_keys(name_mime)
    mime.click_on_save_button()
    mime.click_on_statistic_button()
    mime.click_on_history_button()
    assert mime.get_history_mime_type() == mime_type and mime.get_history_name() == name_mime

def test_create_without_obligatory_fill(driver):
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_on_add_button()
    mime.click_on_save_button()
    assert mime.get_error_text_modal() == 'Mime-тип - обязательно для заполнения'


def test_add_description(driver):
    description = faker.word()
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    mime.input_description().send_keys(description)
    mime.click_on_save_button()
    assert mime.get_description_on_main_frame() == description

def test_cancel_changing(driver):
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    description = mime.get_description_on_main_frame()
    mime.input_description().clear()
    mime.click_on_cancel_button()
    mime.click_on_confirm_cancel_button()
    assert mime.get_description_on_main_frame() == description


def test_add_tag(driver):
    create_teg(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    mime.click_on_tegs_plus_button()
    mime.choose_teg_in_modal()
    name_tag = mime.get_name_tag_in_modal()
    mime.click_on_apply_button()
    mime.click_on_save_button()
    assert mime.get_tag_on_main_frame() == name_tag

def test_statistic_information(driver):
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    name = mime.get_name_object()
    description = mime.get_description_on_main_frame()
    tag = mime.get_tag_on_main_frame()
    mime_type = mime.input_mime_type().get_attribute('value')
    mime.click_on_statistic_button()
    mime.click_on_history_button()
    assert mime.get_history_mime_type() == mime_type and mime.get_history_name() == name and \
        mime.get_history_description() == description and mime.get_history_tag() == tag

def test_delete_tag(driver):
    login(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    mime.click_on_delete_tag()
    mime.click_on_save_button()
    assert mime.get_text_none_tag() == 'Не установлено'

def test_delete_mime(driver):
    del_teg(driver)
    mime = MimeType(driver)
    mime.click_on_object_button()
    mime.click_on_mime_button()
    mime.click_filter_header()
    mime.click_checkbox_authtor()
    mime.click_on_check_filter()
    mime.choose_object_in_main_frame().click()
    count = mime.get_count_object()
    mime.click_on_delete_button()
    mime.click_on_confirm_delete_button()
    if count > 1:
        assert mime.get_count_object() == count-1
    elif count == 1:
        assert mime.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'








