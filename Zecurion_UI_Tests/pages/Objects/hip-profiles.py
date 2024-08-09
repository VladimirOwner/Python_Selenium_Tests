from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

class hip_profiles(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    OBJECT_BUTTON = ('xpath', '//li/div[@class=\'b-super-menu-list__wrap\']/div[@class=\'b-super-menu-list__link\']//span[text()=\'Объекты\']')

    def click_on_object_button(self):
        self.wait(self.driver).until(EC.visibility_of_element_located(self.OBJECT_BUTTON)).click()
