# import time
# import allure
import time
from pages.login_page import LoginPage
from pages.Objects.schedule import Schedule
from faker import Faker
fake = Faker()


def login(driver):
    login_page = LoginPage(driver)
    login_page.login()


def test_create_schedule_object(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.add_new_object().click()
    schedule.start_time_filed().send_keys('00:00')
    schedule.end_time_filed().send_keys('23:59')
    schedule.save_object().click()
    assert schedule.get_name_object() == 'Новое расписание'


def test_edit_name_object(driver):
    random_name = fake.word()
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.pencil_edit_icon().click()
    schedule.edit_name_field().send_keys(random_name)
    schedule.save_object().click()
    assert schedule.get_name_object() == random_name


def test_change_description(driver):
    random_name = fake.word()
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.description_field().send_keys(random_name)
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_description() == random_name


# def test_dropdown_daily(driver):
#     login(driver)
#     schedule = Schedule(driver)
#     schedule.object_button().click()
#     schedule.schedule_button().click()
#     schedule.object().click()
#     schedule.dropdown_button().click()
#     schedule.dropdown_daily().click()
#     schedule.save_object().click()
#     schedule.statistics().click()
#     schedule.last_change().click()
#     assert schedule.get_periodicity() == 'Ежедневно'
#
#
# def test_dropdown_weekly(driver):
#     login(driver)
#     schedule = Schedule(driver)
#     schedule.object_button().click()
#     schedule.schedule_button().click()
#     schedule.object().click()
#     schedule.dropdown_button().click()
#     schedule.dropdown_weekly().click()
#     schedule.save_object().click()
#     schedule.statistics().click()
#     schedule.last_change().click()
#     assert schedule.get_periodicity() == 'Еженедельно'
#
# def test_dropdown_monthly(driver):
#     login(driver)
#     schedule = Schedule(driver)
#     schedule.object_button().click()
#     schedule.schedule_button().click()
#     schedule.object().click()
#     schedule.dropdown_button().click()
#     schedule.dropdown_monthly().click()
#     schedule.save_object().click()
#     schedule.statistics().click()
#     schedule.last_change().click()
#     assert schedule.get_periodicity() == 'Ежемесячно'
#
# def test_dropdown_annualy(driver):
#     login(driver)
#     schedule = Schedule(driver)
#     schedule.object_button().click()
#     schedule.schedule_button().click()
#     schedule.object().click()
#     schedule.dropdown_button().click()
#     schedule.dropdown_annually().click()
#     schedule.save_object().click()
#     schedule.statistics().click()
#     schedule.last_change().click()
#     assert schedule.get_periodicity() == 'Ежегодно'
#
#
# def test_dropdown_period(driver):
#     login(driver)
#     schedule = Schedule(driver)
#     schedule.object_button().click()
#     schedule.schedule_button().click()
#     schedule.object().click()
#     schedule.dropdown_button().click()
#     schedule.dropdown_period().click()
#     schedule.save_object().click()
#     schedule.statistics().click()
#     schedule.last_change().click()
#     assert schedule.get_periodicity() == 'Период'
#

def test_dropdown(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.dropdown_button().click()
    schedule.dropdown_daily().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_periodicity() == 'Ежедневно'
    schedule.close_modal_last_change().click()
    schedule.basics().click()
    schedule.dropdown_button().click()
    schedule.dropdown_weekly().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_periodicity() == 'Еженедельно'
    schedule.close_modal_last_change().click()
    schedule.basics().click()
    schedule.dropdown_button().click()
    schedule.dropdown_monthly().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_periodicity() == 'Ежемесячно'
    schedule.close_modal_last_change().click()
    schedule.basics().click()
    schedule.dropdown_button().click()
    schedule.dropdown_annually().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_periodicity() == 'Ежегодно'
    schedule.close_modal_last_change().click()
    schedule.basics().click()
    schedule.dropdown_button().click()
    schedule.dropdown_period().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_periodicity() == 'Период'


def test_schedule_items(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.dropdown_button().click()
    schedule.dropdown_annually().click()
    schedule.days().click()
    schedule.item_15().click()
    schedule.item_1().click()
    schedule.item_31().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_days_of_month() == '15, 31'


def test_schedule_days(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.dropdown_button().click()
    schedule.dropdown_annually().click()
    schedule.days_of_the_week().click()
    schedule.thursday().click()
    schedule.monday().click()
    schedule.sunday().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_days_of_the_week() == 'Чт, Вс'


def test_schedule_months(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.dropdown_button().click()
    schedule.dropdown_annually().click()
    schedule.days_of_the_week().click()
    schedule.june().click()
    schedule.january().click()
    schedule.december().click()
    schedule.save_object().click()
    schedule.statistics().click()
    schedule.last_change().click()
    assert schedule.get_month_of_year() == 'Июнь, Декабрь'


def test_delete_object(driver):
    login(driver)
    schedule = Schedule(driver)
    schedule.object_button().click()
    schedule.schedule_button().click()
    schedule.open_object().click()
    schedule.delete_object().click()
    schedule.accept_delete_object().click()
    assert schedule.get_no_rows_overlay() == 'По вашему запросу ничего не найдено, попробуйте изменить условия поиска.'
