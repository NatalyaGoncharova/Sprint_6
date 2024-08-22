import pytest
from pages.page_object_main import MainPage
import allure


@allure.feature("FAQ Page")
@allure.story("Verify FAQ questions and answers")
class TestFAQPage:
    @pytest.mark.parametrize("question_index, expected_answer",
                             [(0, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
                              (1,
                               "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
                              (2,
                               "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
                              (3, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
                              (4,
                               "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
                              (5,
                               "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
                              (6,
                               "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
                              (7, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
                              ])
    def test_questions_answers_open(self, driver, question_index, expected_answer):
        main_page = MainPage(driver)

        with allure.step("Confirming cookie"):
            main_page.confirm_cookie()

        with allure.step(f"Opening question {question_index}"):
            main_page.open_question(question_index)

        with allure.step(f"Getting answer for question {question_index}"):
            answer_faq = main_page.get_answer(question_index)

        with allure.step("Verifying the answer"):
            assert answer_faq == expected_answer
