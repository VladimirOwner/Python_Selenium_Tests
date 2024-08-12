import time
import pytest
from pages.login_page import LoginPage
from pages.Objects.settings_authorization_page import AuthorizationPage
import allure

def test_create_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('ntlm')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    assert authorization_page.get_type_object() == 'NTLM'

def test_update_name_object_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_pencil_button()
    authorization_page.input_pencil_field().send_keys('Параметр авторизации NTLM')
    authorization_page.click_on_save_button()
    authorization_page.get_name_in_main_frame()
    assert authorization_page.get_name_in_main_frame() == 'Параметр авторизации NTLM'

def test_add_description_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.description_field().send_keys('Авторизация основная')
    authorization_page.click_on_save_button()
    authorization_page.get_description_in_main_frame()
    assert authorization_page.get_description_in_main_frame() == 'Авторизация основная'

def test_check_button_check_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_check_button()
    assert authorization_page.get_fail_text_information() == 'Не удалось подключиться'

def test_check_checkbox_use_cash_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_checkbox_cash_on_ip()
    authorization_page.click_on_save_button()
    assert authorization_page.get_default_min() == 5

def test_check_type_of_portal_button_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_type_of_portal_button()
    assert authorization_page.get_text_header_madal() == 'Вид портала'

def test_check_checkbox_reject_authorization_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_checkbox_reject_repeate_authorization()
    authorization_page.click_on_save_button()
    authorization_page.click_on_statistic_button()
    authorization_page.click_on_history_button()
    assert authorization_page.get_reject_authorization_on_statistic() == 'Да'

def test_create_object_without_obligatory_field(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.input_url_ldap().send_keys('')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('ivan')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    assert authorization_page.get_error_text_modal() == 'URL LDAP - обязательно для заполнения'

def test_cancel_changing(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    description = authorization_page.get_description_in_main_frame()
    authorization_page.description_field().clear()
    authorization_page.click_on_cancel_button()
    authorization_page.click_on_confirm_cancel_button()
    assert authorization_page.get_description_in_main_frame() == description

def test_history_changing_information(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    name = authorization_page.get_name_in_main_frame()
    login = authorization_page.input_login().get_attribute('value')
    ou = authorization_page.input_base_ou().get_attribute('value')
    ldap = authorization_page.input_url_ldap().get_attribute('value')
    description = authorization_page.get_description_in_main_frame()
    type = authorization_page.get_type_object()
    authorization_page.click_on_statistic_button()
    authorization_page.click_on_history_button()
    assert authorization_page.get_history_type() == type and authorization_page.get_history_ldap() == ldap and authorization_page.get_history_login() == login \
    and authorization_page.get_history_ou() == ou and authorization_page.get_history_autharization() == name and authorization_page.get_history_description() == description

def test_delete_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


def test_create_basic(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_basic()
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('basic')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    assert authorization_page.get_type_object() == 'Basic'

@pytest.mark.parametrize('creds',[' ','-1','4','1440'])
def test_input_time_session(creds,driver):
    time = creds
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    if time == ' ':
        authorization_page.input_time_session().clear()
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - обязательно для заполнения'
    elif time == '-1':
        authorization_page.input_time_session().clear()
        authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - Число должно быть целым и больше или равно 5'
    elif time == '4':
        authorization_page.input_time_session().clear()
        authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - Число должно быть целым и больше или равно 5'

    elif time == '1440':
        authorization_page.input_time_session().clear()
        authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        authorization_page.click_on_statistic_button()
        authorization_page.click_on_history_button()
        assert authorization_page.get_history_time_session() == time

@pytest.mark.parametrize('creds',[' ','-1','0','4'])
def test_input_count_entrance(creds,driver):
    count = creds
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    if count == ' ':
        authorization_page.input_count_entrance().clear()
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - обязательно для заполнения'
    elif count == '-1':
        authorization_page.input_count_entrance().clear()
        authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - Число должно быть целым и больше нуля'
    elif count == '0':
        authorization_page.input_count_entrance().clear()
        authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - Число должно быть целым и больше нуля'
    elif count == '4':
        authorization_page.input_count_entrance().clear()
        authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        authorization_page.click_on_statistic_button()
        authorization_page.click_on_history_button()
        assert authorization_page.get_history_count_entrance() == count

def test_change_source(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_list_source()
    authorization_page.click_adress_book_button()
    authorization_page.click_on_save_button()
    assert authorization_page.get_field_users() == 'Все'

def test_delete_basic_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

def test_create_tacacs_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_tacacs()
    authorization_page.input_ip_adress().send_keys('192.168.3.85')
    authorization_page.input_secret().send_keys('5')
    authorization_page.click_on_save_button()
    assert authorization_page.get_type_object() == 'TACACS'

@pytest.mark.parametrize('creds',[(' ',' '),('192.168.1.2',''),('','5')])
def test_check_obligatory_fill_fields(creds,driver):
    ip_adress, secret = creds
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    if ip_adress == ' ' and secret == ' ':
        authorization_page.input_ip_adress().clear()
        authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        assert authorization_page.get_list_obligatory_fill()[0].text == 'IP-адрес - обязательно для заполнения' \
               and authorization_page.get_list_obligatory_fill()[1].text == 'Секрет - обязательно для заполнения'
    elif ip_adress == '192.168.1.2':
        authorization_page.input_ip_adress().clear()
        authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'Секрет - обязательно для заполнения'
    elif secret == '5':
        authorization_page.input_ip_adress().clear()
        authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        assert authorization_page.get_text_obligatory_fill() == 'IP-адрес - обязательно для заполнения'

def test_delete_tacacs_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

def test_create_dc_log(driver):
    path_cert = 'C:/Users/salynin/Downloads/CertsNew.cer'
    path_key = 'C:/Users/salynin/Downloads/CertsNew.key'
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    authorization_page.input_port().send_keys('5000')
    authorization_page.input_fqdn().send_keys('123')
    authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    authorization_page.input_download_key().send_keys(f"{path_key}")
    authorization_page.input_certificate().send_keys('Подпись сертификата')
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('dc log')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    assert authorization_page.get_type_object() == 'DC Log'

def test_create_object_invalid_sert(driver):
    path_cert = 'C:/Users/salynin/Downloads/SSL.cer'
    path_key = 'C:/Users/salynin/Downloads/CertsNew.key'
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    authorization_page.input_port().send_keys('5000')
    authorization_page.input_fqdn().send_keys('123')
    authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    authorization_page.input_download_key().send_keys(f"{path_key}")
    authorization_page.input_certificate().send_keys('Подпись сертификата')
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('dc log')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    assert authorization_page.get_text_fail_modal() == 'Сертификат или ключ не валидный'

def test_obligatory_to_fill_port(driver):
    path_cert = 'C:/Users/salynin/Downloads/CertsNew.cer'
    path_key = 'C:/Users/salynin/Downloads/CertsNew.key'
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    authorization_page.input_port().send_keys('')
    authorization_page.input_fqdn().send_keys('123')
    authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    authorization_page.input_download_key().send_keys(f"{path_key}")
    authorization_page.input_certificate().send_keys('Подпись сертификата')
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('dc log')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    assert authorization_page.get_text_obligatory_fill() == 'Порт - обязательно для заполнения'

def test_statistic_data_dc_log(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    port = authorization_page.input_port().get_attribute('value')
    sert_name = authorization_page.get_name_sertificate()
    sert_key = authorization_page.get_name_key()
    fill_certificate = authorization_page.input_certificate().get_attribute('value')
    authorization_page.click_on_statistic_button()
    authorization_page.click_on_history_button()
    assert authorization_page.get_history_port() == port and authorization_page.get_history_name_certificate() == sert_name \
           and authorization_page.get_history_fill_sertification() == fill_certificate and authorization_page.get_history_name_key() == sert_key

def test_delete_dclog_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


def test_create_portal(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_portal()
    authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    authorization_page.input_base_ou().send_keys('ea')
    authorization_page.input_login().send_keys('ntlm')
    authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    assert authorization_page.get_type_object() == 'Портал'

def test_delete_portal(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

def test_create_radius_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_radius()
    authorization_page.input_ip_adress().send_keys('192.168.3.85')
    authorization_page.input_secret().send_keys('5')
    authorization_page.click_on_save_button()
    assert authorization_page.get_type_object() == 'RADIUS'

def test_delete_radius(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_delete_button()
    authorization_page.click_on_confirm_delete_button()
    authorization_page.get_text_information()
    assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


