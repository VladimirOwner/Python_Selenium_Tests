
from pages.login_page import LoginPage
from pages.Network.interface_page import NetworkPage
import allure
from conftest import driver

@allure.feature("Сеть")
@allure.story("Интерфейсы")
@allure.title('Создание интерфейса')
def test_create_interface(driver):
    login_page = LoginPage(driver)
    network_page = NetworkPage(driver)
    login_page.login()
    network_page.click_on_network_button()
    network_page.click_on_interface_part()
    network_page.click_on_add_button()
    network_page.click_on_gateway_choose_right()
    network_page.click_on_gateway_choose_modal()
    network_page.click_on_save_button()
    with allure.step('Проверка добавление объекта Интерфейса'):
        assert network_page.get_count_interfaces() == '(1)'


@allure.feature("Сеть")
@allure.story("Интерфейсы")
@allure.title('Проверка создания копии другого интерфейса')
def test_create_same_interface(driver):
    login_page = LoginPage(driver)
    network_page = NetworkPage(driver)
    login_page.login()
    network_page.click_on_network_button()
    network_page.click_on_interface_part()
    network_page.click_on_add_button()
    network_page.click_on_gateway_choose_right()
    network_page.click_on_gateway_choose_modal()
    network_page.click_on_save_button()
    with allure.step('Появление модального окна с ошибкой'):
        assert network_page.get_modal_error_text() == 'Данный интерфейс был создан ранее'

@allure.feature("Сеть")
@allure.story("Интерфейсы")
@allure.title('Изменение интерфейса')
def test_update_interface(driver):
    login_page = LoginPage(driver)
    network_page = NetworkPage(driver)
    login_page.login()
    network_page.click_on_network_button()
    network_page.click_on_interface_part()
    network_page.click_row_in_main_frame()
    with allure.step('В правом фрейме в поле "Описание" вводим текст'):
        network_page.discription_field().send_keys('Интерфейс')
    network_page.click_on_save_button()
    with allure.step('Проверяем изменения в объекте инетрфейса'):
        assert network_page.discription_field().get_attribute('value') == 'Интерфейс'

@allure.feature("Сеть")
@allure.story("Интерфейсы")
@allure.title('Проверка записи изменений в статистике')
def test_created_and_changed_information(driver):
    login_page = LoginPage(driver)
    network_page = NetworkPage(driver)
    login_page.login()
    network_page.click_on_network_button()
    network_page.click_on_interface_part()
    network_page.click_row_in_main_frame()
    network_page.click_on_statistic_button()
    with allure.step('Проверка правильности занесения данных в статистику'):
        assert network_page.get_current_data() == network_page.get_statistic_information()


@allure.feature("Сеть")
@allure.story("Интерфейсы")
@allure.title('Удаление интерфейса')
def test_delete_interface(driver):
    login_page = LoginPage(driver)
    network_page = NetworkPage(driver)
    login_page.login()
    network_page.click_on_network_button()
    network_page.click_on_interface_part()
    network_page.click_row_in_main_frame()
    network_page.click_delete_button()
    network_page.click_confirm_delete_button()
    with allure.step('Проверка удаления объекта интерфейса'):
        assert network_page.get_count_interfaces() == '(0)'



