from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
import allure


class Schedule(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    SCHEDULE_BUTTON = ('xpath', '//div[@class="b-left-frame-tree__section-main"]//span[text()="Расписание"]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    START_TIME_FILED = ('xpath', '//div[@class="b-frame-detail__item b-frame-detail__item_time"]//div[@class="b-schedule__item b-schedule__item_right-position"][1]//input')
    END_TIME_FIELD = ('xpath', '//div[@class="b-frame-detail__item b-frame-detail__item_time"]//div[@class="b-schedule__item b-schedule__item_right-position"][2]//input')
    SAVE_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@type=\'button\']/span[text()=\' Сохранить \']')
    FAST_SEARCH = ('xpath', '//input[@class=\'b-fast-search__input form-control\']')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class=\'c-pencil-edit__icon-edit fas fa-pencil-alt\']')
    EDIT_NAME_FIELD = ('xpath', '//input[@placeholder=\'Введите имя\']')
    STATISTICS = ('xpath', '//a[text()=\'Статистика\']')
    BASICS = ('xpath', '//a[text()=\'Основное\']')
    LAST_CHANGE = ('xpath', '//button[@class=\'b-frame-detail__history-date b-button btn-link\']')
    LIST_OBJECT_DB = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\']')
    GET_NAME_OBJECT = ('xpath', '//div[@class=\'ag-center-cols-clipper\']//div[@role=\'row\'][last()]//span[@class=\'truncate-block\']/span[@class=\'truncate-block__name\']')
    DESCRIPTION_FIELD = ('xpath', '//input[@validatefieldname=\'Описание\']')
    GET_DESCRIPTION = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][8]//div[@class="b-change-modal__item--value text-truncate"]/span')
    DROPDOWN_BUTTON = ('xpath', '//button[@class="btn z-dropdown btn-no-variant b-button btn-no-variant c-select__button"]')
    DROPDOWN_DAILY = ('xpath', '//div[@class="c-dropdown-new__list"]//span[text()=" Ежедневно "]')
    DROPDOWN_WEEKLY = ('xpath', '//div[@class="c-dropdown-new__list"]//span[text()=" Еженедельно "]')
    DROPDOWN_MONTHLY = ('xpath', '//div[@class="c-dropdown-new__list"]//span[text()=" Ежемесячно "]')
    DROPDOWN_ANNUALLY = ('xpath', '//div[@class="c-dropdown-new__list"]//span[text()=" Ежегодно "]')
    DROPDOWN_PERIOD = ('xpath', '//div[@class="c-dropdown-new__list"]//span[text()=" Период "]')
    GET_PERIODICITY = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][9]//div[@class="b-change-modal__item--value text-truncate"]/span')
    CLOSE_MODAL_LAST_CHANGE = ('xpath', '//span[text()=" Закрыть "]')
    DAYS = ('xpath', '//div[@class="b-frame-detail__item m-t-10"]//button[1]')
    DAYS_OF_THE_WEEK = ('xpath', '//div[@class="b-frame-detail__item m-t-10"]//button[2]')
    ITEM_1 = ('xpath', '//div[@class="b-schedule__days"]//button[1]')
    ITEM_15 = ('xpath', '//div[@class="b-schedule__days"]//button[15]')
    ITEM_31 = ('xpath', '//div[@class="b-schedule__days"]//button[31]')
    GET_DAYS_OF_MONTH = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][4]//div[@class="b-change-modal__item--value text-truncate"]/span')
    MONDAY = ('xpath', '//div[@class="b-schedule__item"]/button[1]')
    THURSDAY = ('xpath', '//div[@class="b-schedule__item"]/button[4]')
    SUNDAY = ('xpath', '//div[@class="b-schedule__item"]/button[7]')
    GET_DAYS_OF_THE_WEEK = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][5]//div[@class="b-change-modal__item--value text-truncate"]/span')
    JANUARY = ('xpath', '//span[text()=" Январь "]/..')
    JUNE = ('xpath', '//span[text()=" Июнь "]/..')
    DECEMBER = ('xpath', '//span[text()=" Декабрь "]/..')
    GET_MONTH_OF_YEAR = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][6]//div[@class="b-change-modal__item--value text-truncate"]/span')
    TIME_START = ('xpath', '//div[@class="b-schedule__item b-schedule__item_small-r-indent b-schedule__item_time"]/div[1]//input')
    TIME_END = ('xpath', '//div[@class="b-schedule__item b-schedule__item_small-r-indent b-schedule__item_time"]/div[2]//input')
    DELETE_OBJECT = ('xpath', '//div[@class=\'b-frame-detail__footer-controls\']/i')
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class=\'text-truncate\'][text()=\' Удалить \']')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()=\'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.\']')


    def object_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def schedule_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SCHEDULE_BUTTON))

    def start_time_filed(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.START_TIME_FILED))

    def end_time_filed(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.END_TIME_FIELD))

    def save_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def fast_search(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.FAST_SEARCH))

    def add_new_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def open_object(self):
        list = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT_DB))
        return list[-1]

    def pencil_edit_icon(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def edit_name_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EDIT_NAME_FIELD))

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.STATISTICS))

    def last_change(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def dropdown_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_BUTTON))

    def dropdown_daily(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_DAILY))

    def dropdown_weekly(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_WEEKLY))

    def dropdown_monthly(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_MONTHLY))

    def dropdown_annually(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_ANNUALLY))

    def dropdown_period(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DROPDOWN_PERIOD))

    def get_periodicity(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_PERIODICITY))
        return text.text

    def basics(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.BASICS))

    def close_modal_last_change(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.CLOSE_MODAL_LAST_CHANGE))

    def days(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DAYS))

    def item_1(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ITEM_1))

    def item_15(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ITEM_15))

    def item_31(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ITEM_31))

    def get_days_of_month(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DAYS_OF_MONTH))
        return text.text

    def monday(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.MONDAY))

    def thursday(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.THURSDAY))

    def sunday(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SUNDAY))

    def days_of_the_week(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DAYS_OF_THE_WEEK))

    def get_days_of_the_week(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DAYS_OF_THE_WEEK))
        return text.text

    def january(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.JANUARY))

    def june(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.JUNE))

    def december(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DECEMBER))

    def get_month_of_year(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_MONTH_OF_YEAR))
        return text.text

    def input_time_start(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.TIME_START))

    def input_time_end(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.TIME_END))

    def delete_object(self):
        with allure.step('Нажать на иконку "Удаление объекта"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_OBJECT))

    def accept_delete_object(self):
        with allure.step('Нажать на кнопку подтверждения "Удаления объекта"'):
            return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT))

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text