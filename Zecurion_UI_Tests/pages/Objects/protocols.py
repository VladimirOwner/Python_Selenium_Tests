from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure


class Protocols(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    PROTOCOL_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Протоколы\']')
    ADD_NEW_PROTOCOL = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@type=\'button\']/span[text()=\' Сохранить \']')
    INPUT_FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    AUTHOR_OF_CHANGE = ('xpath', '//div[@class=\'ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height\'][text()=\'Администратор\']')
    NAME_PROTOCOL = ('xpath', '//span[@class=\'text-highlight\']')
    DELETE_PROTOCOL = ('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i')
    ACCEPT_DELETE_PROTOCOL = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    INPUT_EDIT_NAME = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    CLEAR_SEARCH = ('xpath', '//span[@class=\'b-fast-search__remove z-font z-font-delete\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@validatefieldname=\'Описание\']')
    GET_DESCRIPTION = ('xpath', '//span[text()=\'selenium_test\']')
    RIGHT_FRAME_STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    DPI_PROTOCOL = ('xpath', '//button[@class=\'btn b-frame-detail__item-btn btn-no-variant b-button btn-no-variant\']')
    CHECKBOX_MEDIA_DPI = ('xpath', '//p[text()=\' Media \']/../../i')
    SAVE_DPI = ('xpath', '//footer//span[@class=\'text-truncate\'][text()=\' Сохранить \']')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON))

    def protocol_button(self):
        with allure.step('В левом фрейме нажать на раздел "Протоколы"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.PROTOCOL_BUTTON))

    def add_new_protocol(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_NEW_PROTOCOL))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON))

    def input_fast_search(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_FAST_SEARCH))

    def get_author(self):
        with allure.step('(Заглушка) Получение имени автора изменения'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.AUTHOR_OF_CHANGE))

    def get_name_protocol(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.NAME_PROTOCOL))
        return text.text

    def name_protocol(self):
        with allure.step('Открываем выбранный объект'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.NAME_PROTOCOL))

    def delete_object(self):
        with allure.step('Нажать на иконку "Удаление объекта"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_PROTOCOL))

    def accept_delete_object(self):
        with allure.step('Нажать на кнопку подтверждения "Удаления объекта"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.ACCEPT_DELETE_PROTOCOL))

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text

    def pencil_edit_icon(self):
        with allure.step('Нажать на иконку редактирования имени объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def input_edit_name(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_EDIT_NAME))

    def input_description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def get_description(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def statistics(self):
        with allure.step('Открыть вкладку Статистика'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.RIGHT_FRAME_STATISTICS))

    def last_change(self):
        with allure.step('Открыть последнее изменение объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.LAST_CHANGE))

    def dpi_protocol_field(self):
        with allure.step('Нажать на поле DPI-протоколы для открытия модального окна выбора'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DPI_PROTOCOL))

    def checkbox_media(self):
        with allure.step('Нажать на чек бокс "Media"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECKBOX_MEDIA_DPI))

    def get_dpi_protocol(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.DPI_PROTOCOL))
        return text.text

    def save_dpi_modal(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_DPI))
