import allure
import pytest
from pages.main_page import MainPage
from data.faq_data import FAQData


@allure.feature('Вопросы о важном')
class TestFAQ:
    """Тесты для раздела 'Вопросы о важном'"""
    
    @allure.story('Проверка ответов на вопросы')
    @allure.title('Проверка текста ответа на вопрос {question_index}')
    @pytest.mark.parametrize('question_index, expected_answer', 
        [(index, answer) for index, answer in enumerate(FAQData.ANSWERS)]
    )
    def test_faq_answers(self, driver, question_index, expected_answer):
        """Проверка, что при клике на вопрос открывается правильный ответ"""
        main_page = MainPage(driver)
        main_page.click_question(question_index)      # ← кликаем на вопрос
        actual_answer = main_page.get_answer_text(question_index)  # ← получаем текст ответа
        assert actual_answer == expected_answer