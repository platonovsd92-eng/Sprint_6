from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    
    # Кнопки заказа
    ORDER_BUTTON = [By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']"]
    
    # Вопросы в разделе "Вопросы о важном"
    QUESTION_1 = [By.ID, "accordion__heading-0"]
    QUESTION_2 = [By.ID, "accordion__heading-1"]
    QUESTION_3 = [By.ID, "accordion__heading-2"]
    QUESTION_4 = [By.ID, "accordion__heading-3"]
    QUESTION_5 = [By.ID, "accordion__heading-4"]
    QUESTION_6 = [By.ID, "accordion__heading-5"]
    QUESTION_7 = [By.ID, "accordion__heading-6"]
    QUESTION_8 = [By.ID, "accordion__heading-7"]
    
    # Ответы на вопросы
    ANSWER_1 = [By.ID, "accordion__panel-0"]
    ANSWER_2 = [By.ID, "accordion__panel-1"]
    ANSWER_3 = [By.ID, "accordion__panel-2"]
    ANSWER_4 = [By.ID, "accordion__panel-3"]
    ANSWER_5 = [By.ID, "accordion__panel-4"]
    ANSWER_6 = [By.ID, "accordion__panel-5"]
    ANSWER_7 = [By.ID, "accordion__panel-6"]
    ANSWER_8 = [By.ID, "accordion__panel-7"]
    
    # Логотипы
    SCOOTER_LOGO = [By.XPATH, "//img[@alt='Scooter']"]
    YANDEX_LOGO = [By.XPATH, "//img[@alt='Yandex']"]
    
    # Cookie-баннер
    COOKIE_BUTTON = [By.XPATH, "//button[text()='да все привыкли']"]