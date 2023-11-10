from model.data.user_data import student
from model.pages.registration_page import registration_page
from selene import have


def test_fill_form():
    registration_page.open()

    # WHEN
    registration_page.register(student)

    # THEN
    registration_page.registered_user_data.should(
        have.exact_texts(

    )
