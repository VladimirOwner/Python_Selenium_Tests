from pages.login_page import LoginPage
from pages.Objects.application import ApplicationPage
import pytest
import allure

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Создание категории приложений')
def test_create_app_category(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.click_on_add_button()
    app_page.click_on_save_button()
    with allure.step('Проверка создания объекта'):
        assert app_page.get_name_object() == 'Новая категория приложений'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Изменение названия категории')
def test_change_name_category(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_pencil_button()
    with allure.step('Изменить название категории, например "Мессенджеры"'):
        app_page.input_pencil().send_keys('Мессенджеры')
    app_page.click_on_save_button()
    with allure.step('Проверка изменения названия на новое'):
        assert app_page.get_name_object() == 'Мессенджеры'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Добавление описания')
def test_add_description(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    with allure.step('В поле описание ввести "Telegram"'):
        app_page.description_field().send_keys('Telegram')
    app_page.click_on_save_button()
    with allure.step('Проверка добавления описания в объект'):
        assert app_page.get_description_on_main_frame() == 'Telegram'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Проверка записи в "Истории изменений"')
def test_history_button(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    name = app_page.get_name_object()
    description = app_page.get_description_on_main_frame()
    app_page.click_on_statistic_button()
    app_page.click_on_history_button()
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert app_page.get_history_name() == name and app_page.get_history_description() == description

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Создание приложения')
def test_create_app(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_category_button()
    app_page.click_on_add_button()
    with allure.step('В поле "Порт" ввести значение "443"'):
        app_page.input_port().send_keys('443')
    with allure.step('В поле "Хост" ввести значение "web.telegram.org"'):
        app_page.input_host().send_keys('web.telegram.org')
    app_page.click_on_save_button()
    with allure.step('Проверка создания приложения'):
        assert app_page.get_name_object() == 'Новое приложение'

@pytest.mark.skip('Баг ZNGFW-1431')
def test_change_category_app(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_category_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_dropdown()
    app_page.click_on_network_category()
    app_page.click_on_save_button()
    app_page.click_on_statistic_button()
    app_page.click_on_history_button()

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Проверка обязательности заполнения полей "Порт" и "Хост"')
@pytest.mark.parametrize('creds',[('',''),('80',''),('','telegram.org')])
def test_create_without_obligatory_fill(creds,driver):
    port, host = creds
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_category_button()
    app_page.click_on_add_button()
    if port == '' and host == '':
        with allure.step('Поля "Порт" и "Хост" оставляем пустыми'):
            app_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой обязательности заполнения полей "Порт" и "Хост"'):
            assert app_page.get_list_obligatory_fill()[0].text == 'Порты - обязательно для заполнения' and app_page.get_list_obligatory_fill()[1].text == 'Хосты - обязательно для заполнения'
    elif port == '80':
        with allure.step('В поле "Порт" ввести значение "80", поле "Хост" оставляем пустым'):
            app_page.input_port().send_keys(port)
        app_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой обязательности заполнения поля "Хост"'):
            assert app_page.get_text_fail_modal() == 'Хосты - обязательно для заполнения'
    elif host == 'telegram.org':
        with allure.step('В поле "Хост" ввести значение "telegram.org", поле "Порт" оставляем пустым'):
            app_page.input_host().send_keys(host)
        app_page.click_on_save_button()
        with allure.step('Проверка появления модального окна с ошибкой обязательности заполнения поля "Порт"'):
            assert app_page.get_text_fail_modal() == 'Порты - обязательно для заполнения'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Изменение названия приложения')
def test_change_name_app(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_category_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_pencil_button()
    with allure.step('Изменить название приложения, например "Telegram App"'):
        app_page.input_pencil().send_keys('Telegram App')
    app_page.click_on_save_button()
    with allure.step('Проверка изменения названия на новое'):
        assert app_page.get_name_object() == 'Telegram App'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Отмена изменений')
def test_cancel_change(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    description = app_page.description_field().get_attribute('value')
    with allure.step('Очистить поле "Описание"'):
        app_page.description_field().clear()
    app_page.click_on_cancel_button()
    app_page.click_on_confirm_cancel_button()
    with allure.step('Проверка отмены изменений'):
        assert app_page.get_description_on_main_frame() == description

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Удаление приложения')
def test_delete_app(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_category_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_delete_button()
    app_page.click_on_confirm_delete_button()
    with allure.step('Проверка удаления приложения'):
        assert app_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

@allure.feature("Объекты")
@allure.story("Приложения")
@allure.title('Удаление категории')
def test_delete_category_app(driver):
    login_page = LoginPage(driver)
    app_page = ApplicationPage(driver)
    login_page.login()
    app_page.click_on_object_button()
    app_page.click_on_app_button()
    app_page.choose_object_in_main_frame().click()
    app_page.click_on_delete_button()
    app_page.click_on_confirm_delete_button()
    with allure.step('Проверка удаления категории'):
        assert app_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

