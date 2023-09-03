from selene import browser


#Тестирование формы
def testing_DemoQA():
    browser.open("https://demoqa.com/automation-practice-form")
    browser.element("#firstName").type("Vasya")
    browser.element("#lastName").type("Filin")
    browser.element("#userEmail").type("fortest@gmail.com")
    browser.element("[for='gender-radio-1']").click()
    browser.element("#userNumber").type("89995557777")
    #date
    browser.element("#dateOfBirthInput").click()
    browser.element(".react-datepicker__month-select").click()
    browser.element(".react-datepicker__month-select [value='6']").click()
    browser.element(".react-datepicker__year-select").click()
    browser.element(".react-datepicker__year-select [value='1999']").click()
    browser.element(".react-datepicker__day.react-datepicker__day--007").click()
    #hobbies
    browser.element("#subjectsInput")
    browser.element("[for='hobbies-checkbox-3']").click()






