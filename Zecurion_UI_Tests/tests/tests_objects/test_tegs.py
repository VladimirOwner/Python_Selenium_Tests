from pages.login_page import LoginPage
from pages.Objects.tegs import Tegs
import allure


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Создание объекта')
def test_create_teg(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.add_new_object().click()
    app_page.save_button().click()
    with allure.step('Проверка создания объекта'):
        assert app_page.get_name_object() == 'Новый тег'


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Изменение объекта')
def test_change_name_object(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.get_object().click()
    app_page.click_on_pencil_button()
    with allure.step('Изменить название тега, например "123"'):
        app_page.input_pencil().send_keys('123')
    app_page.save_button().click()
    with allure.step('Проверка изменения названия на новое'):
        assert app_page.get_name_object() == '123'
    with allure.step('В поле описание ввести "Telegram"'):
        app_page.description_field().send_keys('Telegram')
        app_page.save_button().click()
    with allure.step('Проверка добавления описания в объект'):
        assert app_page.get_description_on_main_frame() == 'Telegram'
    with allure.step('Unselect checkbox'):
        app_page.unselect_checkbox().click()
        app_page.save_button().click()


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Изменение цвета')
def test_change_color_object(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.get_object().click()
    with allure.step('Изменение цвета но новый'):
        app_page.color_dropdown().click()
        app_page.select_new_color().click()
        app_page.save_button().click()


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Отмена изменений')
def test_cancel_change(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.get_object().click()
    description = app_page.description_field().get_attribute('value')
    with allure.step('Очистить поле "Описание"'):
        app_page.description_field().clear()
    app_page.click_on_cancel_button()
    app_page.click_on_confirm_cancel_button()
    with allure.step('Проверка отмены изменений'):
        assert app_page.get_description_on_main_frame() == description


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Проверка записи в "Истории изменений"')
def test_history_button(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.get_object().click()
    name = app_page.get_name_object()
    description = app_page.get_description_on_main_frame()
    app_page.click_on_statistic_button()
    app_page.click_on_history_button()
    with allure.step('Проверка правильности записи данных в историю изменений'):
        assert app_page.get_history_name() == name and app_page.get_history_description() == description


@allure.feature("Объекты")
@allure.story("Теги")
@allure.title('Удаление объекта')
def test_delete_teg(driver):
    login(driver)
    app_page = Tegs(driver)
    app_page.object_button().click()
    app_page.tegs_button().click()
    app_page.get_object().click()
    app_page.click_on_delete_button()
    app_page.click_on_confirm_delete_button()
    with allure.step('Проверка удаления объекта'):
        assert app_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
