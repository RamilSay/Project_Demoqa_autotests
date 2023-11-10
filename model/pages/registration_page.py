import os

from selene import browser, have, command

import tests


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.mobile = browser.element('#userNumber')
        self.subject_ = browser.element("#subjectsInput")
        self.hobbies_check = browser.all('.custom-checkbox')
        self.picture = browser.element("#uploadPicture")
        self.address = browser.element("#currentAddress")

    def open(self):
        browser.open('/automation-practice-form')

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

    def type_subject(self, values):
        for subject in values:
            self.subject_.type(subject).press_enter()

    def set_hobbies(self, values):
        for hobby in values:
            self.hobbies_check.element_by(have.exact_texts(hobby)).click()

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element(f".react-datepicker__year-select > option[value='{year}']").click()
        browser.element(f".react-datepicker__month-select > option[value='{month - 1}']").click()
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

    def register(self, student):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.email(student.email)
        self.set_gender(student.gender)
        self.mobile(student.mobile)
        self.fill_date_of_birth(student.birth_date.strftime('%Y'),
                                student.birth_date.strftime('%m'),
                                student.birth_date.strftime('%d')
                                )
        self.upload_picture(student.upload_filename)
        self.fill_address(student.address)
        self.fill_state(student.state)
        self.fill_city(student.city)
        self.submit()


    def should_registered_user(self, student):
        browser.element('.table').all('td').even.should(
            have.exact_texts(
                f'{student}'
            )
        )





    @property
    def registered_user_data(self):
        return


registration_page = RegistrationPage()
