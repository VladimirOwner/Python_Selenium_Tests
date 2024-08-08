from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class IP_adress(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    IP_ADRESS_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'IP-адреса\']')
    ADD_NEW_IP = ('xpath', '//div/div/div/button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SAVE_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@type=\'button\']/span[text()=\' Сохранить \']')
    INPUT_FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    AUTHOR_OF_CHANGE = ('xpath', '//div[@class=\'ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height\'][text()=\'Администратор\']')
    IP_NAME = ('xpath', '//span/span[@class="truncate-block__name"]')
    INPUT_IP = ('xpath', '//input[@placeholder="Введите IP-адрес, маску или диапазон"]')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    INPUT_EDIT_NAME = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    CLEAR_SEARCH = ('xpath', '//span[@class=\'b-fast-search__remove z-font z-font-delete\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder="Введите описание"]')
    GET_DESCRIPTION = ('xpath', '//span[text()=\'selenium_test_edit_description\']')
    RIGHT_FRAME_STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    IP_FIELD = ('xpath', '//input[@placeholder=\'Введите IP-адрес, маску или диапазон\']')
    GET_IP = ('xpath', '//div[@class=\'b-change-modal__item\']//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_ERR_EMPTY_IP = ('xpath', '//div[@class=\'b-modal__notice-info\']//span')
    ADD_NEW_IP_FIELD = ('xpath', '//div[@class=\'b-badge-list m-t-40 m-b-5 b-badge-list_uppercase\']/div//button')
    DELETE_OBJECT = (('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i'))
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    SECOND_IP_FIELD = ('xpath', '//div[@class=\'b-objects-detail-clientsip h-100\']/div[2]/div[2]//input')
    IP_CLEAR_BUTTON = ('xpath', '//button[@class=\'btn pointer btn-no-variant b-button btn-addon\']/i[1]')


    def click_on_object_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_ip_adress_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_ADRESS_BUTTON)).click()

    def click_on_add_new_object(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_NEW_IP)).click()

    def click_on_save_IP(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def input_fast_search(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_FAST_SEARCH))

    def get_author(self):
        return self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.AUTHOR_OF_CHANGE))

    def get_name_of_ip_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_NAME))
        return text.text

    def input_ip(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_IP))

    def click_on_pencil_edit_icon(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_EDIT_ICON)).click()

    def click_name_of_ip_object(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_NAME)).click()

    def input_edit_name(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_EDIT_NAME))

    def click_on_clear_search(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CLEAR_SEARCH)).click()

    def input_description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def click_on_statistics(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.RIGHT_FRAME_STATISTICS)).click()

    def click_last_change(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.LAST_CHANGE)).click()

    def get_description(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def clear_ip_field(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_FIELD)).clear()

    def input_ip_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_FIELD))

    def get_ip(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_IP))
        return text.text

    def get_error_empty_ip(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_ERR_EMPTY_IP))
        return text.text

    def add_new_ip_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_NEW_IP_FIELD)).click()

    def delete_object(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_OBJECT)).click()

    def accept_delete_object(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT)).click()

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text

    def input_second_ip(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.SECOND_IP_FIELD))

    def click_on_ip_clear_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.IP_CLEAR_BUTTON)).click()
