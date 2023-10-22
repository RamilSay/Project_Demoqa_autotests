import os

from selene import browser, have


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender_female = browser.all('[name=gender]').element_by(have.value('Female')).element('..')
        self.mobile = browser.element('#userNumber')
        self.subject = browser.element("#subjectsInput")
        self.hobbie_sport = browser.element("[for='hobbies-checkbox-1']")
        self.hobbie_music = browser.element("[for='hobbies-checkbox-3']")
        self.picture = browser.element("#uploadPicture")

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self,value):
        self.email.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').type(year)
        browser.element('.react-datepicker__month-select').type(month)
        browser.element(
            f'.react-datepicker__day--0{day}:not(.react-datepicker__day--outside-month)'
        ).click()

    def upload_picture(self):
        self.picture.send_keys(os.path.abspath("resource/IMG_1.jpg"))