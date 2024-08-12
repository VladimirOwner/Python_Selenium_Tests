import time

from pages.login_page import LoginPage
from pages.Objects.hip_profiles import Hipprofiles

def test_create_object(driver):
    login_page = LoginPage(driver)
    hipprofiles = Hipprofiles(driver)
    login_page.login()
    hipprofiles.object_button().click()
    hipprofiles.hip_profiles_button().click()
    hipprofiles.add_new_object().click()
    hipprofiles.os_field().send_keys('Windows')
    hipprofiles.browser_field().send_keys('Chrome')
    hipprofiles.save_button().click()
    hipprofiles.fast_search().send_keys('Новый HIP-профиль')
    assert hipprofiles.get_name_object() == 'Новый HIP-профиль'

def test_edit_name_object(driver):
    login_page = LoginPage(driver)
    hipprofiles = Hipprofiles(driver)
    login_page.login()
    hipprofiles.object_button().click()
    hipprofiles.hip_profiles_button().click()
    hipprofiles.fast_search().send_keys('Новый HIP-профиль')
    time.sleep(0.5)
    hipprofiles.get_author()
    time.sleep(1)
    hipprofiles.open_object().click()
    hipprofiles.pencil_edit_icon().click()
    hipprofiles.edit_name_object().send_keys('selenium_test_edit_hipprofile_name')
    hipprofiles.save_button().click()
    hipprofiles.fast_search().clear()
    hipprofiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    assert hipprofiles.get_name_object() == 'selenium_test_edit_hipprofile_name'

def test_change_description(driver):
    login_page = LoginPage(driver)
    hipprofiles = Hipprofiles(driver)
    login_page.login()
    hipprofiles.object_button().click()
    hipprofiles.hip_profiles_button().click()
    hipprofiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hipprofiles.get_author()
    time.sleep(1)
    hipprofiles.open_object().click()
    hipprofiles.description_field().send_keys('selenium_test_edit_hipprofile_description')
    hipprofiles.save_button().click()
    hipprofiles.statistics().click()
    hipprofiles.last_change().click()
    assert hipprofiles.get_description() == 'selenium_test_edit_hipprofile_description'

def test_validation_fields(driver):
    login_page = LoginPage(driver)
    hipprofiles = Hipprofiles(driver)
    login_page.login()
    hipprofiles.object_button().click()
    hipprofiles.hip_profiles_button().click()
    hipprofiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hipprofiles.get_author()
    time.sleep(1)
    hipprofiles.open_object().click()
    hipprofiles.os_field().clear()
    hipprofiles.save_button().click()
    assert hipprofiles.get_validation_os() == 'ОС - обязательно для заполнения'
    hipprofiles.close_err_window().click()
    hipprofiles.os_field().send_keys('Windows')
    hipprofiles.browser_field().clear()
    hipprofiles.save_button().click()
    assert hipprofiles.get_validation_browser() == 'Браузер - обязательно для заполнения'
    hipprofiles.close_err_window().click()
    hipprofiles.os_field().clear()
    assert hipprofiles.get_validation_os() == 'ОС - обязательно для заполнения' and hipprofiles.get_validation_browser() == 'Браузер - обязательно для заполнения'

def delete_object(driver):
    login_page = LoginPage(driver)
    hipprofiles = Hipprofiles(driver)
    login_page.login()
    hipprofiles.object_button().click()
    hipprofiles.hip_profiles_button().click()
    hipprofiles.fast_search().send_keys('selenium_test_edit_hipprofile_name')
    time.sleep(0.5)
    hipprofiles.get_author()
    time.sleep(1)
    hipprofiles.open_object().click()
    hipprofiles.delete_object().click()
    hipprofiles.accept_delete_object().click()
    assert hipprofiles.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'