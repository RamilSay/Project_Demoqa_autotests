import os
from selene import browser, have


def testing_demoQA():
    # Values for testing
    name = "Vasya"
    last_name = "Filin"
    e_mail = "fortest@gmail.com"
    mobile = "9995557777"
    hobbies = "Sports, Music"
    address = "1-street, 7-house, 7-apartment"
    state = "NCR"
    city = "Delhi"

    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type(name)
    browser.element("#lastName").type(last_name)
    browser.element("#userEmail").type(e_mail)
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").type(mobile)

    # date of birth
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(".react-datepicker__month-select [value='6']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(".react-datepicker__year-select [value='1999']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--007").click()

    # subjects & hobbies
    browser.element("#subjectsInput").type("Maths").press_enter()
    browser.element("#subjectsInput").type("Physics").press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("/IMG_1.jpg"))

    # address
    browser.element("#currentAddress").type(address)
    browser.element("#react-select-3-input").type(state).press_enter()
    browser.element("#react-select-4-input").type(city).press_enter()
    browser.element("#submit").press_enter()

    # asserts
    browser.element(".table").should(have.text(name))
    browser.element(".table").should(have.text(last_name))
    browser.element(".table").should(have.text(e_mail))
    browser.element("#gender-radio-1").should(have.value("Male"))
    browser.element(".table").should(have.text(mobile))
    browser.element("#dateOfBirthInput").should(have.value("07 Jul 1999"))
    browser.element(".table").should(have.text("Maths"))
    browser.element(".table").should(have.text("Physics"))
    browser.element(".table").should(have.text(hobbies))
    browser.element(".table").should(have.text("IMG_1.jpg"))
    browser.element(".table").should(have.text(address))
    browser.element(".table").should(have.text(state))
    browser.element(".table").should(have.text(city))

