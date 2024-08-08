from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import datetime
import allure

class GeographyPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    GEOGRAPHY_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'География\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    ADD_REGION_BUTTON = ('xpath', '//div[text()=\' Регионы \']/..//button')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    LIST_OBJECT_GEOGRAPHY = ('xpath','//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    ADD_REGION = ('xpath', '//p[text()=\' Европа \']/../../i')
    SAVE_BUTTON_MODAL = ('xpath', '//footer[@class=\'modal-footer\']//span')
    LIST_REGIONS = ('xpath','//ul[@class=\'b-badge-list__list\']/li')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']//div[@col-id=\'description\']')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    GET_NAME_IN_HISROTY_CHANGING = ('xpath', '//span[text()=\' Название \']/..//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_DESCRIPTION_IN_HISTORY_CHANGING = ('xpath', '//span[text()=\' Описание \']/..//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    DROP_DOWN_MODAL = ('xpath', '//p[text()=\' Африка \']/../../../span')
    CHECKBOX_COUNTRY = ('xpath', '//p[text()=\' Алжир \']/../..')
    MODAL_FAST_SEARCH = ('xpath', '//div[@class=\'modal-body__inner-container\']//input[@placeholder=\'Быстрый поиск\']')
    GET_TEXT_COUNTRY = ('xpath', '//p[text()=\' Европа \']/../..')
    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_geography_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.GEOGRAPHY_BUTTON)).click()

    def click_on_add_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def click_on_add_region_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_REGION_BUTTON)).click()

    def count_geograpgy_on_main_frame(self):
        count = len(self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECT_GEOGRAPHY)))
        return count
    def choose_region(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_REGION)).click()

    def click_save_on_modal(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON_MODAL)).click()

    def count_country_on_rigth_frame(self):
        count = len(self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_REGIONS)))
        return count

    def get_name_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTOIN_FIELD))

    def get_description_on_main_frame(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text
    def click_on_cancel_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()

    def click_on_pencil_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def click_on_history_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def choose_object_in_main_frame(self):
        list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECT_GEOGRAPHY))
        return list[-1]

    def click_on_statistic_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def get_name_in_history_changing(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_IN_HISROTY_CHANGING))
        return text.text
    def get_description_on_history_changing(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION_IN_HISTORY_CHANGING))
        return text.text
    def click_on_delete_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def get_text_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text

    def click_on_checkbox_country(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECKBOX_COUNTRY)).click()

    def click_on_drop_down_modal(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.DROP_DOWN_MODAL)).click()

    def input_modal_fast_search(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.MODAL_FAST_SEARCH))
    def get_text_continent(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_TEXT_COUNTRY))
        return text.text