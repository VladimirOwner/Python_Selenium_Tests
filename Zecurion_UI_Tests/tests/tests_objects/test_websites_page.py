import time
from pages.login_page import LoginPage
from pages.Objects.websites_page import WebsitesPage
import allure

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Создание объекта категории')
def test_create_webcategories(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_on_add_button()
    websites_page.click_on_save_button()
    with allure.step('В строке быстрого поиска ввести название созданной категории ("Новая категория веб-сайтов")'):
        websites_page.input_fast_search().send_keys('Новая категория веб-сайтов')
    websites_page.categorie_in_main_frame()
    with allure.step('Проверка создания объекта категории в основном фрейме'):
        assert websites_page.get_name_object() == 'Новая категория веб-сайтов'

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Создание объекта веб-сайта в созданной категории')
def test_create_website(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    websites_page.click_on_add_button_website()
    with allure.step('В поле "Хост" ввести доменное имя сайта например введем (lenta.ru)'):
        websites_page.host_input().send_keys('lenta.ru')
    websites_page.click_on_save_button()
    websites_page.get_name_website()
    with allure.step('Проверка создания объекта веб-сайта в основном фрейме'):
        assert websites_page.get_name_website() == 'Новый веб-сайт'

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Изменение названия объекта веб-сайта')
def test_update_website(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    with allure.step('В основном фрейме выбрать созданный объект веб-сайта'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_pencil_button()
    with allure.step('В поле изменения названия объекта сайта ввести любое название, например "Сайт"'):
        websites_page.input_pencil().send_keys('Сайт')
    websites_page.click_on_save_button()
    with allure.step('Проверка изменения имени объекта веб-сайта'):
        assert websites_page.get_name_website() == 'Сайт'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Дата создания объекта веб-сайта в разделе "Статистика"')
def test_check_data_create_website(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    with allure.step('В основном фрейме выбрать созданный объект веб-сайта'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_statistik_button()
    with allure.step('Проверка даты создания объекта веб-сайта'):
        assert websites_page.get_statistic_information() == websites_page.get_current_data()
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Обязательность заполенеия поля "Хост"')
def test_obligatory_to_fill_input_host(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    websites_page.click_on_add_button_website()
    websites_page.click_on_save_button()
    with allure.step('Проверка появления модального окна с ошибкой об обязательности заполнения поля "Хост"'):
        assert websites_page.get_error_text_host() == 'Хост - обязательно для заполнения'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Проверка работы кнопки "Проверить сайт"')
def test_check_website_in_categorie(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_on_check_website()
    with allure.step('В модальном окне в поле "Хост или URL" ввести доменное имя сайта, в нашем случай "lenta.ru"'):
        websites_page.input_check_website().send_keys('lenta.ru')
    websites_page.click_check_button()
    with allure.step('Проверка появления сайта в созданной категории'):
        assert  websites_page.list_category() == 'Новая категория веб-сайтов'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Удаление объекта веб-сайта в созданной категории')
def test_delete_website_object(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    with allure.step('В основном фрейме выбрать созданный объект веб-сайта'):
        websites_page.categorie_in_main_frame().click()
    websites_page.delete_button_click()
    websites_page.click_confirm_delete_button()
    with allure.step('Проверка удаления объекта веб-сайта'):
        assert websites_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Изменение названия объекта категории')
def test_update_category(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    with allure.step('В строке быстрого поиска ввести название созданной категории ("Новая категория веб-сайтов")'):
        websites_page.input_fast_search().send_keys('Новая категория веб-сайтов')
    websites_page.categorie_in_main_frame().click()
    websites_page.click_on_pencil_button()
    with allure.step('В поле изменения названия объекта категории ввести любое название, например "Категория"'):
        websites_page.input_pencil().send_keys('Категория')
    websites_page.click_on_save_button()
    websites_page.click_on_delete_fast_search_information()
    with allure.step('В строке быстрого поиска ввести название измененной категории ("Категория")'):
        websites_page.input_fast_search().send_keys('Категория')
    with allure.step('В строке быстрого поиска ввести название измененной категории ("Категория")'):
        assert websites_page.get_name_object() == 'Категория'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Отмена изменений в категории')
def test_cancel_changing(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_pencil_button()
    with allure.step('В поле изменения названия объекта категории ввести любое название, например "Категория страшных фильмов"'):
        websites_page.input_pencil().send_keys('Категория страшных фильмов')
    websites_page.click_on_cancel_button()
    websites_page.click_on_confirm_cancel_button()
    with allure.step('Проверка отмены изменений'):
        assert websites_page.get_name_object() == 'Категория'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Дата изменения объекта категории в разделе "Статистика"')
def test_get_changing_information(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_statistik_button()
    with allure.step('Проверка даты изменения объекта категории'):
        assert websites_page.get_changing_information() == websites_page.get_current_data()
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Проверка "Истории изменений" в разделе "Статистика"')
def test_click_on_history_changing_button(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_statistik_button()
    websites_page.click_on_history_button()
    with allure.step('Проверка изменении имени и даты в модальном окне "Истории изменений"'):
        assert websites_page.get_name_object() == websites_page.get_history_categorie_name() and websites_page.get_history_data() == websites_page.get_current_data()
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Удаление объекта категории')
def test_delete_object_categorie(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.delete_button_click()
    websites_page.click_confirm_delete_button()
    with allure.step('Проверка удаления объекта категории'):
        assert websites_page.get_text_information() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Проверка выбора чек бокса обновления категорий сайтов автоматически')
def test_click_checkbox_update_days(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    websites_page.click_on_checkbox_update_days()
    with allure.step('Чек бокс выбирается, в поле "Период обновления,дни" появляется цифра 5'):
        assert websites_page.get_default_days() == 5

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Проверка изменения количества категорий в правом фрейме')
def test_check_count_categories(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    with allure.step('Сохраняем число категорий до создания нового объекта'):
        count = websites_page.get_count_categories()
    websites_page.click_on_add_button()
    websites_page.click_on_save_button()
    websites_page.click_on_websites_button()
    with allure.step('Проверка количества категорий в правом фрейме после создания объекта'):
        assert websites_page.get_count_categories() == count+1

@allure.feature("Объекты")
@allure.story("Веб сайты - URL")
@allure.title('Проверка изменения количества сайтов в правом фрейме')
def test_check_count_sites(driver):
    login_page = LoginPage(driver)
    websites_page = WebsitesPage(driver)
    login_page.login()
    websites_page.click_on_object_button()
    websites_page.click_on_websites_button()
    count = websites_page.get_count_sites()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    with allure.step('В основном фрейме выбрать созданную категорию'):
        websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    websites_page.click_on_add_button_website()
    with allure.step('В поле "Хост" ввести доменное имя сайта например введем (lenta.ru)'):
        websites_page.host_input().send_keys('lenta.ru')
    websites_page.click_on_save_button()
    websites_page.visability_icon()
    websites_page.click_on_websites_button()
    with allure.step('Проверка количества сайтов в правом фрейме после создания сайта'):
        assert websites_page.get_count_sites() == count+1
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    websites_page.categorie_in_main_frame().click()
    websites_page.click_on_category_button()
    websites_page.categorie_in_main_frame().click()
    websites_page.delete_button_click()
    websites_page.click_confirm_delete_button()
    websites_page.click_on_websites_button()
    websites_page.click_filter_header()
    websites_page.click_checkbox_authtor()
    websites_page.click_on_check_filter()
    websites_page.categorie_in_main_frame().click()
    websites_page.delete_button_click()
    websites_page.click_confirm_delete_button()