from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import allure


class Tegs(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//span[text()=\'Объекты\']')
    TEGS_BUTTON = ('xpath', '//span[text()=\'Теги\']/../..//span[@class="d-inline-block text-start"]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    GET_OBJECT = ('xpath', '//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    LIST_OBJECT_APP = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[@role=\'row\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']//div[@col-id=\'description\']')
    COLOR_DROPDOWN = ('xpath', '//div[@class=\'c-select__wrapper\']//span[@class=\'c-select__color\']')
    NEW_COLOR = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[4]')
    CHECKBOX = ('xpath', '//span[text()=\'Отображать название\']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    INFORMATION_MESSAGE = ('xpath', '//*[@id="z-main-content"]/div[1]/div/div[3]/main/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/div/div/div/span')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    HISTORY_CHANGING_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def tegs_button(self):
        with allure.step('Нажать "Теги" в левом фрейме'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.TEGS_BUTTON))

    def add_new_object(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def get_object(self):
        with allure.step('Выбрать объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.LIST_OBJECT_APP))

    def click_on_pencil_button(self):
        with allure.step('Нажать на кнопку редактирование "Карандаш"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_OBJECT))
        return text.text

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTOIN_FIELD))

    def get_description_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text

    def color_dropdown(self):
        with allure.step('В правом фрейме нажать на Dropdown цвета '):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.COLOR_DROPDOWN))

    def select_new_color(self):
        with allure.step('Выбрать новый цвет в правом фрейме'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.NEW_COLOR))

    def unselect_checkbox(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX))

    def click_on_statistic_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Cтатистика"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def click_on_history_button(self):
        with allure.step('Нажать на кнопку "дата" под строкой "История изменений"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def get_history_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_CHANGING_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_CHANGING_DESCRIPTION))
        return text.text

    def click_on_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete_button(self):
        with allure.step('В модальном окне нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def get_text_information(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text

    def click_on_cancel_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Отменить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CANCEL_BUTTON)).click()

    def click_on_confirm_cancel_button(self):
        with allure.step('В модальном окне нажать на кнопку "Отменить изменения"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIRM_CANCEL_BUTTON)).click()
