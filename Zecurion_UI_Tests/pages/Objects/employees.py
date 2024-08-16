from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import datetime
import allure


class Employees(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//span[text()=\'Объекты\']')
    DROPDOWN_EMPLOYEES = ('xpath', '//span[text()=\'Сотрудники\']/../..//span[@class="c-caret b-left-frame-tree__caret"]')
    SUBDIVISION_BUTTON = ('xpath', '//span[text()=\' Подразделения \']')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']/..')
    FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'text-highlight\']')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    EDIT_NAME_OBJECT = ('xpath', '//input[@placeholder=\'Введите имя\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@validatefieldname=\'Описание\']')
    RIGHT_FRAME_STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    GET_DESCRIPTION = ('xpath', '//span[text()=\'selenium_test_edit_subdivision_description\']')  # поменять поиск элемента, не привязывать к какому-то значению
    ADD_DIVISION_TO_OBJECT = ('xpath', '//div[text()=\' Подразделения \']/..//button')
    MODAL_FAST_SEARCH = ('xpath', '//div[@class="modal-body__inner-container"]//input[@placeholder=\'Быстрый поиск\']')
    GET_NAME_MODAL_OBJECT = ('xpath', '//div[@class=\'modal-body\']//div[@class=\'ag-center-cols-viewport\']//div[@role=\'row\']')
    # GET_NAME_MODAL_OBJECT = ('xpath', '//div[@class="ag-center-cols-clipper"][@style="height: 40px;"]//span[@class="truncate-block__name"]]')
    MODAL_APPLY_BUTTON = ('xpath', '//span[text()=\' Применить \']')
    GET_DIVISION = ('xpath', '//span[text()=\' selenium_test_edit_subdivision_name_2\']')
    DELETE_OBJECT = ('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i')
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    EMPLOYEES_BUTTON = ('xpath', '//span[text()=\' Сотрудники \']')
    INPUT_LOGIN = ('xpath', '//input[@placeholder="Введите логин"]')
    INPUT_PASS = ('xpath', '//input[@placeholder="Введите пароль"]')
    GET_EMPLOYEE_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[6]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_EMPLOYEE_EMAIL = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_EMPLOYEE_IP = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    GET_EMPLOYEE_ALLOWED_SIZE = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[8]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    EMPLOYEE_EMAIL_FIELD = ('xpath', '//input[@placeholder="Введите e-mail для уведомлений"]')
    EMPLOYEE_IP_FIELD = ('xpath', '//input[@placeholder="Введите допустимые IP-адреса"]')
    QUOTAS_DROPDOWN = ('xpath', '//button[@class="btn z-dropdown btn-no-variant b-button btn-no-variant c-select__button"]')
    QUOTAS_DROPDOWN_DAY = ('xpath', '//div[@class="c-dropdown-new__list"]/div[@class="c-select__wrapper c-dropdown-new__item active text-truncate"]')
    QUOTAS_DROPDOWN_WEEK = ('xpath', '//div[@class="c-dropdown-new__list"]/div[@class="c-select__wrapper c-dropdown-new__item text-truncate"][2]')
    QUOTAS_DROPDOWN_MONTH = ('xpath', '//div[@class="c-dropdown-new__list"]/div[@class="c-select__wrapper c-dropdown-new__item text-truncate"][3]')
    QUOTAS_ALLOWED_SIZE_FIELD = ('xpath', '//input[@placeholder="Введите размер"]')
    GET_ERR_EMPTY_FIELD = ('xpath', '//span[text()=\'Разрешенный размер, МБ - обязательно для заполнения\']')
    BLOCK_EMPLOYEE_BUTTON = ('xpath', '//span[text()=\' Заблокировать \']/..')
    EMAIL_NOTIFICATION_BUTTON = ('xpath', '//span[text()=\' Выслать на почту ссылку-приглашение \']/..')
    CHANGE_PASS_IN_NEXT_LOGIN_BUTTON = ('xpath', '//span[text()=\' Изменить пароль при следующем входе \']/..')
    GET_BLOCK_TIME = ('xpath', '//span[text()=\' Разблокировать \']/../..//div')
    GET_EMAIL_NOTIFICATION_TIME = ('xpath', '//span[text()=\' Выслать на почту новую ссылку-приглашение \']/../..//div')
    GET_CHANGE_PASS_TIME = ('xpath', '//span[text()=\' Изменить пароль при следующем входе \']/../..//div')
    CHANGE_PASSWORD = ('xpath', '//span[text()=\' Изменить пароль \']/..')
    CURRENT_PASSWORD = ('xpath', '//input[@placeholder="Введите текущий пароль"]')
    NEW_PASSWORD = ('xpath', '//input[@placeholder="Введите новый пароль"]')
    CONFIRM_PASSWORD = ('xpath', '//input[@placeholder="Подтвердите новый пароль"]')
    SAVE_NEW_PASSWORD = ('xpath', '//button[@class="btn b-modal__button b-button_primary btn-no-variant b-button btn-no-variant"]')
    EMPTY_CURRENT_PASSWORD = ('xpath', '//div[@class="vf-form-pristine vf-form-invalid vf-form-touched"]/div[1]//div[@class="b-form-input__text-danger"]')
    EMPTY_NEW_PASSWORD = ('xpath', '//div[@class="vf-form-pristine vf-form-invalid vf-form-touched"]/div[2]//div[@class="b-form-input__text-danger"]')
    EMPTY_CONFIRM_PASSWORD = ('xpath', '//div[@class="vf-form-pristine vf-form-invalid vf-form-touched"]/div[3]//div[@class="b-form-input__text-danger"]')
    CURRENT_PASS_INCORRECT = ('xpath', '//div[@class="b-form-input__text-danger offset-lg-3 offset-4 p-t-2 p-l-3"]')
    PASSWORDS_NOT_MATCH = ('xpath', '//div[@class="b-form-group form-group required-field b-form-labels b-form-labels_two-rows vf-field-dirty vf-field-invalid vf-field-touched vf-field-invalid-validate"]//div[@class="b-form-input__text-danger"]')
    TITLE_MODAL = ('xpath', '//span[text()=" Изменение пароля "]')

    def object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def dropdown_employees(self):
        with allure.step('Нажать на дропдаун "Сотрудники" в левом фрейме'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_EMPLOYEES))

    def subdivision_button(self):
        with allure.step('Нажать на подраздел "Подразделения"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SUBDIVISION_BUTTON))

    def add_new_object(self):
        with allure.step('Нажать на кнопку создания нового объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def save_button(self):
        with allure.step('Нажать на кнопку "Сохранить" объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def fast_search_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.FAST_SEARCH))

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def open_object(self):
        with allure.step('Открываем выбранный объект'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))

    def pencil_edit_icon(self):
        with allure.step('Нажать на иконку редактирования имени объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def edit_name_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EDIT_NAME_OBJECT))

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        with allure.step('Открыть вкладку Статистика'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.RIGHT_FRAME_STATISTICS))

    def last_change(self):
        with allure.step('Открыть последнее изменение объекта'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def add_division_to_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_DIVISION_TO_OBJECT))

    def modal_fast_search_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.MODAL_FAST_SEARCH))

    def modal_object_name(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_MODAL_OBJECT))

    def modal_apply_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.MODAL_APPLY_BUTTON))

    def get_division(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DIVISION))
        return text.text

    def delete_object(self):
        with allure.step('Нажать на иконку "Удаление объекта"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_OBJECT))

    def accept_delete_object(self):
        with allure.step('Нажать на кнопку подтверждения "Удаления объекта"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT))

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text

    def employees_button(self):
        with allure.step('Нажать на подраздел "Сотрудники"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPLOYEES_BUTTON))

    def input_login(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_LOGIN))

    def input_pass(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_PASS))

    def get_employee_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_EMPLOYEE_DESCRIPTION))
        return text.text

    def get_employee_email(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_EMPLOYEE_EMAIL))
        return text.text

    def get_employee_ip(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_EMPLOYEE_IP))
        return text.text

    def email_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPLOYEE_EMAIL_FIELD))

    def ip_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPLOYEE_IP_FIELD))

    def quotas_dropdown(self):
        with allure.step('Нажатие на дропдаун поля "Квоты"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.QUOTAS_DROPDOWN))

    def quotas_dropdown_everyday(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.QUOTAS_DROPDOWN_DAY))

    def quotas_dropdown_every_week(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.QUOTAS_DROPDOWN_WEEK))

    def quotas_dropdown_every_month(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.QUOTAS_DROPDOWN_MONTH))

    def quotas_allowed_size_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.QUOTAS_ALLOWED_SIZE_FIELD))

    def get_employee_allowed_size(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_EMPLOYEE_ALLOWED_SIZE))
        return text.text

    def get_err_empty_field(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_ERR_EMPTY_FIELD))
        return text.text

    def block_employee_button(self):
        with allure.step('Нажать на кнопку "Заблокировать'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.BLOCK_EMPLOYEE_BUTTON))

    def get_block_time_employee(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_BLOCK_TIME))
        return text.text

    def email_notification_button(self):
        with allure.step('Нажать на кнопку "Выслать на почту ссылку-приглашение'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.EMAIL_NOTIFICATION_BUTTON))

    def change_pass_in_next_login_button(self):
        with allure.step('Нажать на кнопку "Изменить пароль при следующем входе"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.CHANGE_PASS_IN_NEXT_LOGIN_BUTTON))

    def get_email_notification_time(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_EMAIL_NOTIFICATION_TIME))
        return text.text

    def get_change_pass_time(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_CHANGE_PASS_TIME))
        return text.text

    def change_pass_button(self):
        with allure.step('Нажать на кнопку "Изменить пароль"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.CHANGE_PASSWORD))

    def input_current_password(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.CURRENT_PASSWORD))

    def input_new_password(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.NEW_PASSWORD))

    def input_password_confirm(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.CONFIRM_PASSWORD))

    def save_new_password_button(self):
        with allure.step('Нажать на кнопку "Сохранить" пароль'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_NEW_PASSWORD))

    def get_empty_current_pass(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPTY_CURRENT_PASSWORD))
        return text.text

    def get_empty_new_pass(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPTY_NEW_PASSWORD))
        return text.text

    def get_empty_confirm_pass(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.EMPTY_CONFIRM_PASSWORD))
        return text.text

    def get_err_current_pass(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.CURRENT_PASS_INCORRECT))
        return text.text

    def get_password_not_match(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.PASSWORDS_NOT_MATCH))
        return text.text

    def title_modal(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.TITLE_MODAL))

    def get_current_data(self):
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date
