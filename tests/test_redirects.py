import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


@allure.feature('Редиректы')
class TestRedirects:
    """Тесты для проверки редиректов по логотипам"""
    
    @allure.story('Логотип Самоката')
    @allure.title('Проверка перехода на главную страницу по клику на логотип Самоката')
    def test_scooter_logo_redirect(self, driver):
        """Проверка: при клике на логотип Самоката происходит переход на главную страницу"""
        main_page = MainPage(driver)
        
        # Переходим на страницу заказа
        main_page.click_order_button_top()
        
        # Кликаем на логотип Самоката
        main_page.click_scooter_logo()
        
        # Проверяем, что остались на главной странице
        current_url = driver.current_url
        assert current_url == 'https://qa-scooter.praktikum-services.ru/'
    
    @allure.story('Логотип Яндекса')
    @allure.title('Проверка перехода на Дзен по клику на логотип Яндекса')
    def test_yandex_logo_redirect(self, driver):
        """Проверка: при клике на логотип Яндекса в новом окне открывается Дзен"""
        main_page = MainPage(driver)
        
        # Получаем текущее окно
        original_window = driver.current_window_handle
        
        # Кликаем на логотип Яндекса
        main_page.click_yandex_logo()
        
        # Ждём открытия нового окна
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        
        # Переключаемся на новое окно
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        
        # Проверяем URL нового окна
        WebDriverWait(driver, 10).until(EC.url_contains('dzen.ru'))
        current_url = driver.current_url
        assert 'dzen.ru' in current_url
        