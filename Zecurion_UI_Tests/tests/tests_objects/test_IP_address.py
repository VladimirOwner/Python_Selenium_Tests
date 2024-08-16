import time
import allure
from pages.login_page import LoginPage
from pages.Objects.ip_address import IpAddress


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Создание объекта IP-адреса')
def test_create_ip_object(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    ip_address.add_new_ip_address().click()
    with allure.step('Ввести IP в поле "IP адрес"'):
        ip_address.input_ip().send_keys('1.1.1.1')
    ip_address.save_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый IP-адрес"'):
        ip_address.input_fast_search().send_keys('Новый IP-адрес')
    ip_address.get_author()
    with allure.step('Проверка создания нового объекта через основной фрейм'):
        assert ip_address.get_name_of_ip_object() == 'Новый IP-адрес'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Изменение имени IP-адреса')
def test_change_name_ip_object(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый IP-адрес"'):
        ip_address.input_fast_search().send_keys('Новый IP-адрес')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    ip_address.pencil_edit_icon().click()
    with allure.step('Ввести новое имя объекта "selenium_test_edit_IP_name"'):
        ip_address.input_edit_name().send_keys('selenium_test_edit_IP_name')
    ip_address.save_button().click()
    with allure.step('Очистить строку быстрого поиска'):
        ip_address.input_fast_search().clear()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    ip_address.get_author()
    with allure.step('Проверка изменения имени объекта на новое'):
        assert ip_address.get_name_of_ip_object() == 'selenium_test_edit_IP_name'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Изменение поля "Описание"')
def test_change_description(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести новое имя объекта "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    with allure.step('Ввести в строке описания "selenium_test_edit_description"'):
        ip_address.input_description_field().send_keys('selenium_test_edit_description')
    ip_address.save_button().click()
    ip_address.statistics().click()
    ip_address.last_change().click()
    with allure.step('Проверка добавления описания объекта'):
        assert ip_address.get_description() == 'selenium_test_edit_description'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Изменение поля "IP-адрес"')
def test_change_ip_address(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    ip_address.input_ip_field().clear()
    with allure.step('Изменить в строке IP-адрес значение на "192.168.0.160"'):
        ip_address.input_ip_field().send_keys('192.168.0.160')
    ip_address.save_button().click()
    ip_address.statistics().click()
    ip_address.last_change().click()
    with allure.step('Проверка изменения IP-адреса объекта'):
        assert ip_address.get_ip() == '192.168.0.160'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Валидация пустой строки "IP-адрес"')
def test_empty_ip_address(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    with allure.step('Очистить поле "IP-адрес"'):
        ip_address.input_ip_field().clear()
    ip_address.save_button().click()
    with allure.step('Проверка валидации поля "IP-адрес" на обязательность заполнения'):
        assert ip_address.get_error_empty_ip() == 'IP-адрес - обязательно для заполнения'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Валидация неправильного заполнения строки "IP-адрес"')
def test_incorrect_ip_address(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    with allure.step('Очистить поле "IP-адрес"'):
        ip_address.input_ip_field().clear()
    with allure.step('Изменить в строке IP-адрес значение на "192.168.0.160."'):
        ip_address.input_ip_field().send_keys('192.168.0.160.')
    ip_address.save_button().click()
    with allure.step('Проверка валидации поля "IP-адрес" с невалидным значением'):
        assert ip_address.get_error_empty_ip() == 'IP-адрес - Некорректное значение'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Добавление второго IP-адреса в объект')
def test_add_multiple_ip_address(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    ip_address.add_new_ip_field()
    with allure.step('Ввести второй IP-адрес в добавленное поле'):
        ip_address.input_second_ip().send_keys('192.168.0.161')
    ip_address.save_button().click()
    ip_address.statistics().click()
    ip_address.last_change().click()
    with allure.step('Проверка добавления двух IP-адресов в объект'):
        assert ip_address.get_ip() == '192.168.0.160, 192.168.0.161'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Удаление первого IP-адреса в объекте')
def test_delete_ip_address(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    ip_address.ip_clear_button().click()
    ip_address.save_button().click()
    ip_address.statistics().click()
    ip_address.last_change().click()
    with allure.step('Проверка удаления первого IP-адреса в объекте'):
        assert ip_address.get_ip() == '192.168.0.161'


@allure.feature('Объекты')
@allure.story('IP адреса')
@allure.title('Удаление объекта IP-адрес')
def test_delete_ip_object(driver):
    login(driver)
    ip_address = IpAddress(driver)
    ip_address.object_button().click()
    ip_address.ip_address_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_IP_name"'):
        ip_address.input_fast_search().send_keys('selenium_test_edit_IP_name')
    time.sleep(1)
    ip_address.get_author()
    time.sleep(1)
    ip_address.open_object().click()
    ip_address.delete_object()
    ip_address.accept_delete_object()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert ip_address.get_no_rows_overlay() == ('По вашему запросу ничего не найдено, попробуйте изменить условия '
                                                    'поиска.')
