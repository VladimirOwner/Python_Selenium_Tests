import time

import allure
from pages.login_page import LoginPage
from pages.Settings.dns_page import DNSPage
from conftest import driver

@allure.feature("Настройки")
@allure.story("DNS-серверы")
@allure.title('Создание DNS-сервера')
def test_create_dns(driver):
    login_page = LoginPage(driver)
    dns_page = DNSPage(driver)
    login_page.login()
    dns_page.click_on_setting_button()
    dns_page.click_on_dns_servers_part()
    dns_page.click_on_add_button()
    dns_page.dns_server_field().send_keys('192.168.0.122')
    dns_page.click_on_add_dns_server()
    dns_page.dns_server_field_second().send_keys('192.168.0.10')
    dns_page.click_on_save_button()
    dns_page.objects_in_main_frame()
    with allure.step('Проверка создания объекта dns-сервера'):
        assert dns_page.get_count_object_dns() == 2 , 'Неверное количество объектов DNS-серверов'

@allure.feature("Настройки")
@allure.story("DNS-серверы")
@allure.title('Изменение объекта DNS-сервера')
def test_update_dns(driver):
    login_page = LoginPage(driver)
    dns_page = DNSPage(driver)
    login_page.login()
    dns_page.click_on_setting_button()
    dns_page.click_on_dns_servers_part()
    with allure.step('В основном фрейме выбрать объект dns-cервера'):
        dns_page.objects_in_main_frame().click()
    dns_page.discription_field().send_keys('Мое описание')
    dns_page.click_on_save_button()
    with allure.step('Проверяем изменения в объекте dns-cерверы'):
        assert dns_page.get_discription() == 'Мое описание' , 'Неверное описание'


@allure.feature("Настройки")
@allure.story("DNS-серверы")
@allure.title('Проверка записи изменений в статистике')
def test_created_and_changed_information(driver):
    login_page = LoginPage(driver)
    dns_page = DNSPage(driver)
    login_page.login()
    dns_page.click_on_setting_button()
    dns_page.click_on_dns_servers_part()
    with allure.step('В основном фрейме выбрать объект dns-cервера'):
        dns_page.objects_in_main_frame().click()
    dns_page.click_on_statistic_button()
    with allure.step('Проверка правильности занесения данных в статистику'):
        assert dns_page.get_current_data() == dns_page.get_statistic_information()


@allure.feature("Настройки")
@allure.story("DNS-серверы")
@allure.title('Удаление DNS-сервера')
def test_delete_dns(driver):
    login_page = LoginPage(driver)
    dns_page = DNSPage(driver)
    login_page.login()
    dns_page.click_on_setting_button()
    dns_page.click_on_dns_servers_part()
    with allure.step('В основном фрейме выбрать объект dns-cервера'):
        dns_page.objects_in_main_frame().click()
    dns_page.click_on_delete_button()
    dns_page.click_on_confirm_delete()
    with allure.step('Проверка удаления объекта dns-сервера'):
        assert dns_page.get_count_object_dns() == 1 , 'Неверное количество объектов DNS-серверов'