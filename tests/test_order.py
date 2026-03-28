import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.order_data import OrderData


@allure.feature('Заказ самоката')
class TestOrder:
    """Тесты для сценария заказа самоката"""
    
    @allure.story('Позитивный сценарий заказа')
    @allure.title('Заказ самоката через кнопку {button_position} с данными: {order_data}')
    @pytest.mark.parametrize('button_position, order_data', [
        ('вверху страницы', OrderData.ORDER_DATA_1),
        ('внизу страницы', OrderData.ORDER_DATA_2)
    ])
    def test_successful_order(self, driver, button_position, order_data):
        """Проверка успешного создания заказа"""
        main_page = MainPage(driver)
        
        if button_position == 'вверху страницы':
            main_page.click_order_button_top()
        else:
            main_page.click_order_button_bottom()
        
        order_page = OrderPage(driver)
        order_page.fill_first_form(order_data)
        order_page.fill_second_form(order_data)
        
        assert order_page.is_order_successful()
        