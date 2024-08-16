from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import allure

class Hipprofiles(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    HIP_PROFILES_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'HIP-профили\']')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    OS_FIELD = ('xpath', '//input[@placeholder="Введите ос"]')
    BROWSER_FIELD = ('xpath', '//input[@placeholder="Введите браузер"]')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'text-highlight\']')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    EDIT_NAME_OBJECT = ('xpath', '//input[@placeholder=\'Введите имя\']')
    AUTHOR_OF_CHANGE = ('xpath', '//div[@class=\'ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height\'][text()=\'Администратор\']')
    LIST_OBJECTS_IN_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    DESCRIPTION_FIELD = ('xpath', '//input[@validatefieldname=\'Описание\']')
    RIGHT_FRAME_STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    GET_DESCRIPTION = ('xpath', '//span[text()=\'selenium_test_edit_hipprofile_description\']')  #поменять поиск элемента, не привязывать к какому-то значению
    VALIDATION_ERR_OS = ('xpath', '//span[text()="ОС - обязательно для заполнения"]')
    VALIDATION_ERR_BROWSER = ('xpath', '//span[text()="Браузер - обязательно для заполнения"]')
    CLOSE_ERR_WINDOW = ('xpath', '//span[text()=" Закрыть "]')
    DELETE_OBJECT = (('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i'))
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON))

    def hip_profiles_button(self):
        with allure.step('В левом фрейме нажать на раздел "HIP-профили"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.HIP_PROFILES_BUTTON))

    def add_new_object(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def os_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.OS_FIELD))

    def browser_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.BROWSER_FIELD))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON))

    def fast_search(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.FAST_SEARCH))

    def get_name_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def open_object(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))

    def pencil_edit_icon(self):
        with allure.step('Нажать на иконку редактирования имени объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def edit_name_object(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.EDIT_NAME_OBJECT))

    def get_author(self):
        with allure.step('(Заглушка) Получение имени автора изменения'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.AUTHOR_OF_CHANGE))
    def get_object(self):
        list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECTS_IN_MAIN_FRAME))
        return list[-1]

    def description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        with allure.step('Открыть вкладку Статистика'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.RIGHT_FRAME_STATISTICS))

    def last_change(self):
        with allure.step('Открыть последнее изменение объекта'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def get_validation_os(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.VALIDATION_ERR_OS))
        return text.text

    def get_validation_browser(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.VALIDATION_ERR_BROWSER))
        return text.text

    def close_err_window(self):
        with allure.step('Закрыть модальное окно ошибки'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.CLOSE_ERR_WINDOW))

    def delete_object(self):
        with allure.step('Нажать на иконку "Удаление объекта"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_OBJECT))

    def accept_delete_object(self):
        with allure.step('Нажать на кнопку подтверждения "Удаления объекта"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT))

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text