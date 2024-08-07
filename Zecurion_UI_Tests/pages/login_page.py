from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC
import allure
class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    USER_FIELD = ('xpath', '//input[@placeholder=\'введите логин\']')
    PASSWORD_FIELD = ('xpath', '//input[@placeholder=\'введите пароль\']')
    BUTTON = ('xpath', '//button[@type=\'button\']')
    ERROR_MESSEGE = ('xpath', '//div[text()=\' Неверный логин или пароль \']')
    EMPTY_USER_FIELD_TEXT = ('xpath', '//div[@class=\'col\']/div[1]/div[text()=\'обязательно для заполнения\']')
    EMPTY_PASSWORD_FIELD_TEXT = ('xpath', '//div[@class=\'col\']/div[2]/div[text()=\'обязательно для заполнения\']')

    def open(self): # Открытие страницы Zecurion
        with allure.step('Открытие страницы портала'):
            self.driver.get('http://192.168.1.39:1297/')

    def user_field(self): # Получение элемента поля "Пользователь"
        return self.driver.find_element(*self.USER_FIELD)


    def password_field(self): # Получение элемента поля "Пароль"
        return self.driver.find_element(*self.PASSWORD_FIELD)

    def button_click(self): # Получение элемента и клик на кнопку "Войти"
        self.driver.find_element(*self.BUTTON).click()

    def get_error_text(self): # Получение текста при неправильном вводе пользователя или пароля
        text = self.wait(self.driver).until(EC.visibility_of_element_located(self.ERROR_MESSEGE))
        return text.text

    def get_empty_user_field_text(self): # Получение элемента текста под полем "Пользователь"
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.EMPTY_USER_FIELD_TEXT))

    # Получение элемента текста под полем "Пароль"
    def get_empty_password_field_text(self): # Получение элемента текста под полем "Пользователь"
        return self.wait(self.driver).until(EC.visibility_of_element_located(self.EMPTY_PASSWORD_FIELD_TEXT))
    with allure.step('Открытие страницы портала и успешная авторизация'):
        def login(self):
            self.open()
            with allure.step('Успешная авторизация'):
                self.user_field().send_keys('admin')
                self.password_field().send_keys('admin')
                self.button_click()
