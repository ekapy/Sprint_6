import pytest
from pages.main_page import MainPage
from selenium.webdriver.common.by import By
from config import url
import allure


class TestMainPage:

    list_of_questions = [
        [MainPage._QUESTION_1_LOCATOR, MainPage._ANSWER_1_LOCATOR, MainPage._TEXT_ANSWER_1_LOCATOR],
        [MainPage._QUESTION_2_LOCATOR, MainPage._ANSWER_2_LOCATOR, MainPage._TEXT_ANSWER_2_LOCATOR],
        [MainPage._QUESTION_3_LOCATOR, MainPage._ANSWER_3_LOCATOR, MainPage._TEXT_ANSWER_3_LOCATOR],
        [MainPage._QUESTION_4_LOCATOR, MainPage._ANSWER_4_LOCATOR, MainPage._TEXT_ANSWER_4_LOCATOR],
        [MainPage._QUESTION_5_LOCATOR, MainPage._ANSWER_5_LOCATOR, MainPage._TEXT_ANSWER_5_LOCATOR],
        [MainPage._QUESTION_6_LOCATOR, MainPage._ANSWER_6_LOCATOR, MainPage._TEXT_ANSWER_6_LOCATOR],
        [MainPage._QUESTION_7_LOCATOR, MainPage._ANSWER_7_LOCATOR, MainPage._TEXT_ANSWER_7_LOCATOR],
        [MainPage._QUESTION_8_LOCATOR, MainPage._ANSWER_8_LOCATOR, MainPage._TEXT_ANSWER_8_LOCATOR]
    ]

    @allure.title('Вопросы о важном. Проверка соответствия текста ответов на вопросы ')
    @pytest.mark.parametrize('question, answer, answer_text', list_of_questions)
    def test_accordion_button(self, driver, question, answer, answer_text):
        accordion = MainPage(driver)
        accordion.navigate(url)
        accordion.scroll_to_element(question)
        accordion.wait_and_click_element(question)

        assert accordion.get_text(answer) == answer_text

    @allure.title('Проверка перехода на главную по лого Самокат')
    def test_from_logo_scooter_to_main_page(self, driver):
        logo_scooter = MainPage(driver)
        logo_scooter.navigate(url)
        logo_scooter.wait_and_click_logo_scooter()

        assert driver.current_url == url

    @allure.title('Проверка перехода на Дзен с лого Яндекса')
    def test_from_logo_yandex_redirect_to_dzen(self, driver):
        logo_yandex = MainPage(driver)
        logo_yandex.navigate(url)
        logo_yandex.click_logo_yandex()

        assert 'dzen.ru' in driver.current_url











