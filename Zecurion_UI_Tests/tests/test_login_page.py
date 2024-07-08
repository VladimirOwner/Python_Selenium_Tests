import pytest
from pages.login_page import LoginPage
from pages.header_page import HeaderPage
from conftest import driver
import allure

@allure.feature("Страница авторизации")
@allure.title('Авторизация пользователя с валидными данными')
def test_login_user_valid_data(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.open()
    with allure.step('Ввод данных в поле \'Пользователь\''):
        login_page.user_field().send_keys('admin')
    with allure.step('Ввод данных в поле \'Пароль\''):
        login_page.password_field().send_keys('admin')
    with allure.step('Нажатие на кнопку войти'):
        login_page.button_click()
    with allure.step('Проверка успешной авторизации'):
        assert header_page.user_name_text() =='Администратор', "Имя пользователя неверно"

@allure.feature("Страница авторизации")
@allure.title('Авторизация пользователя с невалидными данными')
@pytest.mark.parametrize('creds',[('1','admin'),('admin','!23qw')])
def test_invalid_data_user_and_password(creds,driver):
    login, password = creds
    login_page = LoginPage(driver)
    login_page.open()
    if login == '1':
        with allure.step('Ввод некорректных данных в поле \'Пользователь\''):
            login_page.user_field().send_keys(login)
    else:
        with allure.step('Ввод корректных данных в поле \'Пользователь\''):
            login_page.user_field().send_keys(login)
    if password == '!23qw':
        with allure.step('Ввод некорректных данных в поле \'Пароль\''):
            login_page.password_field().send_keys(password)
    else:
        with allure.step('Ввод корректных данных в поле \'Пароль\''):
            login_page.password_field().send_keys(password)
    with allure.step('Нажатие на кнопку войти'):
        login_page.button_click()
    with allure.step('Проверка появления сообщения о неверном логине или пароле'):
        assert login_page.get_error_text() == 'Неверный логин или пароль'

@allure.feature("Страница авторизации")
@allure.title('Проверка появления сообщения \'обязательно для заполнения\' в поле \'Пользователь\'или\'Пароль\'')
@pytest.mark.parametrize('creds',[('','admin'),('admin','')])
def test_text_apperiance_for_field(creds,driver):
    login, password = creds
    login_page = LoginPage(driver)
    login_page.open()
    if login == '':
        with allure.step('Поле \'Пользоватьель\' пустое'):
            login_page.user_field().send_keys(login)
    else:
        with allure.step('Ввод данных в поле \'Пользователь\''):
            login_page.user_field().send_keys(login)
    if password == '':
        with allure.step('Поле \'Пароль\' пустое'):
            login_page.password_field().send_keys(password)
    else:
        with allure.step('Ввод данных в поле \'Пароль\''):
            login_page.password_field().send_keys(password)
    if login == '':
        with allure.step('Проверка появления сообщения \'обязательно для заполнения\' под полем \'Пользователь\''):
            assert login_page.get_empty_user_field_text().text == 'обязательно для заполнения'
    elif password == '':
        with allure.step('Проверка появления сообщения \'обязательно для заполнения\' под полем \'Пароль\''):
            assert login_page.get_empty_password_field_text().text == 'обязательно для заполнения'