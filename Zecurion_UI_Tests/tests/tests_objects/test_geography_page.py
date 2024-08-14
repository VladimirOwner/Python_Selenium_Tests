import time
from pages.login_page import LoginPage
from pages.Objects.geography_page import GeographyPage
import allure

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Создание объекта географии')
def test_create_geography_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    geography_page.click_on_add_button()
    geography_page.click_on_save_button()
    with allure.step('Проверка появления объекта в основном фрейме'):
        assert  geography_page.get_name_object() == 'Новый регион'

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Изменение имени объекта')
def test_update_name_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_pencil_button()
    with allure.step('Изменить название объекта, например "Европа"'):
        geography_page.input_pencil_field().send_keys('Европа')
    geography_page.click_on_save_button()
    with allure.step('Проверка изменения имени на новое'):
        assert geography_page.get_name_object() == 'Европа'

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Добавление описания')
def test_add_description(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    with allure.step('В поле описание ввести "Страны Европы"'):
        geography_page.description_field().send_keys('Страны Европы')
    geography_page.click_on_save_button()
    with allure.step('Проверка добавления описания в объект'):
        assert geography_page.get_description_on_main_frame() == 'Страны Европы'

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Добавление региона')
def test_add_region(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_add_region_button()
    geography_page.choose_region()
    geography_page.click_save_on_modal()
    geography_page.click_on_save_button()
    count_country = geography_page.count_country_on_rigth_frame()
    with allure.step('Проверка добавления стран в объект относящихся к выбранному региону'):
        assert count_country == 54
@allure.feature("Объекты")
@allure.story("География")
@allure.title('Добавление страны в объект')
def test_add_country(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    count_country = geography_page.count_country_on_rigth_frame()
    geography_page.click_on_add_region_button()
    geography_page.click_on_drop_down_modal()
    geography_page.click_on_checkbox_country()
    geography_page.click_save_on_modal()
    geography_page.click_on_save_button()
    with allure.step('Проверка добавления страны в объект'):
        assert geography_page.count_country_on_rigth_frame() == count_country+1
@allure.feature("Объекты")
@allure.story("География")
@allure.title('Проверка работы быстрого поиска в модальном окне выбора региона')
def test_check_fast_search(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_add_region_button()
    with allure.step('В строке быстрого поиска ввести "Россия"'):
        geography_page.input_modal_fast_search().send_keys('Россия')
    continent = geography_page.get_text_continent()
    with allure.step('Проверка появления региона относящегося к данной стране'):
        assert continent == 'Европа'

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Проверка записи в "Истории изменений"')
def test_check_history_changing(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    name = geography_page.get_name_object()
    description = geography_page.get_description_on_main_frame()
    geography_page.click_on_statistic_button()
    geography_page.click_on_history_button()
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert geography_page.get_name_object() == name and geography_page.get_description_on_history_changing() == description

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Отмена изменений')
def test_cancel_changing(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    description = geography_page.get_description_on_main_frame()
    with allure.step('Очищаем поле "Описание"'):
        geography_page.description_field().clear()
    with allure.step('В поле "Описание" вводим "Азиатские страны"'):
        geography_page.description_field().send_keys('Азиатские страны')
    geography_page.click_on_cancel_button()
    geography_page.click_on_confirm_cancel_button()
    with allure.step('Проверка отмены изменений'):
        assert geography_page.get_description_on_main_frame() == description

@allure.feature("Объекты")
@allure.story("География")
@allure.title('Удаление объекта')
def test_delete_object(driver):
    login_page = LoginPage(driver)
    geography_page = GeographyPage(driver)
    login_page.login()
    geography_page.click_on_object_button()
    geography_page.click_on_geography_button()
    with allure.step('В основном фрейме выбрать созданный объект'):
        geography_page.choose_object_in_main_frame().click()
    geography_page.click_on_delete_button()
    geography_page.click_on_confirm_delete_button()
    with allure.step('Проверка удаления объекта'):
        assert geography_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'