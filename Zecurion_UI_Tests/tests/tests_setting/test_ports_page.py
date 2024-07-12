import time
import allure
from pages.login_page import LoginPage
from pages.Settings.ports_page import PortsPage
from conftest import driver

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Создание объекта Портры прокси')
def test_create_ports(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    count = ports_page.count_objects_ports()
    ports_page.click_on_add_button()
    ports_page.click_on_add_ports()
    with allure.step('В поле "Порты" ввести значение'):
        ports_page.input_port_field().send_keys('80')
    ports_page.click_on_invisible_mode_checkbox()
    ports_page.click_on_protocol_dropdown()
    ports_page.click_choose_protocol()
    with allure.step('В поле "Порт" ввести значение'):
        ports_page.invisible_port_field().send_keys('8080')
    ports_page.click_on_save_button()
    ports_page.count_objects_ports()
    with allure.step('Проверка создания объекта "Порты прокси"'):
        assert ports_page.count_objects_ports() == count+1 , 'Неверное количество объектов'

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Проверка записи изменений в статистике')
def test_get_statistic_information(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    ports_page.choose_object_ports()
    ports_page.click_on_statistic_information()
    with allure.step('Проверка правильности занесения данных в статистику'):
        assert ports_page.get_statistic_information() == ports_page.get_current_data(), 'Неверная дата создания'

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Изменение объекта Порты-прокси')
def test_update_ports_object(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    ports_page.choose_object_ports()
    with allure.step('В поле "Описание" ввести произвольные символы'):
        ports_page.discription_field().send_keys('Порт 80')
    ports_page.click_on_save_button()
    with allure.step('Проверка изменения объекта "Порты-прокси"'):
        assert ports_page.get_discription_text_in_main_frame() == 'Порт 80', 'Описание в основном фрейме не совпадает с описанием в объекте'

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Удаление объекта "Порты прокси"')
def test_delete_object_port(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    count = ports_page.count_objects_ports()
    ports_page.choose_object_ports()
    ports_page.click_on_delete_button()
    ports_page.click_on_confirm_delete_button()
    ports_page.count_objects_ports()
    with allure.step('Проверка удаления объекта "Порты прокси"'):
        assert ports_page.count_objects_ports() == count-1

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Создание объекта "Порты прокси" без заполнения обязательных полей')
def test_create_without_obligatory_fill(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    ports_page.click_on_add_button()
    ports_page.click_on_add_ports()
    ports_page.click_on_save_button()
    with allure.step('Проверка появления модального окна с текстом об обязательности заполнения поля "Порты"'):
        assert ports_page.get_error_modal_text() == 'Порты - обязательно для заполнения'

@allure.feature("Настройки")
@allure.story("Порты-прокси")
@allure.title('Проверка появления сообщения об обязательности заполнения полей "Порты" и "Порт"')
def test_check_obligatory_to_fill(driver):
    login_page = LoginPage(driver)
    ports_page = PortsPage(driver)
    login_page.login()
    ports_page.click_on_setting_button()
    ports_page.click_on_ports()
    ports_page.click_on_add_button()
    ports_page.click_on_add_ports()
    ports_page.click_on_invisible_mode_checkbox()
    with allure.step('Проверка появления сообщения об обязательности заполнения полей "Порты" и "Порт"'):
        assert ports_page.get_text_obligatory_to_fill_port() and ports_page.get_text_obligatory_to_fill_ports() == 'обязательно для заполнения'