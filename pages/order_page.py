import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators


class OrderPage(BasePage):
    """Page Object страницы заказа"""
    
    def __init__(self, driver):
        super().__init__(driver)
    
    @allure.step('Заполняем поле "Имя": {name}')
    def set_name(self, name):
        self.send_keys(OrderPageLocators.NAME_FIELD, name)
    
    @allure.step('Заполняем поле "Фамилия": {surname}')
    def set_surname(self, surname):
        self.send_keys(OrderPageLocators.SURNAME_FIELD, surname)
    
    @allure.step('Заполняем поле "Адрес": {address}')
    def set_address(self, address):
        self.send_keys(OrderPageLocators.ADDRESS_FIELD, address)
    
    @allure.step('Выбираем станцию метро: {station}')
    def set_metro_station(self, station):
        """Ускоренный выбор станции метро"""
        # Кликаем на поле ввода метро
        metro_field = self.find_element(OrderPageLocators.METRO_FIELD)
        metro_field.click()
        time.sleep(0.2)  # уменьшено с 0.5
        
        # Вводим название станции
        metro_field.send_keys(station)
        time.sleep(0.3)  # уменьшено с 1
        
        # Ждем появления выпадающего списка и кликаем
        self.wait.until(EC.element_to_be_clickable(OrderPageLocators.METRO_OPTION))
        self.click_element(OrderPageLocators.METRO_OPTION)
        time.sleep(0.2)  # уменьшено с 0.5
    
    @allure.step('Заполняем поле "Телефон": {phone}')
    def set_phone(self, phone):
        self.send_keys(OrderPageLocators.PHONE_FIELD, phone)
    
    @allure.step('Нажимаем кнопку "Далее"')
    def click_next(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)
        time.sleep(0.5)  # уменьшено с 1
    
    @allure.step('Заполняем поле "Дата": {date}')
    def set_date(self, date):
        self.scroll_to_element(OrderPageLocators.DATE_FIELD)
        self.click_element(OrderPageLocators.DATE_FIELD)
        time.sleep(0.2)  # уменьшено с 0.5
        self.send_keys(OrderPageLocators.DATE_FIELD, date)
        time.sleep(0.2)  # уменьшено с 0.5
        self.driver.find_element(*OrderPageLocators.DATE_FIELD).send_keys(Keys.ENTER)
        time.sleep(0.2)  # уменьшено с 0.5
    
    @allure.step('Выбираем срок аренды: {days}')
    def set_rental_period(self, days):
        self.scroll_to_element(OrderPageLocators.RENTAL_PERIOD)
        time.sleep(0.2)  # уменьшено с 0.5
        self.click_element(OrderPageLocators.RENTAL_PERIOD)
        time.sleep(0.3)  # уменьшено с 1
        self.wait.until(EC.visibility_of_element_located(OrderPageLocators.RENTAL_PERIOD_OPTIONS))
        self.click_element(OrderPageLocators.RENTAL_PERIOD_OPTIONS)
        time.sleep(0.2)  # уменьшено с 0.5
    
    @allure.step('Выбираем цвет самоката: {color}')
    def set_color(self, color):
        """Выбор цвета самоката"""
        if color == 'чёрный жемчуг':
            self.scroll_to_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
            time.sleep(0.2)  # уменьшено с 0.5
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_BLACK)
        elif color == 'серая безысходность':
            self.scroll_to_element(OrderPageLocators.COLOR_CHECKBOX_GREY)
            time.sleep(0.2)  # уменьшено с 0.5
            self.click_element(OrderPageLocators.COLOR_CHECKBOX_GREY)
    
    @allure.step('Заполняем комментарий: {comment}')
    def set_comment(self, comment):
        self.send_keys(OrderPageLocators.COMMENT_FIELD, comment)
    
    @allure.step('Нажимаем кнопку "Заказать"')
    def click_order(self):
        self.scroll_to_element(OrderPageLocators.ORDER_BUTTON)
        time.sleep(0.2)  # уменьшено с 0.5
        self.click_element(OrderPageLocators.ORDER_BUTTON)
        time.sleep(0.5)  # уменьшено с 1
    
    @allure.step('Подтверждаем заказ')
    def confirm_order(self):
        try:
            confirm_button = self.wait.until(
                EC.element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
            )
            time.sleep(0.2)  # уменьшено с 0.5
            confirm_button.click()
            time.sleep(0.5)  # уменьшено с 1
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="confirm_button_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    @allure.step('Проверяем, что заказ успешно создан')
    def is_order_successful(self):
        try:
            success_message = self.wait.until(
                EC.visibility_of_element_located(OrderPageLocators.SUCCESS_MESSAGE)
            )
            return success_message is not None
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="success_message_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            return False
    
    @allure.step('Заполняем первую часть формы заказа')
    def fill_first_form(self, order_data):
        """Заполнение первой страницы формы заказа"""
        self.set_name(order_data['name'])
        self.set_surname(order_data['surname'])
        self.set_address(order_data['address'])
        self.set_metro_station(order_data['metro_station'])
        self.set_phone(order_data['phone'])
        self.click_next()
    
    @allure.step('Заполняем вторую часть формы заказа')
    def fill_second_form(self, order_data):
        """Заполнение второй страницы формы заказа"""
        self.set_date(order_data['date'])
        self.set_rental_period(order_data['rental_period'])
        self.set_color(order_data['color'])
        self.set_comment(order_data['comment'])
        self.click_order()
        self.confirm_order()