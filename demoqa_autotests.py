from selene import browser


#Тестирование формы
def testing_DemoQA():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').type('Ramil')
    browser.element('#lastName').type('Sayapov')
    browser.element('#userEmail').type('ramilsayapov71@gmail.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('89995557777')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select [value="6"]').click()





