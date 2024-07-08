import allure
from pages.base_page import BasePage
from  selenium.webdriver.support import expected_conditions as EC
class HeaderPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    USER_NAME = ('xpath', '//div[text()=\' Администратор \']')
    SUPER_MENU_BUTTON = ('xpath','//button[@id=\'super-menu-toggle-button\']')
    COUNT_SECTIONS_IN_SUPER_MENU = ('xpath','//ul[@class=\'b-super-menu-list\']')
    NOTIFICATION_BUTTON = ('xpath','//button[@id=\'notifications-popup-button\']')
    NOTIFICATION_TEXT = ('xpath','//div[text()=\' Уведомления \']')
    CHANGES_BUTTON = ('xpath','//div[@class=\'b-info-bar\']/button[@class=\'b-info-bar__btn b-info-bar__btn--item\']')
    CHANGES_TEXT = ('xpath', '//span[text()=\'Изменения\']')
    FULL_DISPLAY_BUTTON = ('xpath', '//button[@class=\'b-fs-button b-info-bar__btn b-info-bar__btn--item\']')
    DISPLAY_ATTRIBUTE = ('xpath', '//button[@class=\'b-fs-button b-info-bar__btn b-info-bar__btn--item\']/i')
    EXIT_BUTTON = ('xpath','//div[@class=\'b-user-info__ico\']')
    # Имя пользователя в авторизованной системе
    def user_name_text(self):
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.USER_NAME))
        return text.text


    def click_super_menu_button(self):# Нажатие на кнопку "Супер меню"
        with allure.step('Нажатие на кнопку \'Супер меню\''):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.SUPER_MENU_BUTTON)).click()

    def get_count_sections_in_super_menu(self):# Получение количества разделов в супер меню
        count = self.wait(self.driver).until(EC.visibility_of_all_elements_located(self.COUNT_SECTIONS_IN_SUPER_MENU))
        number = len(count)
        return number

    def click_notification_button(self): # Нажатие на кнопку "Уведомления"
        with allure.step('Нажатие на кнопку \'Уведомления\''):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.NOTIFICATION_BUTTON)).click()


    def get_text_notification(self): # Получение текста "УВЕДОМЛЕНИЕ"
        notification = self.wait(self.driver).until(EC.visibility_of_element_located(self.NOTIFICATION_TEXT))
        return notification.text

    def click_on_changes_button(self): # Нажатие на кнопку "Изменения"
        with allure.step('Нажатие на кнопку \'Изменения\''):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.CHANGES_BUTTON)).click()


    def get_text_changes(self): # Получение текста "Изменения"
        changes = self.wait(self.driver).until(EC.visibility_of_element_located(self.CHANGES_TEXT))
        return changes.text


    def click_on_full_display_button(self): # Нажатие на кнопку "Полный экран"
        with allure.step('Нажатие на кнопку \'Полный экран\''):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.FULL_DISPLAY_BUTTON)).click()


    def get_display_attribute(self): # Получение атрибута в полноэкранном режиме
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.DISPLAY_ATTRIBUTE))
        text = text.get_attribute('class')
        return text


    def click_on_exit(self): # Нажатие на кнопку "Выйти"
        with allure.step('Нажатие на кнопку \'Выход\''):
            self.wait(self.driver).until(EC.visibility_of_element_located(self.EXIT_BUTTON)).click()
