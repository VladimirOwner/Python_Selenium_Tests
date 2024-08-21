import time
import pytest
from pages.login_page import LoginPage
from pages.Objects.settings_authorization_page import AuthorizationPage
import allure
@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Создание объекта "NTLM"')
def test_create_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    with allure.step('В поле "LDAP" ввести значение "ea@testdoman.com"'):
        authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "ntlm"'):
        authorization_page.input_login().send_keys('ntlm')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'NTLM'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Изменение названия объекта')
def test_update_name_object_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_pencil_button()
    with allure.step('Изменить название объекта, например "Параметр авторизации NTLM"'):
        authorization_page.input_pencil_field().send_keys('Параметр авторизации NTLM')
    authorization_page.click_on_save_button()
    authorization_page.get_name_in_main_frame()
    with allure.step('Проверка изменения названия объекта'):
        assert authorization_page.get_name_in_main_frame() == 'Параметр авторизации NTLM'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Добавление описания')
def test_add_description_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    with allure.step('В поле описание ввести "Авторизация основная"'):
        authorization_page.description_field().send_keys('Авторизация основная')
    authorization_page.click_on_save_button()
    authorization_page.get_description_in_main_frame()
    with allure.step('Проверка добавления описания'):
        assert authorization_page.get_description_in_main_frame() == 'Авторизация основная'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Проверка кнопки "Проверить"')
def test_check_button_check_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_check_button()
    with allure.step('Проверяем появления сообщения с результатом проверки'):
        assert authorization_page.get_fail_text_information() == 'Не удалось подключиться'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Проверка выбора чек бокса "Использовать кеш по IP"')
def test_check_checkbox_use_cash_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_checkbox_cash_on_ip()
    authorization_page.click_on_save_button()
    with allure.step('Проверяем появления поля "Срок сессии,мин" с дефолтным значением'):
        assert authorization_page.get_default_min() == 5

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Проверка кнопки "Выберите вид портала"')
def test_check_type_of_portal_button_ntlm(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    authorization_page.click_on_type_of_portal_button()
    with allure.step('Проверка появления модального окна с возможностью выбора объекта вида портала'):
        assert authorization_page.get_text_header_madal() == 'Вид портала'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Проверка выбора чек бокса "Запрет повторной авторизации"')
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
    with allure.step('Проверка выбора чек бокса "Запрет повторной авторизации"'):
        assert authorization_page.get_reject_authorization_on_statistic() == 'Да'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Создание объекта "NTLM" без заполнения одного обязательного поля')
def test_create_object_without_obligatory_field(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    with allure.step('Поле "LDAP" осталяем пустым'):
        authorization_page.input_url_ldap().send_keys('')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "ntlm"'):
        authorization_page.input_login().send_keys('ntlm')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "LDAP"'):
        assert authorization_page.get_error_text_modal() == 'URL LDAP - обязательно для заполнения'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Отмена изменений')
def test_cancel_changing(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.choose_object_in_main_frame().click()
    description = authorization_page.get_description_in_main_frame()
    with allure.step('В поле "Описание" удаляем описание'):
        authorization_page.description_field().clear()
    authorization_page.click_on_cancel_button()
    authorization_page.click_on_confirm_cancel_button()
    with allure.step('Проверяем, что изменения сделанные в данном объекте не применились'):
        assert authorization_page.get_description_in_main_frame() == description
@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Проверка записи в "Истории изменений"')
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
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert authorization_page.get_history_type() == type and authorization_page.get_history_ldap() == ldap and authorization_page.get_history_login() == login \
    and authorization_page.get_history_ou() == ou and authorization_page.get_history_autharization() == name and authorization_page.get_history_description() == description

@allure.feature("Объекты")
@allure.story("Параметры авторизации - NTLM")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта "NTLM"'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


@allure.feature("Объекты")
@allure.story("Параметры авторизации - Basic")
@allure.title('Создание объекта "Basic"')
def test_create_basic(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_basic()
    with allure.step('В поле "LDAP" ввести значение "ea@testdoman.com"'):
        authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "Basic"'):
        authorization_page.input_login().send_keys('Basic')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'Basic'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - Basic")
@allure.title('Проверка поля "Срок сессии,мин"')
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
        with allure.step('Оставляем поле "Срок сессии,мин" пустым'):
            authorization_page.input_time_session().clear()
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "Срок сессии,мин"'):
            assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - обязательно для заполнения'
    elif time == '-1':
        authorization_page.input_time_session().clear()
        with allure.step('В поле "Срок сессии,мин" ввести значение "-1"'):
            authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой введенного значения'):
            assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - Число должно быть целым и больше или равно 5'
    elif time == '4':
        authorization_page.input_time_session().clear()
        with allure.step('В поле "Срок сессии,мин" ввести значение "4"'):
            authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой введенного значения'):
            assert authorization_page.get_text_obligatory_fill() == 'Срок сессии, мин - Число должно быть целым и больше или равно 5'

    elif time == '1440':
        authorization_page.input_time_session().clear()
        with allure.step('В поле "Срок сессии,мин" ввести значение "1440"'):
            authorization_page.input_time_session().send_keys(time)
        authorization_page.click_on_save_button()
        authorization_page.click_on_statistic_button()
        authorization_page.click_on_history_button()
        with allure.step('Проверка успешного добавления значения в поле "Срок сессии, мин"'):
            assert authorization_page.get_history_time_session() == time

@allure.feature("Объекты")
@allure.story("Параметры авторизации - Basic")
@allure.title('Проверка поля "Количество ошибок входа"')
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
        with allure.step('Поле "Количество ошибок входа" оставить пустым'):
            authorization_page.input_count_entrance().clear()
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "Количество ошибок входа"'):
            assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - обязательно для заполнения'
    elif count == '-1':
        authorization_page.input_count_entrance().clear()
        with allure.step('В поле "Количество ошибок входа" ввести значение "-1"'):
            authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой введенного значения'):
            assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - Число должно быть целым и больше нуля'
    elif count == '0':
        authorization_page.input_count_entrance().clear()
        with allure.step('В поле "Количество ошибок входа" ввести значение "0"'):
            authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой введенного значения'):
            assert authorization_page.get_text_obligatory_fill() == 'Количество ошибок входа - Число должно быть целым и больше нуля'
    elif count == '4':
        authorization_page.input_count_entrance().clear()
        with allure.step('В поле "Количество ошибок входа" ввести значение "4"'):
            authorization_page.input_count_entrance().send_keys(count)
        authorization_page.click_on_save_button()
        authorization_page.click_on_statistic_button()
        authorization_page.click_on_history_button()
        with allure.step('Проверка успешного добавления значения в поле "Количество ошибок входа"'):
            assert authorization_page.get_history_count_entrance() == count
@allure.feature("Объекты")
@allure.story("Параметры авторизации - Basic")
@allure.title('Изменение "Источника"')
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
    with allure.step('Проверка изменения "Источника"'):
        assert authorization_page.get_field_users() == 'Все'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - Basic")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - TACACS")
@allure.title('Cоздание объекта "TACACS"')
def test_create_tacacs_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_tacacs()
    with allure.step('В поле "IP - адрес" ввести значение "192.168.3.85"'):
        authorization_page.input_ip_adress().send_keys('192.168.3.85')
    with allure.step('В поле "Секрет" ввести значение "5"'):
        authorization_page.input_secret().send_keys('5')
    authorization_page.click_on_save_button()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'TACACS'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - TACACS")
@allure.title('Проверка обязательности заполнения полей "IP - адрес" и "Секрет"')
@pytest.mark.parametrize('creds',[('',''),('192.168.1.2',''),('','5')])
def test_check_obligatory_fill_fields(creds,driver):
    ip_adress, secret = creds
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_tacacs()
    if ip_adress == '' and secret == '':
        authorization_page.input_ip_adress().clear()
        with allure.step('Оставляем поле "IP - адрес" пустым'):
            authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        with allure.step('Оставляем поле "Секрет" пустым'):
            authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения полей "IP - адрес" и "Секрет"'):
            assert authorization_page.get_list_obligatory_fill()[0].text == 'IP-адрес - обязательно для заполнения' \
               and authorization_page.get_list_obligatory_fill()[1].text == 'Секрет - обязательно для заполнения'
    elif ip_adress == '192.168.1.2':
        authorization_page.input_ip_adress().clear()
        with allure.step('В поле "IP - адрес" ввести значение "192.168.1.2"'):
            authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        with allure.step('Оставляем поле "Секрет" пустым'):
            authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "Секрет"'):
            assert authorization_page.get_text_obligatory_fill() == 'Секрет - обязательно для заполнения'
    elif secret == '5':
        authorization_page.input_ip_adress().clear()
        with allure.step('Оставляем поле "IP - адрес" пустым'):
            authorization_page.input_ip_adress().send_keys(ip_adress)
        authorization_page.input_secret().click()
        with allure.step('В поле "Секрет" ввести значение' "5"):
            authorization_page.input_secret().send_keys(secret)
        authorization_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "IP - адрес"'):
            assert authorization_page.get_text_obligatory_fill() == 'IP-адрес - обязательно для заполнения'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - TACACS")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - DC Log")
@allure.title('Создание объекта "DC Log"')
@allure.description('Для прохождения данного теста необходимо наличие на локальном компьютере валидного сертификата и ключа')
def test_create_dc_log(driver):
    with open('creds.txt', 'r') as f:
        for line in f:
            if line.__contains__('CERT'):
                cert = line.split('=')
                cert = cert[-1].strip()
            elif line.__contains__('KEY'):
                key = line.split('=')
                key = key[-1].strip()
    path_cert = cert
    path_key = key
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    with allure.step('В поле "Порт" ввести значение "5000"'):
        authorization_page.input_port().send_keys('5000')
    with allure.step('В поле "Внешний FQDN" ввести значение "123"'):
        authorization_page.input_fqdn().send_keys('123')
    with allure.step('Загружаем с локального компьютере сертификат'):
        authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    with allure.step('Загружаем с локального компьютере ключ от загруженного в предыдущем шаге сертификата'):
        authorization_page.input_download_key().send_keys(f"{path_key}")
    with allure.step('В поле "Подпись центра сертификации" ввести символы например "Подпись сертификата"'):
        authorization_page.input_certificate().send_keys('Подпись сертификата')
    with allure.step('В поле "LDAP" ввести значение "ea@testdoman.com"'):
        authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "Dc Log"'):
        authorization_page.input_login().send_keys('Dc Log')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'DC Log'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - DC Log")
@allure.title('Создание объекта "DC Log" с невалидным сертификатом')
@allure.description('Для прохождения данного теста необходимо наличие на локальном компьютере невалидного сертификата и валидного ключа')
def test_create_object_invalid_sert(driver):
    with open('creds.txt', 'r') as f:
        for line in f:
            if line.__contains__('INVALID'):
                cert = line.split('=')
                cert = cert[-1].strip()
            elif line.__contains__('KEY'):
                key = line.split('=')
                key = key[-1].strip()
    path_cert = cert
    path_key = key
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    with allure.step('В поле "Порт" ввести значение "5000"'):
        authorization_page.input_port().send_keys('5000')
    with allure.step('В поле "Внешний FQDN" ввести значение "123"'):
        authorization_page.input_fqdn().send_keys('123')
    with allure.step('Загружаем с локального компьютере сертификат'):
        authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    with allure.step('Загружаем с локального компьютере ключ от другого сертификата'):
        authorization_page.input_download_key().send_keys(f"{path_key}")
    with allure.step('В поле "Подпись центра сертификации" ввести символы например "Подпись сертификата"'):
        authorization_page.input_certificate().send_keys('Подпись сертификата')
    with allure.step('В поле "LDAP" ввести значение "ea@testdoman.com"'):
        authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "Dc Log'):
        authorization_page.input_login().send_keys('Dc Log')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    with allure.step('Проверка появления модального окна с ошибкой "Сертификат или ключ не валидный"'):
        assert authorization_page.get_text_fail_modal() == 'Сертификат или ключ не валидный'
@allure.feature("Объекты")
@allure.story("Параметры авторизации - DC Log")
@allure.title('Создание объекта без одного заполненного обязательного поля')
def test_obligatory_to_fill_port(driver):
    with open('creds.txt', 'r') as f:
        for line in f:
            if line.__contains__('CERT'):
                cert = line.split('=')
                cert = cert[-1].strip()
            elif line.__contains__('KEY'):
                key = line.split('=')
                key = key[-1].strip()
    path_cert = cert
    path_key = key
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_dc_log()
    with allure.step('Поле "Порт" оставляем пустым'):
        authorization_page.input_port().send_keys('')
    with allure.step('В поле "Внешний FQDN" ввести значение "123"'):
        authorization_page.input_fqdn().send_keys('123')
    with allure.step('Загружаем с локального компьютере сертификат'):
        authorization_page.input_download_certificate().send_keys(f"{path_cert}")
    with allure.step('Загружаем с локального компьютере ключ от загруженного в предыдущем шаге сертификата'):
        authorization_page.input_download_key().send_keys(f"{path_key}")
    with allure.step('В поле "Подпись центра сертификации" ввести символы например "Подпись сертификата"'):
        authorization_page.input_certificate().send_keys('Подпись сертификата')
    with allure.step('В поле "LDAP" ввести значение "ea@testdoman.com"'):
        authorization_page.input_url_ldap().send_keys('ea@testdoman.com')
    with allure.step('В поле "Базовая OU" ввести значение "ea"'):
        authorization_page.input_base_ou().send_keys('ea')
    with allure.step('В поле "Логин" ввести значение "Dc Log'):
        authorization_page.input_login().send_keys('Dc Log')
    with allure.step('В поле "Пароль" ввести значение "1234"'):
        authorization_page.input_password().send_keys('1234')
    authorization_page.click_on_save_button()
    with allure.step('Проверка появления модального окна с ошибкой обязательности заполнения поля "Порт"'):
        assert authorization_page.get_text_obligatory_fill() == 'Порт - обязательно для заполнения'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - DC Log")
@allure.title('Проверка записи в "Истории изменений"')
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
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert authorization_page.get_history_port() == port and authorization_page.get_history_name_certificate() == sert_name \
           and authorization_page.get_history_fill_sertification() == fill_certificate and authorization_page.get_history_name_key() == sert_key

@allure.feature("Объекты")
@allure.story("Параметры авторизации - DC Log")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - Портал")
@allure.title('Создание объекта "Портал"')
def test_create_portal(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_portal()
    authorization_page.click_on_save_button()
    authorization_page.get_type_object()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'Портал'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - Портал")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - RADIUS")
@allure.title('Создание объекта "RADIUS"')
def test_create_radius_object(driver):
    login_page = LoginPage(driver)
    authorization_page = AuthorizationPage(driver)
    login_page.login()
    authorization_page.click_on_object_button()
    authorization_page.click_on_authorization_button()
    authorization_page.click_on_add_button()
    authorization_page.click_on_list_authorization()
    authorization_page.click_on_radius()
    with allure.step('В поле "IP - адрес" ввести значения "192.168.3.85"'):
        authorization_page.input_ip_adress().send_keys('192.168.3.85')
    with allure.step('В поле "Секрет" ввести значения "5"'):
        authorization_page.input_secret().send_keys('100')
    authorization_page.click_on_save_button()
    with allure.step('Проверка создания объекта'):
        assert authorization_page.get_type_object() == 'RADIUS'

@allure.feature("Объекты")
@allure.story("Параметры авторизации - RADIUS")
@allure.title('Удаление объекта')
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
    with allure.step('Проверка удаления объекта'):
        assert authorization_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


