import os
from selene import browser, have, command

import tests
from model.data.user_data import User, student


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
        self.address = browser.element("#currentAddress")

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, value):
        self.email.type(value)

    def set_gender(self, value):
        browser.all('[name=gender]').element_by(have.value(value)).element('..').click()

    def type_mobile(self, value):
        self.mobile.type(value)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f".react-datepicker__month-select > option[value='{month - 1}']").click()
        browser.element(f".react-datepicker__year-select > option[value='{year}']").click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def upload_picture(self, s):
        self.picture.set_value(
            os.path.abspath(
                os.path.join(os.path.dirname(tests.__file__), f'resource/IMG_1.jpg')
            )
        )

    def fill_address(self, value):
        self.address.type(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def submit(self):
        browser.element('#submit').perform(command.js.click)

    def register(self, user: User):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.email(student.email)
        self.set_gender(student.gender)
        self.mobile(student.mobile)
        self.fill_date_of_birth(student.birth_date.strftime('%Y,%m,%d'))





    @property
    def registered_user_data(self):
        return browser.element('.table').all("td").even


registration_page = RegistrationPage()
