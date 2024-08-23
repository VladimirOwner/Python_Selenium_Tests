from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import datetime
import allure


class MimeType(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    MIME_TYPE_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Mime-типы\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    FILTER_HEADER = ('xpath', '//span[text()=\'Автор изменения\']/../../span')
    AUTHOR_CHANCHED = ('xpath', '//label[@class=\'c-checkbox-icon c-checkbox-icon_type-1\']/span[text()=\'Администратор\']')
    CHECK_FILTER = ('xpath', '//button/i[@class=\'button-before-icon fas fa-check\']')
    LIST_OBJECT_DB = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//div[@col-id=\'description\']')
    GET_NAME_OBJECT = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    TEGS_PLUS_BUTTON = ('xpath', '//div[text()=\' Теги \']/..//button')
    TEG_IN_MODAL = ('xpath', '//footer[@class=\'modal-footer\']/..//div[@class=\'ag-center-cols-container\']/div[last()]')
    APPLY_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary\']')
    GET_TEG_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//div[@col-id=\'tags\']')
    HISTORY_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[3]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    DELETE_TAG = ('xpath', '//i[@class=\'b-tag__delete z-font z-font-delete\']')
    TEXT_NONE_TAG = ('xpath', '//span[@class=\'description d-block\']')
    HISTORY_TEG_TEXT = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[4]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INPUT_MIME_TYPE = ('xpath', '//input[@placeholder=\'Введите mime-тип\']')
    HISTORY_MIME_TYPE = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    ERROR_TEXT_MODAL = ('xpath', '//div[@class=\'mb-0\']/span')
    NAME_TAG_IN_MODAL = ('xpath', '//footer[@class=\'modal-footer\']/..//div[@class=\'ag-center-cols-container\']/div[last()]/div[@col-id=\'name\']')

    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_mime_button(self):
        with allure.step('В левом фрейме нажать на раздел "География"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.MIME_TYPE_BUTTON)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def get_description_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text

    def click_on_pencil_button(self):
        with allure.step('Нажать на кнопку редактирование "Карандаш"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def click_on_statistic_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Cтатистика"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def click_on_history_button(self):
        with allure.step('Нажать на кнопку "дата" под строкой "История изменений"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def input_mime_type(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_MIME_TYPE))

    def choose_object_in_main_frame(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT_DB))
        return list[-1]

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def input_description(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def click_on_cancel_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Отменить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CANCEL_BUTTON)).click()

    def click_on_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete_button(self):
        with allure.step('В модальном окне нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def click_on_confirm_cancel_button(self):
        with allure.step('В модальном окне нажать на кнопку "Отменить изменения"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIRM_CANCEL_BUTTON)).click()

    def get_count_object(self):
        count = len(self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT_DB)))
        return count

    def click_filter_header(self):
        with allure.step('В основном фрейме в столбце "Автор изменения" нажать на "Фильтр"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.FILTER_HEADER)).click()
    def click_checkbox_authtor(self):
        with allure.step('В открывшемся окне выбрать чек бокс "Администратор"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.AUTHOR_CHANCHED)).click()

    def click_on_check_filter(self):
        with allure.step('Нажать на кнопку применения фильтра'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECK_FILTER)).click()

    def get_history_mime_type(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_MIME_TYPE))
        return text.text

    def get_history_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_DESCRIPTION))
        return text.text

    def get_history_tag(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_TEG_TEXT))
        return text.text

    def click_on_tegs_plus_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.TEGS_PLUS_BUTTON)).click()

    def choose_teg_in_modal(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.TEG_IN_MODAL)).click()

    def click_on_apply_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.APPLY_BUTTON)).click()

    def get_tag_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_TEG_ON_MAIN_FRAME))
        return text.text

    def get_error_text_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.ERROR_TEXT_MODAL))
        return text.text

    def get_text_none_tag(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.TEXT_NONE_TAG))
        return text.text

    def click_on_delete_tag(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_TAG)).click()

    def get_text_information(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text

    def get_name_tag_in_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.NAME_TAG_IN_MODAL))
        return text.text