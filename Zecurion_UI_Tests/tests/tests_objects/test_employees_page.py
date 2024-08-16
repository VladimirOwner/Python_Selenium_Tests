import time
from pages.login_page import LoginPage
from pages.Objects.employees import Employees
import allure


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()
    
    
@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Создание объекта подразделения')
def test_create_object_division(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    employees.dropdown_employees().click()
    employees.subdivision_button().click()
    employees.add_new_object().click()
    employees.save_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новое подразделение"'):
        employees.fast_search_field().send_keys('Новое подразделение')
    with allure.step('Проверка создания нового подразделения через основной фрейм'):
        assert employees.get_name_object() == 'Новое подразделение'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Изменение имени подразделения')
def test_edit_name_division(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новое подразделение"'):
        employees.fast_search_field().send_keys('Новое подразделение')
    employees.open_object().click()
    employees.pencil_edit_icon().click()
    with allure.step('Ввести новое имя объекта "selenium_test_edit_subdivision_name"'):
        employees.edit_name_object().send_keys('selenium_test_edit_subdivision_name')
    employees.save_button().click()
    with allure.step('Очистить строку быстрого поиска'):
        employees.fast_search_field().clear()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_subdivision_name"'):
        employees.fast_search_field().send_keys('selenium_test_edit_subdivision_name')
    with allure.step('Проверка изменения имени подразделения на новое'):
        assert employees.get_name_object() == 'selenium_test_edit_subdivision_name'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Изменение поля "Описание"')
def test_change_description_of_division(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_subdivision_name"'):
        employees.fast_search_field().send_keys('selenium_test_edit_subdivision_name')
    employees.open_object().click()
    with allure.step('Ввести описание объекта "selenium_test_edit_subdivision_description"'):
        employees.description_field().send_keys('selenium_test_edit_subdivision_description')
    employees.save_button().click()
    employees.statistics().click()
    employees.last_change().click()
    with allure.step('Проверка добавления описания объекта'):
        assert employees.get_description() == 'selenium_test_edit_subdivision_description'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Добавление сотрудника в подразделение')  # Изменить тест, заменить подразделение на сотрудника
def test_add_in_division(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    employees.dropdown_employees().click()
    employees.subdivision_button().click()
    employees.add_new_object().click()
    employees.pencil_edit_icon().click()
    employees.edit_name_object().send_keys('selenium_test_edit_subdivision_name_2')
    employees.save_button().click()
    employees.fast_search_field().send_keys('selenium_test_edit_subdivision_name')
    time.sleep(2)
    employees.open_object().click()
    employees.add_division_to_object().click()
    employees.modal_fast_search_field().send_keys('selenium_test_edit_subdivision_name_2')
    time.sleep(1)
    employees.modal_object_name().click()
    time.sleep(1)
    employees.modal_apply_button().click()
    employees.save_button().click()
    employees.statistics().click()
    employees.last_change().click()
    assert employees.get_division() == 'selenium_test_edit_subdivision_name_2'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Создание объекта сотрудник')
def test_create_employee(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    employees.dropdown_employees().click()
    employees.employees_button().click()
    employees.add_new_object().click()
    with allure.step('Ввести логин'):
        employees.input_login().send_keys('test_login')
    with allure.step('Ввести пароль'):
        employees.input_pass().send_keys('password')
    employees.save_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый сотрудник"'):
        employees.fast_search_field().send_keys('Новый сотрудник')
    with allure.step('Проверка создания нового сотрудника через основной фрейм'):
        assert employees.get_name_object() == 'Новый сотрудник'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Изменение имени сотрудника')
def test_change_name_of_employee(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "Новый сотрудник"'):
        employees.fast_search_field().send_keys('Новый сотрудник')
    employees.open_object().click()
    employees.pencil_edit_icon().click()
    with allure.step('Ввести новое имя объекта "New_test_employee"'):
        employees.edit_name_object().send_keys('New_test_employee')
    employees.save_button().click()
    with allure.step('Очистить строку быстрого поиска'):
        employees.fast_search_field().clear()
    employees.dropdown_employees().click()
    employees.subdivision_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    with allure.step('Проверка изменения имени сотрудника на новое'):
        assert employees.get_name_object() == 'New_test_employee'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Изменение полей во вкладке "Основное"')
def test_change_employee_fields(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    with allure.step('Ввести в строке описания "Test description"'):
        employees.description_field().send_keys('Test description')
    with allure.step('Ввести в строке Допустимые IP-адреса "192.168.1.160"'):
        employees.ip_field().send_keys('192.168.1.160')
    with allure.step('Ввести в строке E-mail для уведомлений "stanislav.vorobyev@zecurion.com"'):
        employees.email_field().send_keys('stanislav.vorobyev@zecurion.com')
    employees.save_button().click()
    employees.statistics().click()
    employees.last_change().click()
    with allure.step('Проверка добавления описания объекта'):
        assert employees.get_employee_description() == 'Test description'
    with allure.step('Проверка добавления "E-mail для уведомлений" объекта'):
        assert employees.get_employee_email() == 'stanislav.vorobyev@zecurion.com'
    with allure.step('Проверка добавления "Допустимые IP-адреса" объекта'):
        assert employees.get_employee_ip() == '192.168.1.160'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Изменение поля "Квоты"')
def test_quotas_field(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.quotas_dropdown().click()
    with allure.step('Нажать в выборе дропдауна "Ежедневно"'):
        employees.quotas_dropdown_everyday().click()
    employees.quotas_dropdown().click()
    with allure.step('Нажать в выборе дропдауна "Еженедельно"'):
        employees.quotas_dropdown_every_week().click()
    employees.quotas_dropdown().click()
    with allure.step('Нажать в выборе дропдауна "Ежемесячно"'):
        employees.quotas_dropdown_every_month().click()
    with allure.step('Ввести в поле "Разрешенный размер, МБ" значение "5"'):
        employees.quotas_allowed_size_field().send_keys('5')
    employees.save_button().click()
    employees.statistics().click()
    employees.last_change().click()
    with allure.step('Проверка изменения значения поля "Разрешенный размер, МБ"'):
        assert employees.get_employee_allowed_size() == '5'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Валидация поля "Квоты"')
def test_validation_quotas_field(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    with allure.step('Очистить поле "Разрешенный размер, МБ"'):
        employees.quotas_allowed_size_field().clear()
    employees.save_button().click()
    with allure.step('Проверка валидации поля "Разрешенный размер, МБ" на обязательность заполнения'):
        assert employees.get_err_empty_field() == 'Разрешенный размер, МБ - обязательно для заполнения'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Работаспособность кнопок "Заблокирован", "Выслать на почту ссылку-приглашение", "Установить пароль при следующем входе"')
def test_block_employee_notification(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.block_employee_button().click()
    employees.email_notification_button().click()
    employees.change_pass_in_next_login_button().click()
    with allure.step('Проверка работоспособности кнопки "Заблокировать"'):
        assert employees.get_block_time_employee() == 'Заблокирован ' + employees.get_current_data()
    with allure.step('Проверка работоспособности кнопки "Выслать на почту ссылку-пришлашение"'):
        assert employees.get_email_notification_time() == 'Приглашение отправлено ' + employees.get_current_data()
    with allure.step('Проверка работоспособности кнопки "Изменить пароль при следующем входе"'):
        assert employees.get_change_pass_time() == 'Запрос на установку пароля создан ' + employees.get_current_data()


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Проверка отображения сообщений "Обязательно для заполнения" в модальном окне изменения пароля')
def test_empty_change_pass_fields(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.change_pass_button().click()
    with allure.step('(Заглушка) клик на модальнео окно'):
        employees.title_modal().click()
    with allure.step('Проверка валидации пустого поля "Текущий пароль"'):
        assert employees.get_empty_current_pass() == 'обязательно для заполнения'
    with allure.step('Проверка валидации пустого поля "Новый пароль'):
        assert employees.get_empty_new_pass() == 'обязательно для заполнения'
    with allure.step('Проверка валидации пустого поля "Подветрждение пароля"'):
        assert employees.get_empty_confirm_pass() == 'обязательно для заполнения'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Отображение сообщения "Текущий пароль не совпадает" в модальном окне изменения пароля')
def test_current_pass_incorrect(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.change_pass_button().click()
    with allure.step('Ввести невалидный пароль в поле "Текущий пароль"'):
        employees.input_current_password().send_keys('123')
    with allure.step('Ввести валидный новый пароль в поле "Новый пароль"'):
        employees.input_new_password().send_keys('p@ssw0rd')
    with allure.step('Ввести валидный новый пароль в поле "Подтверждение пароля"'):
        employees.input_password_confirm().send_keys('p@ssw0rd')
    employees.save_new_password_button().click()
    with allure.step('Проверка валидации поля "Текущий пароль" с невалидным значением'):
        assert employees.get_err_current_pass() == 'Текущий пароль не совпадает'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Отображение сообщения "Пароли не совпадают" в модальном окне изменения пароля')
def test_passwords_not_match(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.change_pass_button().click()
    with allure.step('Ввести валидное значение значение в поле "Текущий пароль'):
        employees.input_current_password().send_keys('password')
    with allure.step('Ввести новый пароль в поле "Новый пароль"'):
        employees.input_new_password().send_keys('p@ssw0rd')
    with allure.step('Ввести пароль отличающийся от поля "Новый пароль"'):
        employees.input_password_confirm().send_keys('p@ssword')
    with allure.step('(Заглушка) клик на модальнео окно'):
        employees.title_modal().click()
    with allure.step('Проверка отображения сообщения "Пароли не совпадают"'):
        assert employees.get_password_not_match() == 'Пароли не совпадают'


# def test_password_save(driver):
#     login(driver)
#     employees = Employees(driver)
#     employees.object_button().click()
#     employees.fast_search_field().send_keys('New_test_employee')
#     employees.open_object().click()
#     employees.change_pass_button().click()
#     employees.input_current_password().send_keys('password')
#     employees.input_new_password().send_keys('p@ssw0rd')
#     employees.input_password_confirm().send_keys('p@ssw0rd')
#     employees.save_new_password_button().click()


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Удаление объекта сотрудник')
def test_delete_employee(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "New_test_employee"'):
        employees.fast_search_field().send_keys('New_test_employee')
    employees.open_object().click()
    employees.delete_object().click()
    employees.accept_delete_object().click()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert employees.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'


@allure.feature('Объекты')
@allure.story('Сотрудники')
@allure.title('Удаление объекта подразделение')
def test_delete_division(driver):
    login(driver)
    employees = Employees(driver)
    employees.object_button().click()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_subdivision_name_2"'):
        employees.fast_search_field().send_keys('selenium_test_edit_subdivision_name_2')
    time.sleep(1)
    employees.open_object().click()
    employees.delete_object().click()
    employees.accept_delete_object().click()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert employees.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
    employees.fast_search_field().clear()
    with allure.step('Ввести в строке быстрого поиска "selenium_test_edit_subdivision_name"'):
        employees.fast_search_field().send_keys('selenium_test_edit_subdivision_name')
    time.sleep(1)
    employees.open_object().click()
    employees.delete_object().click()
    employees.accept_delete_object().click()
    with allure.step('Проверка отсутствия удаленного объекта'):
        assert employees.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
