import allure
import pytest
from pages.main_page import MainPage
from data.urls import Urls


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
        main_page.assert_on_main_page()
    
    @allure.story('Логотип Яндекса')
    @allure.title('Проверка перехода на Дзен по клику на логотип Яндекса')
    def test_yandex_logo_redirect(self, driver):
        """Проверка: при клике на логотип Яндекса в новом окне открывается Дзен"""
        main_page = MainPage(driver)
        
        # Кликаем на логотип Яндекса и переключаемся на новое окно
        main_page.click_yandex_logo_and_switch_to_new_window()
        
        # Проверяем, что открыт Дзен
        main_page.assert_dzen_opened()