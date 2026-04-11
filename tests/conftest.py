import pytest
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from data.urls import Urls


@pytest.fixture
def driver():
    """Фикстура для инициализации и закрытия драйвера"""
    # Путь к geckodriver
    current_dir = os.path.dirname(os.path.abspath(__file__))
    driver_path = os.path.join(current_dir, '..', 'drivers', 'geckodriver.exe')
    
    # Проверяем существование файла
    if not os.path.exists(driver_path):
        raise FileNotFoundError(f"geckodriver не найден по пути: {driver_path}\n"
                                f"Скачайте geckodriver с https://github.com/mozilla/geckodriver/releases\n"
                                f"и поместите в папку drivers/")
    
    print(f"✅ geckodriver найден: {driver_path}")
    
    # Настройки Firefox
    options = Options()
    
    # Указываем путь к Firefox
    firefox_path = r"C:\Program Files\Mozilla Firefox\firefox.exe"
    if os.path.exists(firefox_path):
        options.binary_location = firefox_path
        print(f"✅ Firefox найден: {firefox_path}")
    else:
        print("❌ Firefox не найден! Установите Firefox.")
        raise FileNotFoundError("Firefox не установлен")
    
    # Создаем сервис и драйвер
    service = Service(driver_path)
    driver = webdriver.Firefox(service=service, options=options)
    driver.get(Urls.MAIN_PAGE)
    driver.maximize_window()
    
    yield driver
    driver.quit()