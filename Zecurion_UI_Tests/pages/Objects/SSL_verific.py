from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import allure


class SslVerific(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//span[text()=\'Объекты\']')
    SSL_VERIFIC_BUTTON = ('xpath', '/html/body/div[1]/div/div[3]/main/div/div/div[2]/div/div[1]/div/div/div[1]/div[31]/div/span/span[1]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    GET_OBJECT = ('xpath', '//span[text()=" Новая SSL-верификация "]')
    GET_NEW_OBJECT = ('xpath', '//span[text()="123"]')
    LIST_OBJECT_APP = ('xpath', '//div[@class="ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height"]/span/span')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class="ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-focus"]')
    SELECT_CHECKBOX1 = ('xpath', '//div[@class="h-100"]/label[1]/i')
    SELECT_CHECKBOX2 = ('xpath', '//div[@class="h-100"]/label[2]/i')
    SELECT_CHECKBOX3 = ('xpath', '//div[@class="h-100"]/label[3]/i')
    ACTIVITY_DROPDOWN = ('xpath', '//div[@class="c-select__wrapper text-truncate"]/span[text()=" Включено "]')
    ACTIVITY_SELECT = ('xpath', '//div[@class="c-dropdown-new__list"]/div[2]')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    HISTORY_CHANGING_NAME = ('xpath', '//div[@class="modal-body__inner-container"]/div/div[3]/div/div/div/span')
    HISTORY_CHANGING_DESCRIPTION = ('xpath', '//div[@class="modal-body__inner-container"]/div/div[4]/div/div/div/span')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    INFORMATION_MESSAGE = ('xpath', '//div[@class=\'b-frame-main__container b-frame-main__container_empty\']//span[text()]')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    ADD_TEG = ('xpath', '//div[@class="b-badge-list__header"]/button')
    SELECT_TEG = ('xpath', '//div[@class="modal-content"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div')
    ACCEPT_TEG = ('xpath', '//button[@class="btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary"]/span[text()=" Применить "]')
    DEL_TEG = ('xpath', '//div[@class="b-tags__items"]/span/i')
    TEG_INFO = ('xpath', '//div[@class="b-tags__items"]/span/b/span[text()=" Новый тег "]')
    TEG_INFO_DEL = ('xpath', '//div[@class="b-badge-list b-badge-list_flex"]/span[text()=" Не установлено "]')
    GET_INFO_DEL = ('xpath', '//*[@id="z-main-content"]/div[1]/div/div[3]/main/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/div/div/div/span')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def ssl_button(self):
        with allure.step('Нажать "SSL-верификация" в левом фрейме'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SSL_VERIFIC_BUTTON))

    def add_new_object(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_OBJECT))
        return text.text

    def get_new_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NEW_OBJECT))
        return text.text

    def select_object(self):
        with allure.step('Выбрать объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.LIST_OBJECT_APP))

    def click_on_pencil_button(self):
        with allure.step('Нажать на кнопку редактирование "Карандаш"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTOIN_FIELD))

    def get_description_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text

    def select_checkbox1(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_CHECKBOX1))

    def select_checkbox2(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_CHECKBOX2))

    def select_checkbox3(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_CHECKBOX3))

    def activity_dropdown(self):
        with allure.step('Выбрать dropdown'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVITY_DROPDOWN))

    def activity_select(self):
        with allure.step('Выбрать dropdown'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVITY_SELECT))

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

    def add_teg(self):
        with allure.step('В правом фрейме нажать на "+" в строке Теги'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_TEG)).click()

    def select_teg(self):
        with allure.step('В модальном окне выбрать тег'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_TEG)).click()

    def accept_teg(self):
        with allure.step('В модальном окне нажать на кнопку применить'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ACCEPT_TEG)).click()

    def del_teg(self):
        with allure.step('Удаление тега у объекта'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.DEL_TEG)).click()

    def get_teg_info(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.TEG_INFO))
        return text.text

    def get_teg_info_del(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.TEG_INFO_DEL))
        return text.text

    def get_info_del(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_INFO_DEL))
        return text.text
