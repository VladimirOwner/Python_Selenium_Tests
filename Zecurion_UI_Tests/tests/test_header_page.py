import allure
from pages.login_page import LoginPage
from pages.header_page import HeaderPage

@allure.feature('Функционал кнопок в хедере')
@allure.title('Нажатие кнопки "Супер меню"')
def test_super_menu_open(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.login()
    header_page.click_super_menu_button()
    with allure.step('Проверка открытия \'Супер меню\''):
        assert header_page.get_count_sections_in_super_menu() == 7

@allure.feature('Функционал кнопок в хедере')
@allure.title('Нажатие кнопки "Уведомления"')
def test_notification_open(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.login()
    header_page.click_notification_button()
    with allure.step('Проверка открытия модального окна \'Уведомления\''):
        assert header_page.get_text_notification() == "УВЕДОМЛЕНИЯ"

@allure.feature('Функционал кнопок в хедере')
@allure.title('Нажатие кнопки "Изменения"')
def test_changes_open(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.login()
    header_page.click_on_changes_button()
    with allure.step('Проверка открытия модального окна \'Изменения\''):
        assert header_page.get_text_changes() == "Изменения"

@allure.feature('Функционал кнопок в хедере')
@allure.title('Нажатие кнопки полноэкранного режима')
def test_full_display_open(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.login()
    header_page.click_on_full_display_button()
    with allure.step('Проверка открытия полноэкранного режима'):
        assert header_page.get_display_attribute() == "b-fs-button__icon fas fa-compress"

@allure.feature('Функционал кнопок в хедере')
@allure.title('Нажатие кнопки выхода из портала')
def test_exit(driver):
    login_page = LoginPage(driver)
    header_page = HeaderPage(driver)
    login_page.login()
    header_page.click_on_exit()
    with allure.step('Проверка выхода пользователя из портала'):
        assert login_page.get_empty_user_field_text() or login_page.get_empty_password_field_text() == "обязательно для заполнения"