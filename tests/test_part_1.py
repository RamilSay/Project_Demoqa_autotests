from model.pages.registration_page import RegistrationPage


def test_student_registration_form():
    registration_page = RegistrationPage()
    registration_page.open()

    # Values for testing
    # hobbies = "Sports, Music"
    # address = "1-street, 7-house, 7-apartment"
    # state = "NCR"
    # city = "Delhi"

    # WHEN
    registration_page.fill_first_name('Natali')
    registration_page.fill_last_name('Ivanova')
    registration_page.fill_email('fortest@gmail.com')

    registration_page.gender_female.click()

    registration_page.mobile.type('9995557777')

    registration_page.fill_date_of_birth('2000', '7', '01')

    registration_page.subject.type('Maths').press_enter().type('Physics').press_enter()

    registration_page.hobbie_sport.click()
    registration_page.hobbie_music.click()

    registration_page.upload_picture()


    # browser.element("#currentAddress").type(address)
    # browser.element("#react-select-3-input").type(state).press_enter()
    # browser.element("#react-select-4-input").type(city).press_enter()
    # browser.element("#submit").press_enter()

    ## asserts
    # browser.element(".table").should(have.text(name))
    # browser.element(".table").should(have.text(last_name))
    # browser.element(".table").should(have.text(e_mail))
    # browser.element("#gender-radio-1").should(have.value("Male"))
    # browser.element(".table").should(have.text(mobile))
    # browser.element("#dateOfBirthInput").should(have.value("07 Jul 1999"))
    # browser.element(".table").should(have.text("Maths"))
    # browser.element(".table").should(have.text("Physics"))
    # browser.element(".table").should(have.text(hobbies))
    # browser.element(".table").should(have.text("IMG_1.jpg"))
    # browser.element(".table").should(have.text(address))
    # browser.element(".table").should(have.text(state))
    # browser.element(".table").should(have.text(city))

