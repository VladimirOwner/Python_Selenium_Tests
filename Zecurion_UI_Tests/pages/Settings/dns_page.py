from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import datetime

class DNSPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)


    SETTING_BUTTON = ('xpath','//section[@class=\'ps-container b-scroll-area b-super-menu__nav-container b-super-menu-favorites__list ps ps--theme_default\']/li[6]')
    DNS_SERVERS = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'DNS-серверы\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    DNS_SERVERS_FIELD = ('xpath','//input[@placeholder=\'Введите адрес DNS-сервера\']')
    ADD_DNS_SERVER = ('xpath','//div[text()=\' DNS-серверы \']/..//button[@class=\'btn b-badge-list__header-icon click-area btn-no-variant b-button btn-link\']')
    DNS_SERVER_SECOND_FIELD = ('xpath','//div[@class=\'b-settings-objects-detail-dnsserver h-100\']//div[@class=\'input-group\'][2]//input' )
    SAVE_BUTTON = ('xpath','//button[@class=\'btn b-button_primary btn-no-variant b-button btn-no-variant\']')
    COUNT_OBJECTS_IN_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[@role=\'row\']')
    DISCRIPTION_FIELD = ('xpath','//input[@placeholder=\'Введите описание\']')
    DISCRIPTION_IN_MAIN_FRAME = ('xpath','//div[@class=\'ag-center-cols-container\']//div[@role=\'row\'][2]//div[@col-id=\'description\']')
    OBJECT_IN_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[@role=\'row\'][2]')
    STATISTIC_BUTTON = ('xpath','//ul[@role=\'tablist\']/li[3]')
    STATISTIC_INFORMATION = ('xpath', '//span[text()=\'Создано\']/../span[@class=\'b-frame-detail__stats-value d-flex\']/span')
    DELETE_BUTTON = ('xpath','//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE = ('xpath', '//button[@class=\'btn b-modal__button b-button_primary btn-no-variant b-button btn-no-variant\']')
    ERROR_MODAL_TEXT = ('xpath', '//span[text()=\'Адрес DNS-сервера - обязательно для заполнения\']')
    OBLIGATORY_TO_FILL_FIELD = ('xpath','//div[@class=\'input-group\']//div[text()=\'обязательно для заполнения\']')

    def click_on_setting_button(self):
        with allure.step('Нажать на кнопку "Настройки"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SETTING_BUTTON)).click()

    def click_on_dns_servers_part(self):
        with allure.step('В левом фрейма нажать на раздел "DNS-серверы"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DNS_SERVERS)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def dns_server_field(self):
        with allure.step('В поле адреса DNS-сервера ввести ip адрес'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DNS_SERVERS_FIELD))

    def click_on_add_dns_server(self):
        with allure.step('В строке DNS-СЕРВЕРЫ нажать на кнопку "+"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_DNS_SERVER)).click()

    def dns_server_field_second(self):
        with allure.step('В поле адреса DNS-сервера ввести дополнительный ip адрес сервера'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DNS_SERVER_SECOND_FIELD))

    def click_on_save_button(self):
        with allure.step('Нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def get_count_object_dns(self):
        count = len(self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.COUNT_OBJECTS_IN_MAIN_FRAME)))
        return count

    def discription_field(self):
        with allure.step('В поле описание ввести произвольные символы'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTION_FIELD))

    def get_discription(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTION_IN_MAIN_FRAME)).text

    def objects_in_main_frame(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_IN_MAIN_FRAME))

    def click_on_statistic_button(self):
        with allure.step('В правом фрейме нажать на раздел "Статистика"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def get_current_data(self):# Получение текущей даты
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date

    def get_statistic_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_INFORMATION))
        return text.text

    def click_on_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete(self):
        with allure.step('В модальном окне подтвердить удаление объекта (нажать на кнопку "Удалить")'):
             self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE)).click()

    def get_error_modal_text(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.ERROR_MODAL_TEXT))
        return text.text

    def get_obligatory_to_fill_text(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.OBLIGATORY_TO_FILL_FIELD))
        return text.text