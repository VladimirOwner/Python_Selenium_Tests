from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import datetime
import allure

class ApplicationPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    APP_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name\']//span[text()=\'Приложения\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']/i')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    IN_CATEGORY_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' В категорию \']')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    DESCRIPTOIN_FIELD = ('xpath', '//input[@placeholder=\'Введите описание\']')
    GET_DESCRIPTION_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']//div[@col-id=\'description\']')
    LIST_OBJECT_APP = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    HISTORY_CHANGING_NAME = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[1]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    HISTORY_CHANGING_DESCRIPTION = ('xpath', '//div[@class=\'b-change-modal__content b-change-modal__content_one-block\']/div[2]//div[@class=\'b-change-modal__item--value text-truncate\']/span')
    INPUT_PORT = ('xpath', '//input[@placeholder=\'Введите порты\']')
    INPUT_HOST = ('xpath', '//input[@placeholder=\'Введите хосты\']')
    DROP_DOWN_CATEGORY = ('xpath', '//div[@class=\'c-dropdown-new c-select__dropdown\']//button')
    NETWORK_CATEOGRY = ('xpath', '//div[@class=\'c-dropdown-new__list\']/div[2]')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    CANCEL_BUTTON = ('xpath', '//span[text()=\' Отменить \']/..')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    LIST_OBLIGATORY_FILL = ('xpath', '//div[text()=\' Ошибка в полях: \']/../div[@class=\'mb-0\']')
    FAIL_TEXT_MODAL = ('xpath', '//div[text()=\' Ошибка в поле: \']/..//span')


    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_app_button(self):
        with allure.step('В левом фрейме нажать на раздел "Приложения"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.APP_BUTTON)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def get_name_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def click_on_pencil_button(self):
        with allure.step('Нажать на кнопку редактирование "Карандаш"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def description_field(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DESCRIPTOIN_FIELD))

    def get_description_on_main_frame(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_DESCRIPTION_ON_MAIN_FRAME))
        return text.text

    def choose_object_in_main_frame(self):
        with allure.step('В основном фрейме выбрать созданный объект'):
            list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBJECT_APP))
            return list[-1]

    def click_on_statistic_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Cтатистика"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def click_on_history_button(self):
        with allure.step('Нажать на кнопку "дата" под строкой "История изменений"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def get_history_name(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_NAME))
        return text.text

    def get_history_description(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_DESCRIPTION))
        return text.text

    def input_port(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PORT))

    def input_host(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_HOST))

    def click_on_category_button(self):
        with allure.step('В правом фрейме нажать на кнопку "В категорию"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.IN_CATEGORY_BUTTON)).click()

    def click_on_dropdown(self):
        with allure.step('В правом фрейме нажать на дроп даун выбора категории'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DROP_DOWN_CATEGORY)).click()

    def click_on_network_category(self):
        with allure.step('Из списка категорий выбрать "Сетевое"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.NETWORK_CATEOGRY)).click()

    def click_on_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_on_confirm_delete_button(self):
        with allure.step('В модальном окне нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def click_on_cancel_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Отменить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()
    def click_on_confirm_cancel_button(self):
        with allure.step('В модальном окне нажать на кнопку "Отменить изменения"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_CANCEL_BUTTON)).click()

    def get_text_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text
    def get_list_obligatory_fill(self):
        list = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_OBLIGATORY_FILL))
        return list

    def get_text_fail_modal(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.FAIL_TEXT_MODAL))
        return text.text