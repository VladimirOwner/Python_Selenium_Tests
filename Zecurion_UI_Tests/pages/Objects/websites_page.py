from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class WebsitesPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//section[@class=\'ps-container b-scroll-area b-super-menu__nav-container b-super-menu-favorites__list ps ps--theme_default\']/li[@class=\'b-super-menu-favorites__item\']//span[text()=\'Объекты\']')
    WEBSITES_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name\']//span[text()=\'Веб-сайты — URL\']')
    UPDATE_WEBSITES_BUTTON = ('xpath', '//span[text()=\' Обновить категории сайтов ZECURION \']')
    ADD_BUTTON = ('xpath', '//button[@class=\'btn btn-no-variant b-button btn-no-variant\']/i')
    SAVE_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' Сохранить \']')
    LIST_CATEGORIES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    IN_CATEGORY_BUTTON = ('xpath', '//button[@type=\'button\']/span[text()=\' В категорию \']')
    ADD_BUTTON_WEBSITE = ('xpath', '//div[@class=\'b-frame-main__buttons\']')
    HOST_INPUT = ('xpath', '//div[@class=\'col\']/input[@placeholder=\'Введите хост\']')
    LIST_WEBSITES_ON_MAIN_FRAME = ('xpath', '//div[@class=\'ag-center-cols-container\']/div')
    WEB_CATEGORIES_STATISTIC_BUTTON = ('xpath', '//a[text()=\'Статистика\']')





