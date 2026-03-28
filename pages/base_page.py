import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException


class BasePage:
    """Базовый класс для всех page object"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
    
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
    
    @allure.step('Кликаем на элемент: {locator}')
    def click_element(self, locator):
        """Клик по элементу с обработкой перекрытия"""
        try:
            element = self.wait.until(EC.element_to_be_clickable((locator[0], locator[1])))
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element.click()
        except ElementClickInterceptedException:
            # Если элемент перекрыт, пробуем кликнуть через JavaScript
            element = self.find_element(locator)
            self.driver.execute_script("arguments[0].click();", element)
    
    @allure.step('Заполняем поле: {locator} значением: {text}')
    def send_keys(self, locator, text):
        """Заполнение поля"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    @allure.step('Получаем текст элемента: {locator}')
    def get_text(self, locator):
        """Получение текста элемента"""
        return self.find_element(locator).text
    
    @allure.step('Скроллим к элементу: {locator}')
    def scroll_to_element(self, locator):
        """Скролл к элементу"""
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
