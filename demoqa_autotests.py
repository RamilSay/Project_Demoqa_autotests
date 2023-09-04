import os
from selene import browser, be, have



def testing_DemoQA():
#Values for testing
    name = "Vasya"
    last_name = "Filin"
    e_mail = "fortest@gmail.com"
    mobile = "9995557777"
    address = "1-street, 7-house, 7-apartment"
    state = "NCR"
    city = "Delhi"

    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("name")
    browser.element("#lastName").type("last_name")
    browser.element("#userEmail").type("e_mail")
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").type("mobile")

#date of birth
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(".react-datepicker__month-select [value='6']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(".react-datepicker__year-select [value='1999']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--007").click()

#subjects & hobbies
    browser.element("#subjectsInput").type("math").press_enter()
    browser.element("#subjectsInput").type("Physics").press_enter()
    browser.element("[for='hobbies-checkbox-1']").click()
    browser.element("[for='hobbies-checkbox-3']").click()
    browser.element("#uploadPicture").send_keys(os.path.abspath("/IMG_1.jpg"))

#Adress
    browser.element("#currentAddress").type("adress")
    browser.element("#react-select-3-input").type("state").press_enter()
    browser.element("#react-select-4-input").type("city").press_enter()
    browser.element("#submit").press_enter()

#asserts
    browser.element(".form").should(have.text("VASYA"))
    browser.element(".form").should(have.text("last_name"))





