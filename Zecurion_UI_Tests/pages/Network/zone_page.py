from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import datetime

class ZonePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    NETWORK_BUTTON = ('xpath', '//li[@class=\'b-super-menu-favorites__item\'][6]/div')
    ZONE_PART = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Зоны\']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    SECURITY_LEVEL_FIELD = ('xpath', '//input[@placeholder=\'Введите уровень безопасности\']')
    GATEWAY_CHOOSE_RIGTH = ('xpath', '//span[text()=\' Выбрать \']')
    GATEWAY_CHOOSE_MODAL = ('xpath','//div[@class=\'modal-body__inner-container\']//div[@row-index=\'0\']//span[@class=\'truncate-block__name truncate-block__name_link\']')
    ADD_INTERFACE_BUTTON = ('xpath','//div[text()=\' Интерфейсы \']/..//button')
    CHOOSE_MODAL_INTERFACE = ('xpath', '//div[@id=\'b-select-gateways-modal___BV_modal_body_\']//div[@class=\'ag-center-cols-container\']//div[@row-index=\'0\']')
    APPLY_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant b-modal__button b-button_primary\']')
    SAVE_BUTTON = ('xpath', '//span[text()=\' Сохранить \']')
    COUNT_ZONE = ('xpath', '//span[text()=\'Зоны\']/../span[@class=\'d-inline-block text-start\']/span')
    ROW_IN_MAIN_FRAME = ('xpath','//div[@class=\'ag-center-cols-clipper\']//div[@row-index=\'0\']')
    DELETE_BUTTON = ('xpath','//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath','//span[text()=\' Удалить \']')
    MODAL_ERROR_TEXT = ('xpath', '//span[text()=\'Данные интерфейсы были ранее указаны в других зонах\']')
    DISCRIPTION_FIELD = ('xpath','//input[@placeholder=\'Введите описание\']')
    COUNT_MUST_MORE_ONE = ('xpath','//div[text()=\'Число должно быть целым и больше или равно 1\']')
    COUNT_MUST_LESS = ('xpath', '//div[text()=\'Число должно быть целым и меньше или равно 255\']')
    GATEWAY_ERROR_TEXT = ('xpath', '//span[text()=\'Шлюз - Шлюз должен быть выбран\']')
    SECURITY_LEVEL_ERROR_TEXT = ('xpath','//span[text()=\'Уровень безопасности - обязательно для заполнения\']')
    CANCEL_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@class=\'btn btn-no-variant b-button btn-no-variant\']')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button[@class=\'btn b-modal__button b-button_primary btn-no-variant b-button btn-no-variant\']')
    STATISTIC_BUTTON = ('xpath','//a[text()=\'Статистика\']')
    STATISTIC_INFORMATION = ('xpath','//div[@class=\'tab-pane active\']//div[@class=\'b-frame-detail__item\']//span[@class=\'b-frame-detail__stats-value d-flex\']/span')




    def click_on_network_button(self):
        with allure.step('Нажать на раздел "Сеть"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.NETWORK_BUTTON)).click()

    def click_on_zone_part(self):
        with allure.step('В левом фрейме нажать на раздел "Зоны"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ZONE_PART)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать на "плюс"(добавить объект)'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def securyty_level_field(self):# Поле "Уровень безопасности"
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.SECURITY_LEVEL_FIELD))

    def click_on_gateway_choose_right(self):
        with allure.step('В правом фрейме в строке "Шлюз" нажать на кнопку "Выбрать"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.GATEWAY_CHOOSE_RIGTH)).click()

    def click_on_gateway_choose_modal(self):
        with allure.step('В модальном окне выбираем созданный шлюз'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.GATEWAY_CHOOSE_MODAL)).click()

    def click_on_add_interface_button(self):
        with allure.step('В правом фрейме нажать на кнопку добавления интерфейса'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_INTERFACE_BUTTON)).click()

    def click_on_choose_modal_interface(self):
        with allure.step('В модальном окне выбрать интерфейс'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHOOSE_MODAL_INTERFACE)).click()

    def click_apply_button(self):
        with allure.step('Нажать кнопку "Применить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.APPLY_BUTTON)).click()

    def click_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def get_count_zone(self):# Получение количества объектов зон
        count = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_ZONE))
        return count.text

    def click_on_row_in_main_frame(self):
        with allure.step('В основном фрейме выбрать объект "Зона"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ROW_IN_MAIN_FRAME)).click()

    def click_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_confirm_delete_button(self):
        with allure.step('В модальном окне подтверждения удаления нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def get_modal_error_text(self):# Текст ошибки в модальном окне
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.MODAL_ERROR_TEXT))
        return text.text

    def discription_field(self):# Поле "Описание"
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTION_FIELD))

    def get_error_text_count_more_one(self):# Текст подсказки под полем зона безопасности что поле должно быть больше 0
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_MUST_MORE_ONE))
        return text.text

    def get_error_text_count_less(self):# Текст подсказки под полем зона безопасности что поле должно быть болшьше 255
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_MUST_LESS))
        return text.text

    def get_gateway_error_text(self):# Текст подсказки в строке Шлюз об обязательности выбора шлюза
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GATEWAY_ERROR_TEXT))
        return  text.text

    def get_security_level_error_text(self):# Текст подсказки под полем зона безопасности об обязательности заполнения поля
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.SECURITY_LEVEL_ERROR_TEXT))
        return text.text

    def click_on_cancel_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()

    def click_confirm_cancel_button(self):
        self.wait(self.driver).until(EC.element_to_be_clickable(self.CONFIRM_CANCEL_BUTTON)).click()

    def click_statistic_button(self):
        with allure.step('В правом фрейме нажать на раздел "Статистика"'):
            self.wait(self.driver).until(EC.element_to_be_clickable(self.STATISTIC_BUTTON)).click()

    def get_statistic_information(self):# Получение даты в разделе Статистика
        text = self.wait(self.driver).until(EC.element_to_be_clickable(self.STATISTIC_INFORMATION))
        return text.text

    def get_current_data(self):# Получение текущей даты
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date