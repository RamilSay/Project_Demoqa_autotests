from pages.registration_page import RegistrationPage
from selene import have


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # WHEN
    registration_page.fill_first_name('Natali')
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
    registration_page.fill_city('Delhi')

    registration_page.submit()

    # THEN
    registration_page.registered_user_data.should(
        have.exact_texts(
            'Natali Ivanova',
            'fortest@gmail.com',
            'Female',
            '9995557777',
            '01 November,2000',
            'Maths, Physics',
            'Sports, Music',
            'IMG_1.jpg',
            '1-street, 7-house, 7-apartment',
            'NCR Delhi')
    )
