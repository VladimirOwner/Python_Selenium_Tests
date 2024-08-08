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
    INPUT_PASSWORD = ('xpath', '//div[@class=\'b-objects-detail-authparam h-100\']//div[@class=\'b-form-group form-group required-field b-input b-form-labels vf-field-pristine vf-field-invalid vf-field-untouched vf-field-invalid-required\'][4]//input[@validatefieldname=\'Пароль\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']//div[@col-id=\'description\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    CHECK_BOX_USE_CASH_ON_IP = ('xpath', '//label[@class=\'c-checkbox-icon c-checkbox-icon_default\']')
    INPUT_SESSION_MIN = ('xpath', '//input[@validatefieldname=\'Срок сессии, мин\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')

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