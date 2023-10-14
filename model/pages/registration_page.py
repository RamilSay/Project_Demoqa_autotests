from selene import browser


class RegistrationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')


    def open(self):
        browser.open('/automation-practice-form')
