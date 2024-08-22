#  import time
#  import allure

from pages.login_page import LoginPage
from pages.Objects.services import Services
from faker import Faker
fake = Faker()


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_object_services(driver):
    random_port = fake.port_number()
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.add_new_object().click()
    services.ports_field().send_keys(random_port)
    services.save_button().click()
    services.statistics().click()
    services.last_change().click()
    assert services.get_ports() == random_port
    assert services.get_name_object() == 'Новый сервис'


def test_edit_name_object(driver):
    random_name = fake.word()
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.object().click()
    services.pencil_edit_icon().click()
    services.edit_name_field().send_keys(random_name)
    services.save_button().click()
    assert services.get_name_object() == random_name


def test_change_description(driver):
    random_name = fake.word()
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.object().click()
    services.description_field().send_keys(random_name)
    services.save_button().click()
    services.statistics().click()
    services.last_change().click()
    assert services.get_description() == random_name


def test_empty_ports_validate(driver):
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.object().click()
    services.ports_field().clear()
    services.save_button().click()
    assert services.get_ports_err_validate() == 'Порт - обязательно для заполнения'


def test_incorrect_ports_validate(driver):
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.object().click()
    services.ports_field().clear()
    services.ports_field().send_keys('-1')
    services.save_button().click()
    assert services.get_ports_err_validate() == 'Порт - Некорректное значение'


def test_delete_object(driver):
    login(driver)
    services = Services(driver)
    services.object_button().click()
    services.services_button().click()
    services.object().click()
    services.delete_object().click()
    services.accept_delete_object().click()
    assert services.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'