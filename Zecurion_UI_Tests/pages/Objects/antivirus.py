from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec

import allure


class Antivirus(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//span[text()=\'Объекты\']')
    ANTIVIRUS_BUTTON = ('xpath', '//span[@class="b-left-frame-tree__title-name b-left-frame-tree__title-name_single"]//span[text()="Антивирус"]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    EDIT_NAME_OBJECT = ('xpath', '//input[@placeholder=\'Введите имя\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    LIST_OBJECT = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    GET_NAME_OBJECT = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder="Введите описание"]')
    STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    BASICS = ('xpath', '//a[text()=\'Основное\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    GET_DESCRIPTION = ('xpath', '//div[@class="b-change-modal__content b-change-modal__content_one-block"]/div[5]//div[@class="b-change-modal__item--value text-truncate"]')
    CONFIDENCE_FIELD = ('xpath', '//input[@placeholder="Уверенность"]')
    GET_SAVE_ERR = ('xpath', '//div[@class="modal-body"]//span')
    CLOSE_MODAL_WINDOW = ('xpath', '//div[@class="modal-footer-wrap_flex m-0 w-100"]//button')
    ADD_TEG_BUTTON = ('xpath', '//div[@class="b-tags"]//button')
    LIST_TAGS = ('xpath', '//div[@class="modal-body"]//div[@class="ag-center-cols-container"]/div')
    APPLY_TAGS_BUTTON = ('xpath', '//button[@class="btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary"]/span[text()]')
    GET_TAGS = ('xpath', '//div[@class="b-change-modal__content b-change-modal__content_one-block"]/div[6]//div[@class="b-change-modal__item--value text-truncate"]')
    ACTIVITY_DROPDOWN = ('xpath', '//div[@class="b-objects-detail-antivirus h-100"]/div[@class="row c-select"][2]//button')
    ACTIVITY_ON = ('xpath', '//div[@class="c-dropdown-new__list"]/div[1]')
    ACTIVITY_OFF = ('xpath', '//div[@class="c-dropdown-new__list"]/div[2]')
    GET_ACTIVITY = ('xpath', '//div[@class="b-change-modal__content b-change-modal__content_one-block"]/div[1]//div[@class="b-change-modal__item--value text-truncate"]')
    GET_TAG_IN_MODAL = ('xpath', '//footer[@class=\'modal-footer\']/..//div[@class=\'ag-center-cols-container\']/div[last()]/div[@col-id=\'name\']')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))  # import datetime

    def antivirus_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ANTIVIRUS_BUTTON))

    def add_new_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def pencil_edit_icon(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def edit_name_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EDIT_NAME_OBJECT))

    def save_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def object(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT))
        return list[-1]

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.STATISTICS))

    def basics(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.BASICS))

    def last_change(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def open_object(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT))
        return list[-1]

    def confidence_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIDENCE_FIELD))

    def get_save_err(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_SAVE_ERR))
        return text.text

    def close_modal_window(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.CLOSE_MODAL_WINDOW))

    def add_teg_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_TEG_BUTTON))

    def tags(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_TAGS))
        return list[-1]

    def apply_tags_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.APPLY_TAGS_BUTTON))

    def get_tags(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_TAGS))
        return text.text

    def get_tag_in_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_TAG_IN_MODAL))
        return text.text

    def activity_dropdown(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVITY_DROPDOWN))

    def activity_on(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVITY_ON))

    def activity_off(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVITY_OFF))

    def get_activity(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_ACTIVITY))
        return text.text
