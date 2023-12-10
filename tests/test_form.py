import allure
from allure_commons.types import Severity
from model.data.user import user
from model.pages.registration_page import registration_page


@allure.title('Успешное заполнение формы')
@allure.severity(Severity.CRITICAL)
@allure.feature('Раздел Practice Form')
@allure.story('Пользователь заполняет форму регистрации тестовыми данными')
def test_fill_form(browser_setup):
    registration_page.open()

    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.should_registered_user(user)
