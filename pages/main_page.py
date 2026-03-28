import allure
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from data.urls import Urls


class MainPage(BasePage):
    """Page Object главной страницы"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Закрываем cookie-баннер, если он есть')
    def close_cookie_banner(self):
        """Закрытие баннера с cookie, если он есть"""
        if self.is_element_displayed(MainPageLocators.COOKIE_BUTTON):
            self.click_element(MainPageLocators.COOKIE_BUTTON)
    
    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_order_button_top(self):
        """Клик по верхней кнопке заказа"""
        self.close_cookie_banner()
        self.click_element_by_index(MainPageLocators.ORDER_BUTTON, 0)
    
    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        """Клик по нижней кнопке заказа"""
        self.close_cookie_banner()
        self.click_element_by_index(MainPageLocators.ORDER_BUTTON, 1)
    
    @allure.step('Кликаем на вопрос: {question_index}')
    def click_question(self, question_index):
        """Клик по вопросу с указанным индексом"""
        question_locators = [
            MainPageLocators.QUESTION_1,
            MainPageLocators.QUESTION_2,
            MainPageLocators.QUESTION_3,
            MainPageLocators.QUESTION_4,
            MainPageLocators.QUESTION_5,
            MainPageLocators.QUESTION_6,
            MainPageLocators.QUESTION_7,
            MainPageLocators.QUESTION_8,
        ]
        self.scroll_to_element(question_locators[question_index])
        self.click_element(question_locators[question_index])
        
        # Ждем, пока ответ станет видимым после клика
        answer_locators = [
            MainPageLocators.ANSWER_1,
            MainPageLocators.ANSWER_2,
            MainPageLocators.ANSWER_3,
            MainPageLocators.ANSWER_4,
            MainPageLocators.ANSWER_5,
            MainPageLocators.ANSWER_6,
            MainPageLocators.ANSWER_7,
            MainPageLocators.ANSWER_8,
        ]
        self.wait.until(EC.visibility_of_element_located((answer_locators[question_index][0], answer_locators[question_index][1])))
    
    @allure.step('Получаем текст ответа на вопрос: {question_index}')
    def get_answer_text(self, question_index):
        """Получение текста ответа по индексу вопроса"""
        answer_locators = [
            MainPageLocators.ANSWER_1,
            MainPageLocators.ANSWER_2,
            MainPageLocators.ANSWER_3,
            MainPageLocators.ANSWER_4,
            MainPageLocators.ANSWER_5,
            MainPageLocators.ANSWER_6,
            MainPageLocators.ANSWER_7,
            MainPageLocators.ANSWER_8,
        ]
        return self.get_text(answer_locators[question_index])
    
    @allure.step('Кликаем на логотип "Самокат"')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step('Кликаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)
    
    @allure.step('Проверяем, что находимся на главной странице')
    def assert_on_main_page(self):
        """Проверка, что находимся на главной странице"""
        self.assert_current_url(self.urls.MAIN_PAGE)
    
    @allure.step('Кликаем на логотип Яндекса и переключаемся на новое окно')
    def click_yandex_logo_and_switch_to_new_window(self):
        """Клик по логотипу Яндекса и переключение на новое окно"""
        original_window = self.get_current_window_handle()
        self.click_yandex_logo()
        self.wait_for_number_of_windows(2)
        
        # Переключаемся на новое окно
        for window_handle in self.get_window_handles():
            if window_handle != original_window:
                self.switch_to_window(window_handle)
                break
        
        # Ждем загрузки страницы Дзена
        self.wait.until(EC.url_contains('dzen.ru'))
    
    @allure.step('Проверяем, что открыт Дзен')
    def assert_dzen_opened(self):
        """Проверка, что открыта страница Дзена"""
        self.assert_url_contains('dzen.ru')
