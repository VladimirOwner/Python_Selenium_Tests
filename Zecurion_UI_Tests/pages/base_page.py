from selenium.webdriver.support.ui import WebDriverWait


class BasePage:
    def __init__(self,driver):
        self.driver = driver

    def wait(self,driver):
        wait = WebDriverWait(driver, 30)
        return wait


