from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import datetime
import allure


class Adblock(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    ADBLOCK_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'AdBlock\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
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
    ACTIVE_DROP_DOWN_BUTTON = ('xpath', '//button[@class=\'btn z-dropdown btn-no-variant b-button btn-link c-select__button\']//span')
    LIST_ACTIVITY = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div')
    HISTORY_ACTIVITY = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    CHECKBOX_BLOCK_TRAFFIC = ('xpath', '//i[@class=\'c-checkbox-icon__checkbox far fa-check-square\']')
    HISTORY_BLOCK_TRAFFIC = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INPUT_SITES_BLOCK = ('xpath', '//div[@class=\'b-objects-detail-adblock h-100\']//div[@class=\'input-group\'][last()]//input[@placeholder]')
    ERROR_TEXT_MODAL = ('xpath', '//div[@class=\'mb-0\']/span')
    SUCSSES_ICON = ('xpath', '//i[@class=\'fa fa-check success\']')
    ERROR_ICON = ('xpath', '//i[@class=\'fas fa-exclamation-triangle error-icon\']')
    SITES_PLUS_BUTTON = ('xpath', '//div[text()=\' Справочники сайтов AdBlock \']/..//button')
    LIST_INPUT_SITES = ('xpath', '//div[@class=\'b-objects-detail-adblock h-100\']//div[@class=\'input-group\']')
    DELETE_INPUT_SITES_BUTTON = ('xpath', '//div[@class=\'b-objects-detail-adblock h-100\']//div[@class=\'input-group\'][last()]//button')
    TEGS_PLUS_BUTTON = ('xpath', '//div[text()=\' Теги \']/..//button')
    TEG_IN_MODAL = ('xpath', '//footer[@class=\'modal-footer\']/..//div[@class=\'ag-center-cols-container\']/div[last()]')
    APPLY_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary\']')
    GET_TEG_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//div[@col-id=\'tags\']')
    HISTORY_TEG_TEXT = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[5]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    VALUE_ACTIVITY = ('xpath', '//span[@class=\'c-select__wrapper--text text-truncate\']')
    HISTORY_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[3]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[4]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    DELETE_TAG = ('xpath', '//i[@class=\'b-tag__delete z-font z-font-delete\']')
    TEXT_NONE_TAG = ('xpath', '//span[@class=\'description d-block\']')










    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_adblock_button(self):
        with allure.step('В левом фрейме нажать на раздел "География"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ADBLOCK_BUTTON)).click()

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

    def get_text_information(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text

    def choose_list_activity(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_ACTIVITY))
        return list[-1]

    def click_on_active_drop_down(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVE_DROP_DOWN_BUTTON)).click()

    def get_history_activity(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_ACTIVITY))
        return text.text

    def click_checkbox_block_traffic(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_BLOCK_TRAFFIC)).click()

    def get_history_block_traffic(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_BLOCK_TRAFFIC))
        return text.text

    def input_sites_block(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_SITES_BLOCK))

    def get_error_text_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.ERROR_TEXT_MODAL))
        return text.text

    def get_sucsses_icon(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SUCSSES_ICON))

    def get_error_icon(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ERROR_ICON))

    def click_on_plus_sites(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.SITES_PLUS_BUTTON)).click()

    def count_input_sites(self):
        count = len(self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_INPUT_SITES)))
        return count

    def click_on_delete_input_site(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_INPUT_SITES_BUTTON)).click()

    def choose_teg_in_modal(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.TEG_IN_MODAL)).click()

    def click_on_apply_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.APPLY_BUTTON)).click()

    def click_on_tegs_plus_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.TEGS_PLUS_BUTTON)).click()

    def get_tag_on_main_frame(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_TEG_ON_MAIN_FRAME))
        return text.text

    def get_history_teg(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_TEG_TEXT))
        return text.text

    def get_value_activity(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.VALUE_ACTIVITY))
        return text.text

    def get_history_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_DESCRIPTION))
        return text.text

    def click_on_delete_tag(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_TAG)).click()

    def get_text_none_tag(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.TEXT_NONE_TAG))
        return text.text

