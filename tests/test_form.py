from model.pages.registration_page import registration_page
from selene import have


def test_fill_form():
    registration_page.open()

    # WHEN
    registration_page.



     fill_first_name('Natali'))
    registration_page.fill_last_name('Ivanova')
    registration_page.fill_email('fortest@gmail.com')

    registration_page.gender_female.click()

    registration_page.mobile.type('9995557777')

    registration_page.fill_date_of_birth('2000', '10', '01')

    registration_page.subject.type('Maths').press_enter().type('Physics').press_enter()

    registration_page.hobbie_sport.click()
    registration_page.hobbie_music.click()

    registration_page.upload_picture('IMG_1.jpg')

    registration_page.fill_address('1-street, 7-house, 7-apartment')

    registration_page.fill_state('NCR')

    registration_page.submit()

    # THEN
    registration_page.registered_user_data.should(
        have.exact_texts(

    )
