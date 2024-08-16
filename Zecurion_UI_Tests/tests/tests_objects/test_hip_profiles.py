import time
import allure

from pages.login_page import LoginPage
from pages.Objects.hip_profiles import Hipprofiles


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


@allure.feature('Объекты')
@allure.story('HIP-профили')
@allure.title('Создание объекта HIP-профиль')
def test_create_object_hip_profile(driver):
    login(driver)
    hip_profiles = Hipprofiles(driver)
    hip_profiles.object_button().click()
    hip_profiles.hip_profiles_button().click()
    hip_profiles.add_new_object().click()
    with allure.step('В поле ОС ввести значение "Windows'):
        hip_profiles.os_field().send_keys('Windows')
    with allure.step('В поле Браузер ввести значение "Chrome'):
        hip_profiles.browser_field().send_keys('Chrome')
    hip_profiles.save_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый HIP-профиль"'):
        hip_profiles.fast_search().send_keys('Новый HIP-профиль')
    with allure.step('Проверка создания нового объекта через основной фрейм'):
        assert hip_profiles.get_name_object() == 'Новый HIP-профиль'


@allure.feature('Объекты')
@allure.story('HIP-профили')
@allure.title('Изменение имени HIP-профиля')
def test_edit_name_object(driver):
    login(driver)
    hip_profiles = Hipprofiles(driver)
    hip_profiles.object_button().click()
    hip_profiles.hip_profiles_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый HIP-профиль"'):
        hip_profiles.fast_search().send_keys('Новый HIP-профиль')
    time.sleep(0.5)
    hip_profiles.get_author()
    time.sleep(1)
    hip_profiles.open_object().click()
    hip_profiles.pencil_edit_icon().click()
    with allure.step('Ввести новое имя объекта "selenium_test_edit_hipprofile_name"'):
        hip_profiles.edit_name_object().send_keys('selenium_test_edit_hipprofile_name')
    hip_profiles.save_button().click()
    with allure.step('Очистить строку быстрого поиска'):
        hip_profiles.fast_search().clear()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_hipprofile_name"'):
        hip_profiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    with allure.step('Проверка изменения имени объекта на новое'):
        assert hip_profiles.get_name_object() == 'selenium_test_edit_hipprofile_name'


@allure.feature('Объекты')
@allure.story('HIP-профили')
@allure.title('Изменение поля "Описание"')
def test_change_description(driver):
    login(driver)
    hip_profiles = Hipprofiles(driver)
    hip_profiles.object_button().click()
    hip_profiles.hip_profiles_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_hipprofile_name"'):
        hip_profiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hip_profiles.get_author()
    time.sleep(1)
    hip_profiles.open_object().click()
    with allure.step('Ввести описание объекта "selenium_test_edit_hipprofile_description"'):
        hip_profiles.description_field().send_keys('selenium_test_edit_hipprofile_description')
    hip_profiles.save_button().click()
    hip_profiles.statistics().click()
    hip_profiles.last_change().click()
    with allure.step('Проверка добавления описания объекта'):
        assert hip_profiles.get_description() == 'selenium_test_edit_hipprofile_description'


@allure.feature('Объекты')
@allure.story('HIP-профили')
@allure.title('Валидация полей "ОС" и "Браузер"')
def test_validation_fields(driver):
    login(driver)
    hip_profiles = Hipprofiles(driver)
    hip_profiles.object_button().click()
    hip_profiles.hip_profiles_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_hipprofile_name"'):
        hip_profiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hip_profiles.get_author()
    time.sleep(1)
    hip_profiles.open_object().click()
    with allure.step('Очистить поле ОС'):
        hip_profiles.os_field().clear()
    hip_profiles.save_button().click()
    with allure.step('Проверка валидации пустого значения в поле "ОС"'):
        assert hip_profiles.get_validation_os() == 'ОС - обязательно для заполнения'
    hip_profiles.close_err_window().click()
    with allure.step('В поле ОС ввести значение "Windows'):
        hip_profiles.os_field().send_keys('Windows')
    with allure.step('Очистить поле Браузер'):
        hip_profiles.browser_field().clear()
    hip_profiles.save_button().click()
    with allure.step('Проверка валидации пустого значения в поле "Браузер"'):
        assert hip_profiles.get_validation_browser() == 'Браузер - обязательно для заполнения'
    hip_profiles.close_err_window().click()
    with allure.step('Очистить поле ОС'):
        hip_profiles.os_field().clear()
    hip_profiles.save_button().click()
    with allure.step('Проверка одновременной валидации пустого значения в полях "ОС" и "Браузер"'):
        assert hip_profiles.get_validation_os() == 'ОС - обязательно для заполнения' and hip_profiles.get_validation_browser() == 'Браузер - обязательно для заполнения'


@allure.feature('Объекты')
@allure.story('HIP-профили')
@allure.title('Удаление объекта HIP-профиль')
def test_delete_object(driver):
    login(driver)
    hip_profiles = Hipprofiles(driver)
    hip_profiles.object_button().click()
    hip_profiles.hip_profiles_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_hipprofile_name"'):
        hip_profiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hip_profiles.get_author()
    time.sleep(1)
    hip_profiles.open_object().click()
    hip_profiles.delete_object().click()
    hip_profiles.accept_delete_object().click()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert hip_profiles.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'