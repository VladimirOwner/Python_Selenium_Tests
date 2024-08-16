from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import allure


class IpAddress(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    IP_ADDRESS_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'IP-адреса\']')
    ADD_NEW_IP = ('xpath', '//div/div/div/button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SAVE_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@type=\'button\']/span[text()=\' Сохранить \']')
    INPUT_FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    AUTHOR_OF_CHANGE = ('xpath', '//div[@class=\'ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height\'][text()=\'Администратор\']')
    IP_NAME = ('xpath', '//span/span[@class="truncate-block__name"]')
    INPUT_IP = ('xpath', '//input[@placeholder="Введите IP-адрес, маску или диапазон"]')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    INPUT_EDIT_NAME = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    CLEAR_SEARCH = ('xpath', '//span[@class=\'b-fast-search__remove z-font z-font-delete\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder="Введите описание"]')
    GET_DESCRIPTION = ('xpath', '//span[text()=\'selenium_test_edit_description\']')
    RIGHT_FRAME_STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    IP_FIELD = ('xpath', '//input[@placeholder=\'Введите IP-адрес, маску или диапазон\']')
    GET_IP = ('xpath', '//div[@class=\'b-change-modal__item\']//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_ERR_EMPTY_IP = ('xpath', '//div[@class=\'b-modal__notice-info\']//span')
    ADD_NEW_IP_FIELD = ('xpath', '//div[@class=\'b-badge-list m-t-40 m-b-5 b-badge-list_uppercase\']/div//button')
    DELETE_OBJECT = ('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i')
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    SECOND_IP_FIELD = ('xpath', '//div[@class=\'b-objects-detail-clientsip h-100\']/div[2]/div[2]//input')
    IP_CLEAR_BUTTON = ('xpath', '//button[@class=\'btn pointer btn-no-variant b-button btn-addon\']/i[1]')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def ip_address_button(self):
        with allure.step('В левом фрейме нажать на раздел "HIP-профили"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.IP_ADDRESS_BUTTON))

    def add_new_ip_address(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_IP))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def input_fast_search(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_FAST_SEARCH))

    def get_author(self):
        with allure.step('(Заглушка) Получение имени автора изменения'):
            return self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.AUTHOR_OF_CHANGE))

    def get_name_of_ip_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.IP_NAME))
        return text.text

    def input_ip(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_IP))

    def pencil_edit_icon(self):
        with allure.step('Нажать на иконку редактирования имени объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def open_object(self):
        with allure.step('Открываем выбранный объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.IP_NAME))

    def input_edit_name(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_EDIT_NAME))

    def input_description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        with allure.step('Открыть вкладку Статистика'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.RIGHT_FRAME_STATISTICS))

    def last_change(self):
        with allure.step('Открыть последнее изменение объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def input_ip_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.IP_FIELD))

    def get_ip(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_IP))
        return text.text

    def get_error_empty_ip(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_ERR_EMPTY_IP))
        return text.text

    def add_new_ip_field(self):
        with allure.step('Добавить новое поле "IP-адрес"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_IP_FIELD)).click()

    def delete_object(self):
        with allure.step('Нажать на иконку "Удаление объекта"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_OBJECT)).click()

    def accept_delete_object(self):
        with allure.step('Нажать на кнопку подтверждения "Удаления объекта"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT)).click()

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text

    def input_second_ip(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SECOND_IP_FIELD))

    def ip_clear_button(self):
        with allure.step('Очистить поле "IP-адрес"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.IP_CLEAR_BUTTON))
