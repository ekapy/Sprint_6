from pages.order_page import OrderPage
from pages.base_page import BasePage
from pages.main_page import MainPage
from config import url
from helpers import get_order_data
import allure


class TestOrderPage:
    @allure.title('Создание заказа через кнопку в хедере')
    def test_make_order_from_header_button(self, driver):
        name, surname, address, telephone, calendar_date = get_order_data()
        order = OrderPage(driver)
        order.navigate(url)
        order.wait_and_click_element(MainPage.ORDER_BUTTON_ON_HEADER)

        order.enter_name(name)
        order.enter_surname(surname)
        order.metro_station_selection()
        order.enter_telephone(telephone)
        order.next_button_click()

        order.enter_calendar_data(calendar_date)
        order.period_selection()
        order.color_selection()
        order.order_button_click()

        order.order_confirm_yes()

        assert order.order_success_popup() == True

    @allure.title('Создание заказа через кнопку на главной странице')
    def test_make_order_from_button_on_main_page(self, driver):
        name, surname, address, telephone, calendar_date = get_order_data()
        order = OrderPage(driver)
        order.navigate(url)
        order.scroll_to_element(MainPage.ORDER_BUTTON_ON_PAGE)
        order.wait_and_click_element(MainPage.ORDER_BUTTON_ON_PAGE)

        order.enter_name(name)
        order.enter_surname(surname)
        order.metro_station_selection()
        order.enter_telephone(telephone)
        order.next_button_click()

        order.enter_calendar_data(calendar_date)
        order.period_selection()
        order.color_selection()
        order.order_button_click()

        order.order_confirm_yes()

        assert order.order_success_popup() == True























