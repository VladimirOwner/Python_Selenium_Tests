import pytest
from pages.Network.zone_page import ZonePage
from pages.login_page import LoginPage
import allure
from conftest import driver

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Создание зоны')
def test_create_zone(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_add_button()
    with allure.step('В поле "Уровень безопасности" ввести целое число от 1 до 255'):
        zone_page.securyty_level_field().send_keys("50")
    zone_page.click_on_gateway_choose_right()
    zone_page.click_on_gateway_choose_modal()
    zone_page.click_on_add_interface_button()
    zone_page.click_on_choose_modal_interface()
    zone_page.click_apply_button()
    zone_page.click_save_button()
    with allure.step('Проверка создания объекта "Зона"'):
        assert zone_page.get_count_zone() == '(1)'

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Проверка создания объекта зона с одним и тем же интерфейсом')
def test_create_same_zone(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_add_button()
    with allure.step('В поле "Уровень безопасности" ввести целое число от 1 до 255'):
        zone_page.securyty_level_field().send_keys("50")
    zone_page.click_on_gateway_choose_right()
    zone_page.click_on_gateway_choose_modal()
    zone_page.click_on_add_interface_button()
    zone_page.click_on_choose_modal_interface()
    zone_page.click_apply_button()
    zone_page.click_save_button()
    with allure.step('Проверка появление модального окна с ошибкой'):
        assert zone_page.get_modal_error_text() == 'Данные интерфейсы были ранее указаны в других зонах'

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Изменение объекта зона')
def test_update_zone(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_row_in_main_frame()
    zone_page.discription_field().send_keys("Закрытая сеть")
    zone_page.click_save_button()
    with allure.step('Проверяем изменения в объекте зона'):
        assert zone_page.discription_field().get_attribute('value') == 'Закрытая сеть'

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Проверка функционала кнопки "Отмена"')
def test_check_cancel_button(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_row_in_main_frame()
    zone_page.discription_field().send_keys("Закрытая сеть")
    zone_page.click_on_cancel_button()
    zone_page.click_confirm_cancel_button()
    with allure.step('Проверяем что изменения были отменены'):
        assert zone_page.discription_field().get_attribute('value') == ''

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Проверка записи изменений в статистике')
def test_created_and_changed_information(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_row_in_main_frame()
    zone_page.click_statistic_button()
    with allure.step('Проверка правильности занесения данных в статистику'):
        assert zone_page.get_statistic_information() == zone_page.get_current_data()

@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Удаление объекта зона')
def test_delete_zone(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_row_in_main_frame()
    zone_page.click_delete_button()
    zone_page.click_confirm_delete_button()
    with allure.step('Проверка удаления объекта зона'):
        assert zone_page.get_count_zone() == '(0)'


@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Проверка поля "Уровень безопасности" на класс эквивалентности')
@pytest.mark.parametrize('creds',[('0'),('256')])
def test_check_security_level_field(creds,driver):
    count = creds
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_add_button()
    with allure.step('В поле "Уровень безопасности" ввести невалидное число'):
        zone_page.securyty_level_field().send_keys(count)
        if count == '0':
            with allure.step("Поверка появления подсказки что число должно быть целым и больше 0"):
                assert zone_page.get_error_text_count_more_one() == 'Число должно быть целым и больше или равно 1'
        else:
            with allure.step("Поверка появления подсказки что число должно быть целым и меньше 255"):
                assert zone_page.get_error_text_count_less() == 'Число должно быть целым и меньше или равно 255'


@allure.feature("Сеть")
@allure.story("Зоны")
@allure.title('Проверка обязательности заполнения полей')
def test_obligatory_fields(driver):
    login_page = LoginPage(driver)
    zone_page = ZonePage(driver)
    login_page.login()
    zone_page.click_on_network_button()
    zone_page.click_on_zone_part()
    zone_page.click_on_add_button()
    zone_page.click_save_button()
    with allure.step("Проверка появления модального окна с ошибкой об обязательности заполнения полей"):
        assert zone_page.get_gateway_error_text() == 'Шлюз - Шлюз должен быть выбран' and zone_page.get_security_level_error_text() == 'Уровень безопасности - обязательно для заполнения'