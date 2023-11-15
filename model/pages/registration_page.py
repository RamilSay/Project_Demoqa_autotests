import os
from selene import browser, have, command
from selene.core.command import js

import tests
from model.data.user import User


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.mobile = browser.element('#userNumber')
        self.subject_ = browser.element("#subjectsInput")
        self.picture = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")

    def open(self):
        browser.open('/automation-practice-form')
        return self

    def close_banner(self):
        browser.execute_script('document.querySelector("#fixedban").remove()')
        return self

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
        browser.element(f".react-datepicker__year-select > option[value='{year}']").click()
        browser.element(f".react-datepicker__month-select > option[value='{month}']").click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def type_subject(self, subject):
        self.subject_.type(subject).press_enter()

    def set_hobbies(self, hobby):
        if hobby == 'Sports':
            browser.element('[for="hobbies-checkbox-1"]').click()
        elif hobby == 'Music':
            browser.element('[for="hobbies-checkbox-3"]').click()

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
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.set_gender(user.gender)
        self.type_mobile(user.mobile)
        self.fill_date_of_birth(user.birth_date.strftime('%Y'),
                                user.birth_date.strftime('%m'),
                                user.birth_date.strftime('%d'))
        self.type_subject(user.subjects[0])
        self.type_subject(user.subjects[1])
        self.set_hobbies(user.hobbies[0])
        self.set_hobbies(user.hobbies[1])
        self.upload_picture(user.upload_filename)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)

        self.submit()

    def should_registered_user(self, user: User):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{user.first_name} {user.last_name}',
                user.email,
                user.gender,
                user.mobile,
                f'{user.birth_date.strftime("%d")}',
                f'{user.birth_date.strftime("%m")}',
                f'{user.birth_date.strftime("%Y")}',
                user.subjects,
                user.hobbies,
                user.upload_filename,
                user.address,
                f'{user.state} {user.city}'
            )
        )


registration_page = RegistrationPage()
