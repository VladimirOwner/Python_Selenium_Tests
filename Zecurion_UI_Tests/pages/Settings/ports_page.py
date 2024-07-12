from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import datetime

class PortsPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    SETTING_BUTTON = ('xpath','//section[@class=\'ps-container b-scroll-area b-super-menu__nav-container b-super-menu-favorites__list ps ps--theme_default\']/li[6]')
    PORTS = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']/span[text()=\'Порты прокси\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    ADD_PORT = ('xpath', '//div[text()=\' Порты \']/../button')
    INPUT_PORTS_FIELD = ('xpath', '//input[@placeholder=\'Введите порты\']')
    INVISIBLE_MODE_BUTTON = ('xpath', '//span[text()=\'Прозрачный режим\']/../i')
    PROTOCOL_DROPDOWN = ('xpath', '//span[text()=\'Протокол\']/../..//div[@class=\'c-dropdown-new c-select__dropdown\']')
    PROTOCOL_CHOOSE = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[1]')
    INVISIBLE_PORT_FIELD = ('xpath', '//input[@placeholder=\'Введите порт\']')
    SAVE_BUTTON = ('xpath', '//button[@class=\'btn b-button_primary btn-no-variant b-button btn-no-variant\']')
    LIST_OBJECTS_PORTS = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    STATISTIC_BUTTON = ('xpath', '//ul[@role=\'tablist\']/li[3]')
    STATISTIC_INFORMATION = ('xpath', '//div[@class=\'tab-pane active\']//div[@class=\'b-frame-detail__item\'][1]/span[@class=\'b-frame-detail__stats-value d-flex\']/span[1]')
    DISCRIPTION_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    DISCRIPTION_IN_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//div[@col-id=\'description\']')
    OBLIGATORY_TO_FILL_FIELD_PORTS = ('xpath', '//input[@placeholder=\'Введите порты\']/..//div[text()=\'обязательно для заполнения\']')
    OBLIGATORY_TO_FILL_FIELD_PORT = ('xpath','//input[@placeholder=\'Введите порт\']/..//div[text()=\'обязательно для заполнения\']')
    ERROR_MODAL_TEXT = ('xpath', '//span[text()=\'Порты - обязательно для заполнения\']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button[@class=\'btn b-modal__button b-button_primary btn-no-variant b-button btn-no-variant\']')


    def click_on_setting_button(self):
        with allure.step('Нажать на кнопку "Настройки"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SETTING_BUTTON)).click()

    def click_on_ports(self):
        with allure.step('В левом фрейме нажать на раздел "Порты прокси"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.PORTS)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_add_ports(self):
        with allure.step('Нажать на кнопку "+" - добавить порт'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_PORT)).click()

    def input_port_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PORTS_FIELD))

    def click_on_invisible_mode_checkbox(self):
        with allure.step('В правом фрейме в строке "Прозрачный режим" нажать на чек-бокс'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.INVISIBLE_MODE_BUTTON)).click()

    def click_on_protocol_dropdown(self):
        with allure.step('В строке "Протокол" нажать на список протоколов'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.PROTOCOL_DROPDOWN)).click()

    def click_choose_protocol(self):
        with allure.step('Выбрать протокол из списка (например HTTP)'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.PROTOCOL_CHOOSE)).click()

    def invisible_port_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INVISIBLE_PORT_FIELD))

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def count_objects_ports(self):
        count = len(self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECTS_PORTS)))
        return count

    def choose_object_ports(self):
        with allure.step('В основном фрейме выбрать созданный объект'):
            list_object = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECTS_PORTS))
            object_port = list_object[-1]
            object_port.click()

    def get_current_data(self):# Получение текущей даты
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date

    def click_on_statistic_information(self):
        with allure.step('В правом фрейме нажать на раздел "Статистика"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def get_statistic_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_INFORMATION))
        return text.text

    def discription_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTION_FIELD))

    def get_discription_text_in_main_frame(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTION_IN_MAIN_FRAME))
        return text.text

    def get_text_obligatory_to_fill_ports(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.OBLIGATORY_TO_FILL_FIELD_PORTS)).text
        return text

    def get_text_obligatory_to_fill_port(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.OBLIGATORY_TO_FILL_FIELD_PORT)).text
        return text

    def get_error_modal_text(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.ERROR_MODAL_TEXT)).text
        return text

    def click_on_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete_button(self):
        with allure.step('В модальном окне подтвердить удаление объекта (нажать на кнопку "Удалить")'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()