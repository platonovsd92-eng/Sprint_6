import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    """Page Object главной страницы"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Закрываем cookie-баннер, если он есть')
    def close_cookie_banner(self):
        """Закрытие баннера с cookie, если он мешает"""
        try:
            cookie_button = self.driver.find_element(By.XPATH, "//button[text()='да все привыкли']")
            if cookie_button.is_displayed():
                cookie_button.click()
        except:
            pass
    
    @allure.step('Нажимаем на кнопку "Заказать" вверху страницы')
    def click_order_button_top(self):
        self.close_cookie_banner()
        buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
        if buttons:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[0])
            buttons[0].click()
    
    @allure.step('Нажимаем на кнопку "Заказать" внизу страницы')
    def click_order_button_bottom(self):
        self.close_cookie_banner()
        buttons = self.driver.find_elements(By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")
        if len(buttons) > 1:
            # Скроллим к нижней кнопке
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[1])
            # Ждем, пока кнопка станет кликабельной
            self.wait.until(EC.element_to_be_clickable(buttons[1]))
            buttons[1].click()
        elif buttons:
            buttons[0].click()
    
    @allure.step('Кликаем на вопрос: {question_index}')
    def click_question(self, question_index):
        """Клик по вопросу с указанным индексом"""
        self.close_cookie_banner()
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
        self.close_cookie_banner()
        self.click_element(MainPageLocators.SCOOTER_LOGO)
    
    @allure.step('Кликаем на логотип "Яндекс"')
    def click_yandex_logo(self):
        self.close_cookie_banner()
        self.click_element(MainPageLocators.YANDEX_LOGO)
        