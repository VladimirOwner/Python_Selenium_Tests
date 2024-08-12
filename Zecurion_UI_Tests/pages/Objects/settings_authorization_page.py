from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure

class AuthorizationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    AUTHORIZATION_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Параметры авторизации\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    INPUT_URL_LDAP = ('xpath', '//input[@validatefieldname=\'URL LDAP\']')
    INPUT_BASE_OU = ('xpath', '//input[@validatefieldname=\'Базовая OU\']')
    INPUT_LOGIN = ('xpath', '//input[@validatefieldname=\'Логин\']')
    INPUT_PASSWORD = ('xpath', '//div[@class=\'b-objects-detail-authparam h-100\']//div[@class=\'password-input--wrap\']//input[@validatefieldname=\'Пароль\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']//div[@col-id=\'description\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    CHECK_BOX_USE_CASH_ON_IP = ('xpath', '//label[@class=\'c-checkbox-icon c-checkbox-icon_default\']')
    INPUT_SESSION_MIN = ('xpath', '//input[@validatefieldname=\'Срок сессии, мин\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    TYPE_IN_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[@col-id=\'authtype\']')
    LIST_OBJECT_AUTHORIZATION = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[@role=\'row\']')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    CHECK_BUTTON = ('xpath', '//span[text()=\' Проверить \']/..')
    FAILD_TEXT_INFORMATION = ('xpath', '//div[@class=\'b-objects-detail-authparam__check-info\']//span')
    TYPE_OF_PORTAL_BUTTON = ('xpath', '//span[text()=\' Выберите вид портала \']/..')
    GET_HEADER_MODAL = ('xpath', '//span[text()=\' Вид портала \']')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    CHECKBOX_REJECT_REAPITE_AUTHORIZATOIN = ('xpath', '//div[@class=\'b-objects-detail-authparam h-100\']//label[2]/i')
    CONFIRM_REJECT_AUTHORIZATION_IN_STATISTIC = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[6]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    ERROR_TEXT_MODAL = ('xpath' , '//div[@class=\'mb-0\']/span')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить изменения \']')
    HISTORY_CHANGING_GET_LDAP = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_GET_LOGIN = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[3]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_GET_OU = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[4]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_GET_AUTHORIZATION_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[13]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_GET_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[14]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_GET_TYPE = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[19]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    LIST_AUTHORIZATION_BUTTON = ('xpath', '//div[@class=\'c-dropdown-new c-select__dropdown\']/button')
    BASIC_AUTHORIZATION = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[2]')
    INPUT_TIME_SESSION = ('xpath' , '//input[@placeholder=\'Введите срок сессии, мин\']')
    TEXT_OBLIGATORY_FILL = ('xpath', '//div[text()=\' Ошибка в поле: \']/..//span')
    LIST_SOURCE = ('xpath', '//p[text()=\' Домен \']/../../..')
    ADDRESS_BOOK_BUTTON = ('xpath', '//p[text()=\' Адресная книга \']/..')
    USERS = ('xpath', '//p[text()=\' Все \']/..')
    HISTORY_CHANGING_TIME_SESSION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[17]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INPUT_COUNT_ENTRANCE = ('xpath', '//input[@validatefieldname=\'Количество ошибок входа\']')
    HISTORY_COUNT_ENTRANCE = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[12]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    TACACS_AUTHORIZATION = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[3]')
    INPUT_IP_ADRESS = ('xpath', '//input[@validatefieldname=\'IP-адрес\']')
    INPUT_SECRET = ('xpath', '//input[@validatefieldname=\'Секрет\']')
    LIST_OBLIGATORY_FILL = ('xpath', '//div[text()=\' Ошибка в полях: \']/../div[@class=\'mb-0\']')
    DOWNLOAD_CERTIFICATE_BUTTON = ('xpath', '//div[@class=\'b-upload-button b-button btn-link\']/..//input[@type=\'file\']')
    INPUT_PORT = ('xpath', '//input[@placeholder=\'Введите порт\']')
    INPUT_FQDN = ('xpath', '//input[@placeholder=\'Введите внешний fqdn\']')
    INPUT_CERTIFICATE = ('xpath', '//input[@placeholder=\'Введите подпись центра сертификации\']')
    DC_LOG_AUTHORIZATION = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[4]')
    DOWNLOAD_KEY_BUTTON = ('xpath', '//div[@class=\'b-upload-button b-button btn-link m-r-10\']//input')
    FAIL_TEXT_MODAL = ('xpath', '//div[@class=\'b-modal__notice-info b-modal__notice-info_pre-wrap\']/span')
    HISTORY_PORT = ('xpath','//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[16]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_FILL_CERTIFICATE = ('xpath','//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[15]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_KEY = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[7]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CERTIFICATE = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[8]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_NAME_SERTIFICATE = ('xpath' , '//div[@class=\'b-manage-certificate__value\']/span[1]')
    GET_NAME_KEY = ('xpath', '//span[text()=\' Ключ \']/..//span[@class=\'b-manage-certificate__value--name text-truncate\']')
    PORTAL_AUTHORIZATION = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[5]')
    RADIUS_AUTHORIZATION = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[6]')

    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_authorization_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.AUTHORIZATION_BUTTON)).click()

    def click_on_add_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def input_url_ldap(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_URL_LDAP))

    def input_base_ou(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_BASE_OU))

    def input_login(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_LOGIN))

    def input_password(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PASSWORD))

    def click_on_save_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def click_on_delete_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_cancel_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()

    def click_on_checkbox_cash_on_ip(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_BOX_USE_CASH_ON_IP)).click()

    def get_default_min(self):
        value = self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_SESSION_MIN)).get_attribute('value')
        return int(value)

    def get_type_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.TYPE_IN_MAIN_FRAME))
        return text.text

    def choose_object_in_main_frame(self):
        list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECT_AUTHORIZATION))
        return list[-1]
    def click_on_pencil_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def get_name_in_main_frame(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTOIN_FIELD))

    def get_description_in_main_frame(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text

    def click_on_check_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_BUTTON)).click()

    def get_fail_text_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.FAILD_TEXT_INFORMATION))
        return text.text

    def click_on_type_of_portal_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.TYPE_OF_PORTAL_BUTTON)).click()

    def get_text_header_madal(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_HEADER_MODAL))
        return text.text

    def click_on_statistic_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def click_on_history_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def click_on_checkbox_reject_repeate_authorization(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECKBOX_REJECT_REAPITE_AUTHORIZATOIN)).click()

    def get_reject_authorization_on_statistic(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_REJECT_AUTHORIZATION_IN_STATISTIC))
        return text.text
    def get_error_text_modal(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.ERROR_TEXT_MODAL))
        return text.text

    def click_on_confirm_cancel_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_CANCEL_BUTTON)).click()

    def get_history_ldap(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_LDAP))
        return text.text

    def get_history_login(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_LOGIN))
        return text.text

    def get_history_ou(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_OU))
        return text.text

    def get_history_autharization(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_AUTHORIZATION_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_DESCRIPTION))
        return text.text

    def get_history_type(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_GET_TYPE))
        return text.text

    def click_on_confirm_delete_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def get_text_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text
    def click_on_list_authorization(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.LIST_AUTHORIZATION_BUTTON)).click()

    def click_on_basic(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.BASIC_AUTHORIZATION)).click()

    def input_time_session(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_TIME_SESSION))

    def get_text_obligatory_fill(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.TEXT_OBLIGATORY_FILL))
        return text.text
    def click_on_list_source(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.LIST_SOURCE)).click()

    def click_adress_book_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADDRESS_BOOK_BUTTON)).click()

    def get_field_users(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.USERS)).text

    def get_history_time_session(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_TIME_SESSION))
        return text.text

    def input_count_entrance(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_COUNT_ENTRANCE))

    def get_history_count_entrance(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_COUNT_ENTRANCE))
        return text.text

    def click_on_tacacs(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.TACACS_AUTHORIZATION)).click()

    def input_ip_adress(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_IP_ADRESS))

    def input_secret(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_SECRET))
    def get_list_obligatory_fill(self):
        list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBLIGATORY_FILL))
        return list
    def click_on_dc_log(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.DC_LOG_AUTHORIZATION)).click()

    def input_port(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PORT))

    def input_download_certificate(self):
        return self.wait(self.driver).until(EC.presence_of_element_located(self.DOWNLOAD_CERTIFICATE_BUTTON))

    def input_fqdn(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_FQDN))

    def input_certificate(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_CERTIFICATE))

    def input_download_key(self):
        return self.wait(self.driver).until(EC.presence_of_element_located(self.DOWNLOAD_KEY_BUTTON))

    def get_text_fail_modal(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.FAIL_TEXT_MODAL))
        return text.text
    def get_history_port(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_PORT))
        return text.text

    def get_history_fill_sertification(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_FILL_CERTIFICATE))
        return text.text
    def get_history_name_key(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_KEY))
        return text.text

    def get_history_name_certificate(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CERTIFICATE))
        return text.text

    def get_name_sertificate(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_SERTIFICATE))
        return text.text
    def get_name_key(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_KEY))
        return text.text
    def click_on_portal(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.PORTAL_AUTHORIZATION)).click()

    def click_on_radius(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.RADIUS_AUTHORIZATION)).click()