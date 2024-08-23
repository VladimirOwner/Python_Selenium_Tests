from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import allure


class SslInspec(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//span[text()=\'Объекты\']')
    SSL_INSPEC_BUTTON = ('xpath', '/html/body/div[1]/div/div[3]/main/div/div/div[2]/div/div[1]/div/div/div[1]/div[30]/div/span/span[1]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    GET_OBJECT = ('xpath', '//span[text()=" Новая SSL-инспекция "]')
    GET_NEW_OBJECT = ('xpath', '//span[text()=" 123 "]')
    LIST_OBJECT_APP = ('xpath', '//div[@class="ag-center-cols-container"]/div/div/span/span[text()]')
    GENERATE_SSL = ('xpath', '//span[text()=\' Сгенерировать \']')
    INPUT_SSL_NAME = ('xpath', '//input[@placeholder=\'Введите имя сертификата\']')
    GENERATE_BUTTON = ('xpath', '//div[@class=\'modal-content\']/footer[@class]/div[@class]/button')
    CLOSE_MODAL = ('xpath', '//div[@class=\'modal-content\']/footer[@class]/div[@class]/button/span[text()=" Закрыть "]')
    DOWNLOAD_SSL = ('xpath', '//div[@class="tab-content"]/div/div/div/div[5]/div/div/button')
    DOWNLOAD_KEY = ('xpath', '//div[@class="b-manage-certificate__item b-frame-detail__item"]/span[2]/button')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class="ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height ag-cell-focus"]')
    GET_DROPDOWN_ON_MAIN_FRAME = ('xpath', '//span[text()="ГОСТ"]')
    DROPDOWN_BUTTON = ('xpath', '//div[@class="c-dropdown-new c-select__dropdown"]')
    DROPDOWN_SELECT = ('xpath', '//div[@class="c-select__wrapper c-dropdown-new__item text-truncate"]/span')
    SELECT_CHECKBOX1 = ('xpath', '//div[@class=\'b-objects-detail-sslinspection h-100\']/label[1]/i')
    SELECT_CHECKBOX2 = ('xpath', '//div[@class=\'b-objects-detail-sslinspection h-100\']/label[2]/i')
    ACTIVITY_DROPDOWN = ('xpath', '//div[@class="c-select__wrapper text-truncate"]/span[text()=" Включено "]')
    ACTIVITY_SELECT = ('xpath', '//div[@class="c-dropdown-new__list"]/div[2]')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    HISTORY_CHANGING_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[5]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[6]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    INFORMATION_MESSAGE = ('xpath', '//div[@class=\'b-frame-main__container b-frame-main__container_empty\']//span[text()]')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    ADD_TEG = ('xpath', '//div[@class="b-badge-list__header"]/button')
    SELECT_TEG = ('xpath', '//div[@class="modal-content"]/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[3]/div/div/div[2]/div/div/div')
    GET_TEG_NAME = ('xpath', '//footer[@class="modal-footer"]/..//div[@class="ag-center-cols-container"]/div[last()]/div[@col-id="name"]/span')
    ACCEPT_TEG = ('xpath', '//button[@class="btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary"]/span[text()]')
    DEL_TEG = ('xpath', '//div[@class="b-tags__items"]/span/i')
    TEG_INFO = ('xpath', '//span[@class="b-tag"]/b/span')
    TEG_INFO_DEL = ('xpath', '//div[@class="b-badge-list b-badge-list_flex"]/span[text()=" Не установлено "]')
    GET_INFO_DEL = ('xpath', '//*[@id="z-main-content"]/div[1]/div/div[3]/main/div/div/div[2]/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[7]/div/div/div/span')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def ssl_button(self):
        with allure.step('Нажать "SSL-инспекция" в левом фрейме'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SSL_INSPEC_BUTTON))

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

    def generate_ssl(self):
        with allure.step('Открыть модальное окно генерации'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.GENERATE_SSL))

    def input_ssl_name(self):
        with allure.step('Ввести имя сертификата'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_SSL_NAME))

    def generate_button(self):
        with allure.step('Сгенерировать серитификат'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.GENERATE_BUTTON))

    def close_modal(self):
        with allure.step('Сгенерировать серитификат'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.CLOSE_MODAL))

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

    def get_dropdown_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DROPDOWN_ON_MAIN_FRAME))
        return text.text

    def open_dropdown(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_BUTTON))

    def select_dropdown(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_SELECT))

    def select_checkbox1(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_CHECKBOX1))

    def select_checkbox2(self):
        with allure.step('В правом фрейме unselect checbox'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SELECT_CHECKBOX2))

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

    def download_certif(self):
        with allure.step('Скачать серитификат'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.DOWNLOAD_SSL))

    def download_key(self):
        with allure.step('Скачать ключ'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.DOWNLOAD_KEY))

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

    def get_teg_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_TEG_NAME))
        return text.text
