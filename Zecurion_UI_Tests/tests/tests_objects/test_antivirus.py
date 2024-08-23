import time

from pages.Objects.tegs import Tegs
from pages.login_page import LoginPage
from pages.Objects.antivirus import Antivirus
from test_tegs import test_create_teg as create_teg, test_delete_teg as del_teg
import pytest
#  import allure
from faker import Faker
fake = Faker()


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_object_antivirus(driver):
    random_name = fake.word()
    login(driver)
    antivirus = Antivirus(driver)
    antivirus.object_button().click()
    antivirus.antivirus_button().click()
    antivirus.add_new_object().click()
    antivirus.pencil_edit_icon().click()
    antivirus.edit_name_object().send_keys(random_name)
    antivirus.save_button().click()
    assert antivirus.get_name_object() == random_name


def test_description_field(driver):
    random_desc = fake.sentence()
    login(driver)
    antivirus = Antivirus(driver)
    antivirus.object_button().click()
    antivirus.antivirus_button().click()
    antivirus.open_object().click()
    antivirus.description_field().send_keys(random_desc)
    antivirus.save_button().click()
    antivirus.statistics().click()
    antivirus.last_change().click()
    assert antivirus.get_description() == random_desc


def test_confidence_field(driver):
    login(driver)
    antivirus = Antivirus(driver)
    antivirus.object_button().click()
    antivirus.antivirus_button().click()
    antivirus.open_object().click()
    antivirus.confidence_field().clear()
    antivirus.confidence_field().send_keys('-1')
    antivirus.save_button().click()
    assert antivirus.get_save_err() == 'Уверенность - Число должно быть целым и больше или равно 1'
    antivirus.close_modal_window().click()
    antivirus.confidence_field().clear()
    antivirus.confidence_field().send_keys('1.1')
    antivirus.save_button().click()
    assert antivirus.get_save_err() == 'Уверенность - Число должно быть целым и больше или равно 1'
    antivirus.close_modal_window().click()
    antivirus.confidence_field().clear()
    antivirus.confidence_field().send_keys('101')
    antivirus.save_button().click()
    assert antivirus.get_save_err() == 'Уверенность - Число должно быть целым и меньше или равно 100'
    antivirus.close_modal_window().click()
    antivirus.confidence_field().clear()
    antivirus.save_button().click()
    assert antivirus.get_save_err() == 'Уверенность - обязательно для заполнения'


def test_add_teg(driver):
    login(driver)
    antivirus = Antivirus(driver)
    create_teg(driver)
    antivirus.antivirus_button().click()
    antivirus.open_object().click()
    antivirus.add_teg_button().click()
    name = antivirus.get_tag_in_modal()
    antivirus.tags().click()
    antivirus.apply_tags_button().click()
    antivirus.save_button().click()
    antivirus.statistics().click()
    antivirus.last_change().click()
    assert antivirus.get_tags() == name


def test_activity(driver):
    login(driver)
    antivirus = Antivirus(driver)
    antivirus.object_button().click()
    antivirus.antivirus_button().click()
    antivirus.open_object().click()
    antivirus.activity_dropdown().click()
    antivirus.activity_off().click()
    antivirus.save_button().click()
    antivirus.statistics().click()
    antivirus.last_change().click()
    assert antivirus.get_activity() == 'Выключено'
    antivirus.close_modal_window().click()
    antivirus.basics().click()
    antivirus.activity_dropdown().click()
    antivirus.activity_on().click()
    antivirus.save_button().click()
    antivirus.statistics().click()
    antivirus.last_change().click()
    assert antivirus.get_activity() == 'Включено'
