import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config import url


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу')
    def navigate(self, url):
        self.driver.get(url)

    @allure.step('Ожидание и нахождение элемента')
    def find_element(self, locator):
        WebDriverWait(self.driver,15).until(EC.presence_of_element_located(locator))
        return self.driver.find_element(*locator)


    @allure.step('Ожидание элемента и клик')
    def wait_and_click_element(self, locator):
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(locator))
        self.find_element(locator).click()

    @allure.step('Клик по элементу')
    def click_element(self, locator):
        self.find_element(locator).click()

    @allure.step('Ввод значений')
    def enter_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Получить текст')
    def get_text(self, locator):
        return self.find_element(locator).text

    @allure.step('Переключение на вкладку')
    def switch(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
    @allure.step('Скролл до элемента')
    def scroll_to_element(self, locator ):
        element = self.find_element(locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)














