from selenium.webdriver.common.by import By


class OrderPageLocators:
    """Локаторы страницы заказа"""
    
    # Локаторы для первой страницы формы заказа
    NAME_FIELD = [By.XPATH, "//input[@placeholder='* Имя']"]
    SURNAME_FIELD = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    ADDRESS_FIELD = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    METRO_FIELD = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    METRO_OPTION = [By.XPATH, "//div[@class='select-search__select']//button"]
    PHONE_FIELD = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    NEXT_BUTTON = [By.XPATH, "//button[text()='Далее']"]
    
    # Локаторы для второй страницы формы заказа
    DATE_FIELD = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    RENTAL_PERIOD = [By.XPATH, "//div[contains(@class, 'Dropdown-control')]"]
    RENTAL_PERIOD_OPTIONS = [By.XPATH, "//div[contains(@class, 'Dropdown-menu')]/div"]
    COLOR_CHECKBOX_BLACK = [By.XPATH, "//label[contains(text(), 'чёрный жемчуг')]"]
    COLOR_CHECKBOX_GREY = [By.XPATH, "//label[contains(text(), 'серая безысходность')]"]
    COMMENT_FIELD = [By.XPATH, "//input[@placeholder='Комментарий для курьера']"]
    ORDER_BUTTON = [By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']"]
    CONFIRM_BUTTON = [By.XPATH, "//button[text()='Да']"]
    
    # Локатор сообщения об успешном заказе
    SUCCESS_MESSAGE = [By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and contains(text(), 'Заказ оформлен')]"]
    
    # Локатор для закрытия календаря
    BODY = [By.TAG_NAME, "body"]
    