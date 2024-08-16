import allure
from pages.login_page import LoginPage
from pages.Objects.protocols import Protocols


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


@allure.feature('Объекты')
@allure.story('Протоколы')
@allure.title('Создание объекта протокол')
def test_create_object_protocol(driver):
    login(driver)
    protocols = Protocols(driver)
    protocols.object_button().click()
    protocols.protocol_button().click()
    protocols.add_new_protocol().click()
    protocols.save_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый протокол"'):
        protocols.input_fast_search().send_keys('Новый протокол')
    protocols.get_author()
    with allure.step('Проверка создания нового объекта через основной фрейм'):
        assert protocols.get_name_protocol() == 'Новый протокол'


@allure.feature('Объекты')
@allure.story('Протоколы')
@allure.title('Изменение имени протокола')
def test_change_name_protocol(driver):
    login(driver)
    protocols = Protocols(driver)
    protocols.object_button().click()
    protocols.protocol_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый протокол"'):
        protocols.input_fast_search().send_keys('Новый протокол')
    protocols.get_author()
    protocols.name_protocol().click()
    protocols.pencil_edit_icon().click()
    protocols.input_edit_name().send_keys('selenium_test_edit_protocol_name')
    protocols.save_button().click()
    with allure.step('Очистить строку быстрого поиска'):
        protocols.input_fast_search().clear()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_protocol_name"'):
        protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    with allure.step('Проверка соответствия измененного имени'):
        assert protocols.get_name_protocol() == 'selenium_test_edit_protocol_name'


@allure.feature('Объекты')
@allure.story('Протоколы')
@allure.title('Изменение поля "Описание"')
def test_description_field(driver):
    login(driver)
    protocols = Protocols(driver)
    protocols.object_button().click()
    protocols.protocol_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_protocol_name"'):
        protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.name_protocol().click()
    with allure.step('Ввести в поле описания "selenium_test"'):
        protocols.input_description_field().send_keys('selenium_test')
    protocols.save_button().click()
    protocols.statistics().click()
    protocols.last_change().click()
    with allure.step('Проверка добавления описания объекта'):
        assert protocols.get_description() == 'selenium_test'


@allure.feature('Объекты')
@allure.story('Протоколы')
@allure.title('Добавле DPI протокола')
def test_add_dpi_protocol(driver):
    login(driver)
    protocols = Protocols(driver)
    protocols.object_button().click()
    protocols.protocol_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_protocol_name"'):
        protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.name_protocol().click()
    protocols.dpi_protocol_field().click()
    protocols.checkbox_media().click()
    protocols.save_dpi_modal().click()
    with allure.step('Проверка добавления dpi протокола в объект'):
        assert protocols.get_dpi_protocol() == 'Media'


@allure.feature('Объекты')
@allure.story('Протоколы')
@allure.title('Удаление объекта протокол')
def test_delete_protocol(driver):
    login(driver)
    protocols = Protocols(driver)
    protocols.object_button().click()
    protocols.protocol_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_protocol_name"'):
        protocols.input_fast_search().send_keys('selenium_test_edit_protocol_name')
    protocols.get_author()
    protocols.name_protocol().click()
    protocols.delete_object().click()
    protocols.accept_delete_object().click()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert protocols.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
