from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
import datetime

class NetworkPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    NETWORK_BUTTON = ('xpath', '//li[@class=\'b-super-menu-favorites__item\'][6]/div')
    INTERFACES_PART = ('xpath','//span[text()=\'Интерфейсы\']')
    ADD_BUTTON = ('xpath','//div[@class=\'b-frame-main\']//button')
    GATEWAY_CHOOSE_RIGTH = ('xpath','//span[text()=\' Выбрать \']')
    GATEWAY_CHOOSE_MODAL = ('xpath','//span[@class=\'position-relative truncate-block\']/span')
    SAVE_BUTTON = ('xpath','//span[text()=\' Сохранить \']')
    GATEWAY_TEXT_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div/div[text()]')
    MODAL_ERROR_TEXT = ('xpath','//span[text()=\'Данный интерфейс был создан ранее\']')
    COUNT_INTERFACES = ('xpath','//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']/span[@class=\'d-inline-block text-start\']/span')
    DELETE_BUTTON = ('xpath','//div[@class=\'b-frame-detail__footer-controls\']/i')
    ROW_IN_MAIN_FRAME = ('xpath','//div[@class=\'ag-cell-value ag-cell ag-cell-not-inline-editing ag-cell-normal-height\'][1]')
    CONFIRM_DELETE_BUTTON = ('xpath','//span[text()=\' Удалить \']')
    DISCRIPTOIN_FIELD = ('xpath','//input[@placeholder=\'Введите описание\']')
    STATISTIC_BUTTON = ('xpath', '//a[text()=\'Статистика\']')
    STATISTIC_INFORMATION = ('xpath','//div[@class=\'b-frame-detail__item\'][1]//span[@class=\'b-frame-detail__stats-value d-flex\']/span')




    def click_on_network_button(self):
        with allure.step('Нажать на раздел "Сеть"'):
            self.wait(self.driver).until(EC.element_to_be_clickable(self.NETWORK_BUTTON)).click()


    def click_on_interface_part(self):
        with allure.step('В левом фрейме нажать на раздел "Интерфейсы"'):
            interfaces = self.wait(self.driver).until(EC.visibility_of_element_located(self.INTERFACES_PART))
            interfaces.click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать на "плюс"(добавить объект)'):
            add_button = self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON))
            add_button.click()

    def click_on_gateway_choose_right(self):
        with allure.step('В правом фрейме в строке "Шлюз" нажать на кнопку "Выбрать"'):
            button = self.wait(self.driver).until(EC.visibility_of_element_located(self.GATEWAY_CHOOSE_RIGTH))
            button.click()

    def click_on_gateway_choose_modal(self):
        with allure.step('В модальном окне выбираем созданный шлюз'):
            button = self.wait(self.driver).until(EC.visibility_of_element_located(self.GATEWAY_CHOOSE_MODAL))
            button.click()
    #
    def get_gateway_choose_modal_text(self):
        button = self.driver.find_element(*self.GATEWAY_CHOOSE_MODAL)
        return button.text()

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            button = self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON))
            button.click()



    def get_gateway_text_on_main_frame(self):
        button = self.driver.find_element(*self.GATEWAY_TEXT_ON_MAIN_FRAME)
        return button.text()

    def get_modal_error_text(self):# Получение текста об ошибке в модальном окне при попытке создания повторного объекта
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.MODAL_ERROR_TEXT))
        return text.text

    def get_count_interfaces(self):# Получение количества объектов интерфейса
        count = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_INTERFACES))
        return count.text


    def click_delete_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()


    def click_row_in_main_frame(self):
        with allure.step('В основном фрейме нажать на объект интерфейса'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ROW_IN_MAIN_FRAME)).click()

    def click_confirm_delete_button(self):
        with allure.step('В модальном окне подтверждения удаления нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()

    def discription_field(self):# Поле для ввода описания в правом фрейме
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.DISCRIPTOIN_FIELD))

    def click_on_statistic_button(self):
        with allure.step('В правом фрейме нажать на раздел "Статистика"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def get_statistic_information(self):# Получение текста со статистикой
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_INFORMATION)).text


    def get_current_data(self):# Получение текущей даты
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date
