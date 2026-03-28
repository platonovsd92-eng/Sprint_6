import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера"""
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    driver.get('https://qa-scooter.praktikum-services.ru/')
    driver.maximize_window()
    yield driver
    driver.quit()