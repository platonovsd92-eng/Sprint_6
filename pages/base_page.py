import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from data.urls import Urls


class BasePage:
    """Базовый класс для всех page object"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.urls = Urls
    
    @allure.step('Открываем страницу: {url}')
    def open_page(self, url):
        """Открытие страницы по URL"""
        self.driver.get(url)
    
    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        """Открытие главной страницы"""
        self.driver.get(self.urls.MAIN_PAGE)
    
    @allure.step('Находим элемент: {locator}')
    def find_element(self, locator):
        """Поиск элемента"""
        try:
            return self.wait.until(EC.presence_of_element_located((locator[0], locator[1])))
        except TimeoutException:
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name="element_not_found",
                attachment_type=allure.attachment_type.PNG
            )
            raise
    
    @allure.step('Находим все элементы: {locator}')
    def find_elements(self, locator):
        """Поиск всех элементов"""
        return self.driver.find_elements(locator[0], locator[1])
    
    @allure.step('Кликаем на элемент: {locator}')
    def click_element(self, locator):
        """Клик по элементу"""
        element = self.wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        element.click()
    
    @allure.step('Кликаем на элемент по индексу: {locator}, индекс: {index}')
    def click_element_by_index(self, locator, index):
        """Клик по элементу по индексу"""
        elements = self.wait.until(EC.presence_of_all_elements_located((locator[0], locator[1])))
        if len(elements) > index:
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elements[index])
            elements[index].click()
    
    @allure.step('Заполняем поле: {locator} значением: {text}')
    def send_keys(self, locator, text):
        """Заполнение поля"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Заполняем поле и нажимаем Enter: {locator} значением: {text}')
    def send_keys_with_enter(self, locator, text):
        """Заполнение поля и нажатие Enter"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.ENTER)
    
    @allure.step('Получаем текст элемента: {locator}')
    def get_text(self, locator):
        """Получение текста элемента"""
        return self.find_element(locator).text
    
    @allure.step('Скроллим к элементу: {locator}')
    def scroll_to_element(self, locator):
        """Скролл к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
    
    @allure.step('Проверяем, видим ли элемент: {locator}')
    def is_element_displayed(self, locator):
        """Проверка видимости элемента"""
        try:
            return self.find_element(locator).is_displayed()
        except TimeoutException:
            return False
    
    @allure.step('Закрываем cookie-баннер')
    def close_cookie_banner(self):
        """Закрытие баннера с cookie"""
        cookie_locator = [By.XPATH, "//button[text()='да все привыкли']"]
        if self.is_element_displayed(cookie_locator):
            self.click_element(cookie_locator)
    
    @allure.step('Выбираем опцию из выпадающего списка по тексту')
    def select_dropdown_option(self, dropdown_locator, option_locator, option_text):
        """Выбор опции из выпадающего списка"""
        self.click_element(dropdown_locator)
        self.wait.until(EC.visibility_of_element_located(option_locator))
        options = self.find_elements(option_locator)
        for option in options:
            if option.text == option_text:
                option.click()
                break
    
    @allure.step('Получаем текущий URL')
    def get_current_url(self):
        """Получение текущего URL страницы"""
        return self.driver.current_url
    
    @allure.step('Проверяем, что текущий URL соответствует ожидаемому')
    def assert_current_url(self, expected_url):
        """Проверка текущего URL"""
        actual_url = self.get_current_url()
        assert actual_url == expected_url, f"Ожидался URL {expected_url}, получен {actual_url}"
    
    @allure.step('Проверяем, что текущий URL содержит подстроку')
    def assert_url_contains(self, substring):
        """Проверка, что текущий URL содержит подстроку"""
        actual_url = self.get_current_url()
        assert substring in actual_url, f"URL {actual_url} не содержит {substring}"
    
    @allure.step('Получаем текущее окно')
    def get_current_window_handle(self):
        """Получение идентификатора текущего окна"""
        return self.driver.current_window_handle
    
    @allure.step('Получаем все окна')
    def get_window_handles(self):
        """Получение всех идентификаторов окон"""
        return self.driver.window_handles
    
    @allure.step('Переключаемся на окно по индексу')
    def switch_to_window(self, window_handle):
        """Переключение на окно"""
        self.driver.switch_to.window(window_handle)
    
    @allure.step('Ожидаем количество окон: {expected_count}')
    def wait_for_number_of_windows(self, expected_count):
        """Ожидание появления указанного количества окон"""
        self.wait.until(EC.number_of_windows_to_be(expected_count))
        