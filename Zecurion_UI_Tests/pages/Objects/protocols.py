from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class WebsitesPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')
    PROTOCOL_BUTTON = ('xpath', '//span[@class=\'b-left-frame-tree__title-name b-left-frame-tree__title-name_single\']//span[text()=\'Протоколы\']')
    ADD_NEW_PROTOCOL = ('xpath', '//div[@class=\'b-frame-main__buttons\']//button[@type=\'button\']')
    SAVE_BUTTON = ('xpath', '//div[@class=\'b-frame-detail__footer-buttons\']/button[@type=\'button\']/span[text()=\' Сохранить \']')