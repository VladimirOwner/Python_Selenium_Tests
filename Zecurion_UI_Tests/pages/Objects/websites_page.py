from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import datetime
import allure

class WebsitesPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    WEBSITES_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name\']//span[text()=\'Веб-сайты — URL\']')
    INFORMATION_lAST_UPDATE = ('xpath', '//div[@class=\'b-objects-root-detail-websites__update\']/span')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']/i')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'form-group b-form-input\']//div[@class=\'b-form-input__container\']/input[@placeholder=\'Введите имя\']')
    DELETE_FAST_SEARCH_INFORMATION = ('xpath', '//span[@class=\'b-fast-search__remove z-font z-font-delete\']')
    GET_NAME_OBJECT = ('xpath', '//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    CATEGORIES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']//div[text()=\'Администратор\']')
    IN_CATEGORY_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' В категорию \']')
    ADD_BUTTON_WEBSITE = ('xpath', '//div[@class=\'b-frame-main__buttons\']')
    HOST_INPUT = ('xpath', '//div[@class=\'col\']/input[@placeholder=\'Введите хост\']')
    LIST_WEBSITES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    STATISTIC_INFORMATION_WEBSITE = ('xpath', '//span[text()=\'Создано\']/../span[@class=\'b-frame-detail__stats-value d-flex\']/span')
    INPUT_FAST_SEARCH = ('xpath', '//div[@class=\'b-fast-search b-fast-search_no-variant\']//input')
    FILTER_HEADER = ('xpath', '//span[text()=\'Автор изменения\']/../../span')
    AUTHOR_CHANCHED = ('xpath','//label[@class=\'c-checkbox-icon c-checkbox-icon_type-1\']/span[text()=\'Администратор\']')
    CHECK_FILTER = ('xpath', '//button/i[@class=\'button-before-icon fas fa-check\']')
    GET_NAME_WEBSITE = ('xpath', '//span[@class=\'c-pencil-edit__title-text text-truncate\']')
    CHECK_WEBSITE_BUTTON = ('xpath','//button/span[text()=\' Проверить сайт \']')
    INPUT_CHECK_WEBSITE = ('xpath', '//input[@placeholder=\'Введите хост или URL\']')
    CHECK_BUTTON = ('xpath', '//button/span[text()=\' Проверить \']')
    LIST_CATEGORIES = ('xpath', '//div[@class=\'b-modal__notice-info\']/div/div')
    STATISTIC_BUTTON = ('xpath', '//li/a[text()=\'Статистика\']')
    ERROR_TEXT_HOST = ('xpath', '//div/span[text()=\'Хост - обязательно для заполнения\']')
    CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить \']')
    CONFIRM_CANCEL_BUTTON = ('xpath', '//button/span[text()=\' Отменить изменения \']')
    DELETE_BUTTON = ('xpath', '//i[@class=\'b-frame-detail__footer-delete far fa-trash-alt\']')
    CONFIRM_DELETE_BUTTON = ('xpath', '//button/span[text()=\' Удалить \']')
    INFORMATION_MESSAGE = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')
    CHANGING_INFORMATION_CATEGORIES = ('xpath', '//span[text()=\'Изменено\']/../span[@class=\'b-frame-detail__stats-value d-flex\']/span')
    HISTORY_BUTTON = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    HISTORY_CATEGORIE_NAME = ('xpath', '//div[@class=\'b-change-modal__item--description\']/div/span')
    HISTORY_CHANGING_INFORMATION = ('xpath', '//span[@class=\'b-change-modal__header-changes\']')
    CHECK_BOX_UPDATE_DAYS = ('xpath', '//label[@class=\'m-t-20 c-checkbox-icon c-checkbox-icon_default\']/i')
    DEFAULT_DAYS = ('xpath','//div[@class=\'form-row form-group b-form-input\']//input[@placeholder=\'\']')
    COUNT_CATEGORIES = ('xpath', '//div[text()=\' Категории \']/../div[@class=\'b-frame-detail__contents-count\']')
    COUNT_SITES = ('xpath', '//div[text()=\' Сайты \']/../div[@class=\'b-frame-detail__contents-count\']')
    ICON = ('xpath', '//i[@class=\'fas fa-exclamation-circle warning-icon m-l-10\']')

    def click_on_object_button(self):
        with allure.step('Нажать на раздел "Объекты"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_websites_button(self):
        with allure.step('В левом фрейме нажать на раздел "Веб сайты-URL"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.WEBSITES_BUTTON)).click()

    def click_on_add_button(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()

    def input_fast_search(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_FAST_SEARCH))

    def categorie_in_main_frame(self):
        with allure.step('В правом фрейме нажать на кнопку "Сохранить"'):
            return self.wait(self.driver).until(EC.visibility_of_element_located(self.CATEGORIES_ON_MAIN_FRAME))


    def get_name_object(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def click_on_pencil_button(self):
        with allure.step('Нажать на кнопку редактирование "Карандаш"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.PENCIL_BUTTON)).click()

    def input_pencil(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_PENCIL_FIELD))

    def click_on_delete_fast_search_information(self):
        with allure.step('Нажать на кнопку удаления справа в строке быстрого поиска'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_FAST_SEARCH_INFORMATION)).click()

    def click_on_add_button_website(self):
        with allure.step('В основном фрейме нажать снизу на кнопку "Добавить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON_WEBSITE)).click()

    def click_filter_header(self):
        with allure.step('В основном фрейме в столбце "Автор изменения" нажать на "Фильтр"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.FILTER_HEADER)).click()
    def click_checkbox_authtor(self):
        with allure.step('В открывшемся окне выбрать чек бокс "Администратор"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.AUTHOR_CHANCHED)).click()

    def click_on_check_filter(self):
        with allure.step('Нажать на кнопку применения фильтра'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_FILTER)).click()

    def click_on_category_button(self):
        with allure.step('В правом фрейме нажать на кнопку "В категорию"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.IN_CATEGORY_BUTTON)).click()
    def host_input(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.HOST_INPUT))
    def get_name_website(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.GET_NAME_WEBSITE))
        return text.text
    def click_on_check_website(self):
        with allure.step('В правом фрейме, снизу, нажать на кнопку "Проверить сайт"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_WEBSITE_BUTTON)).click()

    def input_check_website(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.INPUT_CHECK_WEBSITE))

    def click_check_button(self):
        with allure.step('В модальном окне нажать на кнопку "Проверить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_BUTTON)).click()

    def list_category(self):
        list= self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.LIST_CATEGORIES))
        for l in list:
            if l.text == 'Новая категория веб-сайтов':
                return l.text

    def click_on_statistik_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Статистика"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_BUTTON)).click()

    def get_statistic_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.STATISTIC_INFORMATION_WEBSITE))
        return text.text

    def get_current_data(self):# Получение текущей даты
        current_date = datetime.datetime.now().strftime('%d.%m.%Y')
        return current_date
    def get_error_text_host(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.ERROR_TEXT_HOST))
        return text.text
    def click_on_cancel_button(self):
        with allure.step('В правом фрейме нажать на кнопку "Отменить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CANCEL_BUTTON)).click()
    def click_on_confirm_cancel_button(self):
        with allure.step('В модальном окне нажать на кнопку "Отменить изменения"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_CANCEL_BUTTON)).click()

    def delete_button_click(self):
        with allure.step('В правом фрейме внизу нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.DELETE_BUTTON)).click()

    def click_confirm_delete_button(self):
        with allure.step('В модальном окне нажать на кнопку "Удалить"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CONFIRM_DELETE_BUTTON)).click()
    def get_text_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.INFORMATION_MESSAGE))
        return text.text
    def get_changing_information(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.CHANGING_INFORMATION_CATEGORIES))
        return text.text
    def click_on_history_button(self):
        with allure.step('В разделе "Статистика" под строкой "История изменений" нажать на кнопку "дата"'):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_BUTTON)).click()

    def get_history_categorie_name(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CATEGORIE_NAME))
        return text.text
    def get_history_data(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.HISTORY_CHANGING_INFORMATION))
        data = text.text.split(' ')
        return data[1]
    def click_on_checkbox_update_days(self):
        with allure.step('В правом фрейме в строке "Обновлять категории сайтов автоматически" выбрать данный чек бокс '):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHECK_BOX_UPDATE_DAYS)).click()
    def get_default_days(self):
        value = self.wait(self.driver).until(EC.visibility_of_element_located(self.DEFAULT_DAYS)).get_attribute('value')
        return int(value)
    def get_count_categories(self):
        value = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_CATEGORIES)).text
        return int(value)
    def get_count_sites(self):
        value = self.wait(self.driver).until(EC.visibility_of_element_located(self.COUNT_SITES)).text
        return int(value)
    def visability_icon(self):
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.ICON))