from selene import browser


def testing_DemoQA():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.config.type_by_js = True
    #browser.element('#firstName').with_(click_by_js=True).click()
    browser.element("//input[@id='firstName']").type('Ramil')
    browser.element('#lastName').type('Sayapov')
    browser.element('#userEmail').type('ramilsayapov71@gmail.com')