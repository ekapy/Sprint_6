from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.main_page import MainPage
import allure




class OrderPage(BasePage):

    _NAME_LOCATOR = (By.XPATH, '//input[@placeholder="* Имя"]')
    _SURNAME_LOCATOR = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    _ADDRESS_LOCATOR = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    _METRO_LOCATOR = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    _METRO_VALUE = (By.XPATH, '//li[@data-value="1"]')
    _TELEPHONE_LOCATOR = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    _NEXT_STEP_BUTTON_LOCATOR = (By.XPATH, '//button[contains(text(),"Далее")]')
    _TITLE_LOCATOR = (By.XPATH, '//div[contains(@class,"Order_Header")]')
    _CALENDAR_FIELD_LOCATOR = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    _PERIOD_FIELD_LOCATOR = (By.XPATH, '//div[@class="Dropdown-control"]')
    _PERIOD_SELECTION_LOCATOR = (By.XPATH, '//div[contains(text(),"сутки")]')
    _COLOR_SELECTION_LOCATOR = (By.XPATH, '//input[@id="grey"]')
    _ORDER_BUTTON_LOCATOR = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')
    _CONFIRM_BUTTON_YES_LOCATOR = (By.XPATH, '//button[contains (text(),"Да")]')
    _ORDER_POPUP_SUCCESS_LOCATOR = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    _ORDER_POPUP_BUTTON = (By.XPATH, '//button[contains (text(),"Посмотреть статус")]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('f"Ввод имени {name}"')
    def enter_name(self, name):
        self.enter_text(self._NAME_LOCATOR, name)

    @allure.step('f"Ввод фамилии {surname}"')
    def enter_surname(self, surname):
        self.enter_text(self._SURNAME_LOCATOR, surname)

    @allure.step('Выбор станции метро')
    def metro_station_selection(self):
        self.click_element(self._METRO_LOCATOR)
        self.click_element(self._METRO_VALUE)

    @allure.step('f"Ввод номера телефона {telephone}"')
    def enter_telephone(self, telephone):
        self.enter_text(self._TELEPHONE_LOCATOR, telephone)

    @allure.step('Клик по кнопке Далее')
    def next_button_click(self):
        self.click_element(self._NEXT_STEP_BUTTON_LOCATOR)

    @allure.step('Ввод даты')
    def enter_calendar_data(self, calendar_data):
        self.enter_text(self._CALENDAR_FIELD_LOCATOR, calendar_data)
        self.click_element(self._TITLE_LOCATOR)

    @allure.step('Выбор срока аренды')
    def period_selection(self):
        self.click_element(self._PERIOD_FIELD_LOCATOR)
        self.click_element(self._PERIOD_SELECTION_LOCATOR)

    @allure.step('Выбор цвета самоката')
    def color_selection(self):
        self.click_element(self._COLOR_SELECTION_LOCATOR)

    @allure.step('Клик по кнопке Заказать')
    def order_button_click(self):
        self.click_element(self._ORDER_BUTTON_LOCATOR)

    @allure.step('Подтверждение заказа, клик на Да')
    def order_confirm_yes(self):
        self.click_element(self._CONFIRM_BUTTON_YES_LOCATOR)

    @allure.step('Наличие попапа об успешном заказе')
    def order_success_popup(self):
       if self.find_element(self._ORDER_POPUP_SUCCESS_LOCATOR):
           return True
       else:
           return False





























