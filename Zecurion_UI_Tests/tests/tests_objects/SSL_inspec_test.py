# import time
from pages.login_page import LoginPage
from pages.Objects.SSL_inspec import SslInspec
from test_tegs import test_create_teg as create_teg, test_delete_teg as del_teg
import allure


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Создание объекта')
def test_create_ssl(driver):
    app_page = SslInspec(driver)
    create_teg(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.add_new_object().click()
    app_page.generate_ssl().click()
    with allure.step('Ввести название сертификата'):
        app_page.input_ssl_name().send_keys('123')
        app_page.generate_button().click()
        app_page.close_modal().click()
    app_page.save_button().click()
    with allure.step('Проверка создания объекта'):
        assert app_page.get_name_object() == 'Новая SSL-инспекция'


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Редактирование названия и описания')
def test_edit(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    app_page.click_on_pencil_button()
    with allure.step('Изменить название объекта, например "123"'):
        app_page.input_pencil().send_keys('123')
    app_page.save_button().click()
    with allure.step('Проверка изменения названия на новое'):
        assert app_page.get_new_object() == '123'
    with allure.step('В поле описание ввести "123"'):
        app_page.description_field().send_keys('123')
        app_page.save_button().click()
    with allure.step('Проверка добавления описания в объект'):
        assert app_page.get_description_on_main_frame() == '123'


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Редактирование типа')
def test_dropdown(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    app_page.click_on_pencil_button()
    with allure.step('Изменить значение dropdown'):
        app_page.open_dropdown().click()
        app_page.select_dropdown().click()
    app_page.save_button().click()
    with allure.step('Проверка изменения значения dropdown'):
        assert app_page.get_dropdown_on_main_frame() == 'ГОСТ'


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Изменение чекбоксов')
def test_checkbox(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    with allure.step('Выбрать общий приватный ключ'):
        app_page.select_checkbox1().click()
        app_page.save_button().click()
    with allure.step('Выбрать Поддерживать технологии Cloudflare'):
        app_page.select_checkbox2().click()
        app_page.save_button().click()


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Изменение активности')
def test_activity(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    with allure.step('Открыть dropdown активность'):
        app_page.activity_dropdown().click()
        app_page.activity_select().click()
        app_page.save_button().click()


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Проверка записи в "Истории изменений"')
def test_history_button(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    app_page.click_on_statistic_button()
    app_page.click_on_history_button()
    name = app_page.get_new_object()
    description = app_page.get_description_on_main_frame()
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert app_page.get_history_name() == name and app_page.get_history_description() == description


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Отмена изменений')
def test_cancel_change(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    description = app_page.description_field().get_attribute('value')
    with allure.step('Очистить поле "Описание"'):
        app_page.description_field().clear()
    app_page.click_on_cancel_button()
    app_page.click_on_confirm_cancel_button()
    with allure.step('Проверка отмены изменений'):
        assert app_page.get_description_on_main_frame() == description


# @allure.feature("Объекты")
# @allure.story("SSL-инспекция")
# @allure.title('Скачивание сертификата')
# def test_download(driver):
#   login(driver)
#   app_page = SslInspec(driver)
#   app_page.object_button().click()
#   app_page.ssl_button().click()
#   app_page.select_object().click()
#   with allure.step('Скачать сертификат'):
#      app_page.download_certif().click()
#    time.sleep(2)
#    with allure.step('Скачать ключ'):
#      app_page.download_key().click()
#    time.sleep(2)


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Добавление тега')
def test_ssl_addteg(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    with allure.step('Нажать на "+" в строке Теги'):
        app_page.add_teg()
    with allure.step('В модальном окне выбрать тег и применить его'):
        app_page.select_teg()
        name_teg = app_page.get_teg_name()
        app_page.accept_teg()
        app_page.save_button().click()
    with allure.step('Проверка добавления тега'):
        assert app_page.get_teg_info() == name_teg


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Удаление тега')
def test_ssl_delteg(driver):
    login(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    with allure.step('Нажать на "x" в строке Теги'):
        app_page.del_teg()
        app_page.save_button().click()
    with allure.step('Проверка удаления тега'):
        assert app_page.get_teg_info_del() == 'Не установлено'


@allure.feature("Объекты")
@allure.story("SSL-инспекция")
@allure.title('Удаление объекта')
def test_delete_ssl(driver):
    del_teg(driver)
    app_page = SslInspec(driver)
    app_page.object_button().click()
    app_page.ssl_button().click()
    app_page.select_object().click()
    app_page.click_on_delete_button()
    app_page.click_on_confirm_delete_button()
    with allure.step('Проверка удаления объекта'):
        assert app_page.get_info_del() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
