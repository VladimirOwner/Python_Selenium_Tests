from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import datetime
import allure


class JournalDB(BasePage):
    def __init__(self, driver):
        super().__init__(driver)


    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    JOURNAL_DB_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Журналирование в базы данных\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    INPUT_ENTER_DB = ('xpath', '//input[@placeholder=\'Введите имя базы данных\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    DESCRIPTION_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    CHECK_CONNECTION_BUTTON = ('xpath', '//span[text()=\' Проверить соединение \']')
    SUCCESS_CONNECTION_TEXT = ('xpath', '//div[@class=\'b-objects-detail-logdb__success\']//span')
    LIST_OBJECT_DB = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    ACTIVE_DROP_DOWN_BUTTON = ('xpath', '//button[@class=\'btn z-dropdown btn-no-variant b-button btn-link c-select__button\']//span')
    LIST_ACTIVITY = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div')
    HISTORY_ACTIVITY = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    TYPE_SERVER_BUTTON =('xpath', '//button[@class=\'btn z-dropdown btn-no-variant b-button btn-no-variant c-select__button\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//div[@col-id=\'description\']')
    GET_NAME_OBJECT = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    ERROR_TEXT_MODAL = ('xpath' , '//div[@class=\'mb-0\']/span')
    POSTGRES_DB_BUTTON = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[2]')
    USER_ERROR_TEXT = ('xpath', '//span[text()=\'Пользователь - обязательно для заполнения\']')
    PASSWORD_ERROR_TEXT = ('xpath', '//span[text()=\'Пароль - обязательно для заполнения\']')
    SERVER_ERROR_TEXT = ('xpath', '//span[text()=\'Сервер - обязательно для заполнения\']')
    BD_ERROR_TEXT = ('xpath', '//span[text()=\'База данных - обязательно для заполнения\']')
    INPUT_SRVER =  ('xpath', '//input[@placeholder=\'Введите имя сервера\']')
    INPUT_USER = ('xpath', '//input[@placeholder=\'Введите имя пользователя\']')
    INPUT_PASSWORD = ('xpath', '//input[@placeholder=\'Введите пароль\']')
    HISTORY_TYPE_SERVER = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[8]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    HISTORY_DB = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[3]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[4]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_USER = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[5]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_SERVER = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[6]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')




    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_journaldb_button(self):
        with allure.step('В левом фрейме нажать на раздел "География"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.JOURNAL_DB_BUTTON)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def input_enter_db(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_ENTER_DB))

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

    def choose_list_activity(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_ACTIVITY))
        return list[-1]

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def input_description(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def click_on_check_connection_button(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.CHECK_CONNECTION_BUTTON)).click()

    def get_connection_text(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.SUCCESS_CONNECTION_TEXT))
        return text.text

    def click_on_active_drop_down(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.ACTIVE_DROP_DOWN_BUTTON)).click()

    def get_history_activity(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_ACTIVITY))
        return text.text

    def get_error_text_modal(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.ERROR_TEXT_MODAL))
        return text.text

    def click_on_postgres_db(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.POSTGRES_DB_BUTTON)).click()

    def get_error_text_password(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.PASSWORD_ERROR_TEXT))
        return text.text

    def get_error_text_user(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.USER_ERROR_TEXT))
        return text.text

    def get_error_text_bd(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.BD_ERROR_TEXT))
        return text.text

    def get_error_text_server(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.SERVER_ERROR_TEXT))
        return text.text

    def click_on_type_server(self):
        self.wait(self.driver).until(ec.visibility_of_element_located(self.TYPE_SERVER_BUTTON)).click()

    def input_server(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_SRVER))

    def input_user(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_USER))

    def input_password(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.INPUT_PASSWORD))

    def get_history_type_server(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_TYPE_SERVER))
        return text.text

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

    def get_history_db(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_DB))
        return text.text

    def get_history_name(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_DESCRIPTION))
        return text.text

    def get_history_user(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_USER))
        return text.text

    def get_history_server(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.HISTORY_SERVER))
        return text.text

    def get_count_object(self):
        count = len(self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT_DB)))
        return count

    def get_text_information(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text

