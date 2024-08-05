from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class WebsitesPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    WEBSITES_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name\']//span[text()=\'Веб-сайты — URL\']')
    UPDATE_WEBSITES_BUTTON = ('xpath', '//span[text()=\' Обновить категории сайтов ZECURION \']')
    INFORMATION_lAST_UPDATE = ('xpath', '//div[@class=\'b-objects-root-detail-websites__update\']/span')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']/i')
    PENCIL_BUTTON = ('xpath', '//span[@class=\'c-pencil-edit__icon\']')
    INPUT_PENCIL_FIELD = ('xpath', '//div[@class=\'b-form-group form-group required-field c-pencil-edit__input vf-field-dirty vf-field-valid vf-field-touched\']')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    LIST_CATEGORIES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    IN_CATEGORY_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' В категорию \']')
    ADD_BUTTON_WEBSITE = ('xpath', '//div[@class=\'b-frame-main__buttons\']')
    HOST_INPUT = ('xpath', '//div[@class=\'col\']/input[@placeholder=\'Введите хост\']')
    LIST_WEBSITES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    WEB_CATEGORIES_STATISTIC_BUTTON = ('xpath', '//a[text()=\'Статистика\']')
    STATISTIC_INFORMATION = ('xpath', '//span[text()=\'Создано\']/../span[@class=\'b-frame-detail__stats-value d-flex\']/span')


    def click_on_object_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()

    def click_on_websites_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.WEBSITES_BUTTON)).click()

    def click_on_update_websites_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.UPDATE_WEBSITES_BUTTON)).click()

    def click_on_add_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()

    def click_on_save_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()



