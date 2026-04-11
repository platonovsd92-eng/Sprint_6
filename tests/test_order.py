import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData


@allure.feature('Заказ самоката')
class TestOrder:
    """Тесты для сценария заказа самоката"""
    
    @allure.story('Позитивный сценарий заказа через верхнюю кнопку')
    @allure.title('Заказ самоката через верхнюю кнопку с данными: {order_data}')
    @pytest.mark.parametrize('order_data', [
        OrderData.ORDER_DATA_1,
        OrderData.ORDER_DATA_2
    ])
    def test_successful_order_top_button(self, driver, order_data):
        """Проверка успешного создания заказа через верхнюю кнопку"""
        main_page = MainPage(driver)
        main_page.click_order_button_top()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(order_data)
        order_page.fill_second_form(order_data)
        
        assert order_page.is_order_successful()
    
    @allure.story('Позитивный сценарий заказа через нижнюю кнопку')
    @allure.title('Заказ самоката через нижнюю кнопку с данными: {order_data}')
    @pytest.mark.parametrize('order_data', [
        OrderData.ORDER_DATA_1,
        OrderData.ORDER_DATA_2
    ])
    def test_successful_order_bottom_button(self, driver, order_data):
        """Проверка успешного создания заказа через нижнюю кнопку"""
        main_page = MainPage(driver)
        main_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(order_data)
        order_page.fill_second_form(order_data)
        
        assert order_page.is_order_successful()
        