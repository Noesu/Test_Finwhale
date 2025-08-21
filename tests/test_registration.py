import time

from config.data import Company

def test_registration(page):
    page.accept_cookies_if_present()
    page.click_registration_button()
    page.reg_modal.wait_until_modal_is_visible()
    page.reg_modal.select_company_inn(Company.INN)
    page.reg_modal.check_same_address_checkbox()
    page.reg_modal.select_company_segment(Company.SEGMENT)
    page.reg_modal.set_last_name(Company.USER_LAST_NAME)
    page.reg_modal.set_first_name(Company.USER_FIRST_NAME)
    page.reg_modal.set_middle_name(Company.USER_MIDDLE_NAME)
    page.reg_modal.set_phone(Company.USER_PHONE)
    page.reg_modal.set_email(Company.USER_EMAIL)
    page.reg_modal.select_company_curator(Company.USER_CURATOR)
    page.reg_modal.check_no_sales_manager_checkbox()
    page.reg_modal.check_email_notification_checkbox()
    page.reg_modal.check_accept_privacy_checkbox()

    page.reg_modal.submit_registration()


    time.sleep(3)


