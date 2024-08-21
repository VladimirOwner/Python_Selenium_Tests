from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import datetime
import allure

class ContentProtection(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    PROTECTION_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Защита контента\']')
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
    HISTORY_ACTIVITY = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[9]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    CHECKBOX_BLOCK_TRAFFIC = ('xpath', '//i[@class=\'c-checkbox-icon__checkbox far fa-check-square\']')
    HISTORY_BLOCK_TRAFFIC = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[10]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    MASK_PLUS_BUTTON = ('xpath', '//span[text()=\'Маски\']/..//i')
    INPUT_MASK = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']//div[@class=\'input-group\'][last()]//input[@placeholder]')
    DOWNLOAD_MASK = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']//div[@class=\'input-group\'][last()]//input[@type=\'file\']')
    GET_FILE_NAME = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']//div[@class=\'input-group\'][last()]//button/span')
    ERROR_TEXT_MODAL = ('xpath', '//div[@class=\'mb-0\']/span')
    CHECKBOX_PERSON_DATA = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[5]/label/i')
    CHECKBOX_PII = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[6]/label/i')
    CHECKBOX_PCI_DSS = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[7]/label/i')
    CHECKBOX_PHI = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[8]/label/i')
    CHECKBOX_FINANCIAL_RECORDS = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[9]/label/i')
    CHECKBOX_GDPR_RESTRICTED = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[10]/label/i')
    CHECKBOX_GDBPR = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[11]/label/i')
    CHECKBOX_GLBA = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[12]/label/i')
    CHECKBOX_HIPAA = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']/div[13]/label/i')
    HISTORY_FINANCIAL_RECORDS = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_GDBPR = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_GDPR_RESTRICTED = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[3]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_GLBA = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[4]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_HIPAA = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[5]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_PCI_DSS = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[6]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_PHI = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[7]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_PII = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[8]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_PERSON_DATA = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[14]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    CLOSE_MASK_BUTTON = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']//div[@class=\'input-group\'][last()]//button[@class=\'btn m-l--1 pointer btn-no-variant b-button btn-addon\']')
    LIST_MASK = ('xpath', '//div[@class=\'b-objects-detail-contentprotection h-100\']//div[@class=\'input-group\']')




    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_protection_button(self):
        with allure.step('В левом фрейме нажать на раздел "География"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.PROTECTION_BUTTON)).click()

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

    def click_on_mask_plus(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.MASK_PLUS_BUTTON)).click()

    def input_mask(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_MASK))

    def input_download_mask(self):
        return self.wait(self.driver).until(ec.presence_of_element_located(self.DOWNLOAD_MASK))

    def get_file_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_FILE_NAME))
        return text.text

    def get_error_text_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.ERROR_TEXT_MODAL))
        return text.text

    def click_checkbox_personal_data(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_PERSON_DATA)).click()

    def click_checkbox_pii(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_PII)).click()

    def click_checkbox_psi_dss(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_PCI_DSS)).click()

    def click_checkbox_phi(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_PHI)).click()

    def click_checkbox_financial_records(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_FINANCIAL_RECORDS)).click()

    def click_checkbox_gdpr_restricted(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_GDPR_RESTRICTED)).click()

    def click_checkbox_gdbpr(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_GDBPR)).click()

    def click_checkbox_glba(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_GLBA)).click()

    def click_checkbox_hipaa(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECKBOX_HIPAA)).click()

    def get_history_financial_records(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_FINANCIAL_RECORDS))
        return text.text

    def get_history_gdbpr(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_GDBPR))
        return text.text

    def get_history_gdpr_restricted(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_GDPR_RESTRICTED))
        return text.text

    def get_history_glba(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_GLBA))
        return text.text

    def get_history_hipaa(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_HIPAA))
        return text.text

    def get_history_pci_dss(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_PCI_DSS))
        return text.text

    def get_history_phi(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_PHI))
        return text.text

    def get_history_financial_records(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_FINANCIAL_RECORDS))
        return text.text

    def get_history_personal_data(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_PERSON_DATA))
        return text.text

    def click_on_close_mask_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CLOSE_MASK_BUTTON)).click()

    def get_count_mask(self):
        list = len (self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_MASK)))
        return list



