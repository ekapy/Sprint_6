from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure


class MainPage(BasePage):

    _QUESTION_1_LOCATOR = (By.ID, 'accordion__heading-0')
    _QUESTION_2_LOCATOR = (By.ID, 'accordion__heading-1')
    _QUESTION_3_LOCATOR = (By.ID, 'accordion__heading-2')
    _QUESTION_4_LOCATOR = (By.ID, 'accordion__heading-3')
    _QUESTION_5_LOCATOR = (By.ID, 'accordion__heading-4')
    _QUESTION_6_LOCATOR = (By.ID, 'accordion__heading-5')
    _QUESTION_7_LOCATOR = (By.ID, 'accordion__heading-6')
    _QUESTION_8_LOCATOR = (By.ID, 'accordion__heading-7')

    _ANSWER_1_LOCATOR = (By.ID, 'accordion__panel-0')
    _ANSWER_2_LOCATOR = (By.ID, 'accordion__panel-1')
    _ANSWER_3_LOCATOR = (By.ID, 'accordion__panel-2')
    _ANSWER_4_LOCATOR = (By.ID, 'accordion__panel-3')
    _ANSWER_5_LOCATOR = (By.ID, 'accordion__panel-4')
    _ANSWER_6_LOCATOR = (By.ID, 'accordion__panel-5')
    _ANSWER_7_LOCATOR = (By.ID, 'accordion__panel-6')
    _ANSWER_8_LOCATOR = (By.ID, 'accordion__panel-7')

    _TEXT_ANSWER_1_LOCATOR = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    _TEXT_ANSWER_2_LOCATOR = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    _TEXT_ANSWER_3_LOCATOR = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    _TEXT_ANSWER_4_LOCATOR = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    _TEXT_ANSWER_5_LOCATOR = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    _TEXT_ANSWER_6_LOCATOR = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    _TEXT_ANSWER_7_LOCATOR = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    _TEXT_ANSWER_8_LOCATOR = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

    _LOGO_SCOOTER_LOCATOR = (By.XPATH, '//img[@alt="Scooter"]')
    _LOGO_YANDEX_LOCATOR = (By.XPATH, '//a[@href="//yandex.ru"]')
    _LOGO_DZEN_LOCATOR = (By.XPATH, '//a[@class="desktop-base-header__logoLink-aE"]')

    ORDER_BUTTON_ON_HEADER = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    ORDER_BUTTON_ON_PAGE = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]')

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ожидание лого Самоката и клик по нему')
    def wait_and_click_logo_scooter(self):
        self.wait_and_click_element(self._LOGO_SCOOTER_LOCATOR)

    @allure.step('Ожидание лого Яндекс и клик по нему')
    def click_logo_yandex(self):
        self.wait_and_click_element(self._LOGO_YANDEX_LOCATOR)
        self.switch()
        self.find_element(self._LOGO_DZEN_LOCATOR)















