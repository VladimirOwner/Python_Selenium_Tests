import time
from pages.login_page import LoginPage
from pages.Objects.geography_page import GeographyPage
import allure

def test_create_geography_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.click_on_add_button()
    geography_page.click_on_save_button()
    assert  geography_page.get_name_object() == 'Новый регион'

def test_update_name_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_pencil_button()
    geography_page.input_pencil_field().send_keys('Европа')
    geography_page.click_on_save_button()
    assert geography_page.get_name_object() == 'Европа'

def test_add_description(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    geography_page.description_field().send_keys('Страны Европы')
    geography_page.click_on_save_button()
    assert geography_page.get_description_on_main_frame() == 'Страны Европы'

def test_add_region(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_add_region_button()
    geography_page.choose_region()
    geography_page.click_save_on_modal()
    geography_page.click_on_save_button()
    count_country = geography_page.count_country_on_rigth_frame()
    assert count_country == 54

def test_add_country(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    count_country = geography_page.count_country_on_rigth_frame()
    geography_page.click_on_add_region_button()
    geography_page.click_on_drop_down_modal()
    geography_page.click_on_checkbox_country()
    geography_page.click_save_on_modal()
    geography_page.click_on_save_button()
    assert geography_page.count_country_on_rigth_frame() == count_country+1

def test_check_fast_search(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_add_region_button()
    geography_page.input_modal_fast_search().send_keys('Россия')
    continent = geography_page.get_text_continent()
    assert continent == 'Европа'


def test_check_history_changing(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    name = geography_page.get_name_object()
    description = geography_page.get_description_on_main_frame()
    geography_page.click_on_statistic_button()
    geography_page.click_on_history_button()
    assert geography_page.get_name_object() == name and geography_page.get_description_on_history_changing() == description

def test_cancel_changing(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    description = geography_page.get_description_on_main_frame()
    geography_page.description_field().send_keys('Азиатские страны')
    geography_page.click_on_cancel_button()
    assert geography_page.get_description_on_main_frame() == description


def test_delete_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_delete_button()
    geography_page.click_on_confirm_delete_button()
    assert geography_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'