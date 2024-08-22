from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as ec
#  import allure


class Services(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class="b-super-menu-list__wrap"]/div[@class="b-super-menu-list__link"]//span[text()="Объекты"]')
    SERVICES_BUTTON = ('xpath', '//span[@class="b-left-frame-tree__title-name b-left-frame-tree__title-name_single"]//span[text()="Сервисы"]')
    ADD_NEW_OBJECT = ('xpath', '//div[@class="b-frame-main__buttons"]//button[@type="button"]')
    GET_NAME_OBJECT = ('xpath', '//div[@class="ag-center-cols-clipper"]//div[@role="row"][last()]//span[@class="truncate-block"]/span[@class="truncate-block__name"]')
    SAVE_BUTTON = ('xpath', '//span[text()=" Сохранить "]/..')
    PORTS_FIELD = ('xpath', '//input[@placeholder="Введите порт"]')
    LIST_OBJECT_DB = ('xpath', '//div[@class="ag-center-cols-clipper"]//div[@role="row"]')
    PENCIL_EDIT_ICON = ('xpath', '//span[@class="c-pencil-edit__icon-edit fas fa-pencil-alt"]')
    EDIT_NAME_FIELD = ('xpath', '//input[@placeholder="Введите имя"]')
    DESCRIPTION_FIELD = ('xpath', '//input[@validatefieldname="Описание"]')
    STATISTICS = ('xpath', '//a[text()="Статистика"]')
    LAST_CHANGE = ('xpath', '//button[@class="b-frame-detail__history-date b-button btn-link"]')
    GET_DESCRIPTION = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][2]//div[@class="b-change-modal__item--value text-truncate"]/span')
    GET_PORTS = ('xpath', '//div[@class="modal-body__inner-container"]//div[@class="b-change-modal__content--old"][3]//div[@class="b-change-modal__item--value text-truncate"]/span')
    GET_VALIDATE_ERR = ('xpath', '/html/body/div[4]/div[1]/div/div/div/div/div/div[2]/div[2]/span')
    DELETE_OBJECT = ('xpath', '//div[@class="b-frame-detail__footer-controls"]/i')
    ACCEPT_DELETE_OBJECT = ('xpath', '//span[@class="text-truncate"][text()=" Удалить "]')
    NO_ROWS_OVERLAY = ('xpath', '//span[text()="По вашему запросу ничего не найдено, попробуйте изменить условия поиска."]')

    def object_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.OBJECT_BUTTON))

    def services_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SERVICES_BUTTON))

    def add_new_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ADD_NEW_OBJECT))

    def save_button(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.SAVE_BUTTON))

    def ports_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.PORTS_FIELD))

    def get_name_object(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_NAME_OBJECT))
        return text.text

    def object(self):
        list_object = self.wait(self.driver).until(ec.visibility_of_all_elements_located(self.LIST_OBJECT_DB))
        return list_object[-1]

    def pencil_edit_icon(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.PENCIL_EDIT_ICON))

    def edit_name_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.EDIT_NAME_FIELD))

    def description_field(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DESCRIPTION_FIELD))

    def statistics(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.STATISTICS))

    def last_change(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.LAST_CHANGE))

    def get_description(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_DESCRIPTION))
        return text.text

    def get_ports(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_PORTS))
        return text.text

    def get_ports_err_validate(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.GET_VALIDATE_ERR))
        return text.text

    def delete_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.DELETE_OBJECT))

    def accept_delete_object(self):
        return self.wait(self.driver).until(ec.visibility_of_element_located(self.ACCEPT_DELETE_OBJECT))

    def get_no_rows_overlay(self):
        text = self.wait(self.driver).until(ec.visibility_of_element_located(self.NO_ROWS_OVERLAY))
        return text.text