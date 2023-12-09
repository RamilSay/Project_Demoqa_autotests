from model.data.user import user
from model.pages.registration_page import registration_page


def test_fill_form(browser_setup):
    registration_page.open()

    # WHEN
    registration_page.register(user)

    # THEN
    registration_page.should_registered_user(user)
