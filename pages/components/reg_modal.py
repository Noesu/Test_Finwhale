from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC


class RegModalComponent:
    MODAL_WEB_ELEMENT = (By.CLASS_NAME, "tab-modal")
    COMPANY_INN = (By.ID, "company_inn")
    COMPANY_INN_SUGGESTION = (By.CLASS_NAME, "input-search__option")
    COMPANY_INN_SUGGESTIONS_LIST = (By.CLASS_NAME, "input-search__options")
    SAME_ADDRESS_CHECKBOX = (By.XPATH, "//div[@class='checkbox__item']//span")
    COMPANY_SEGMENT = (By.ID, "segment")
    COMPANY_SEGMENT_SUGGESTIONS = (By.XPATH, "//div[@class = 'select__options']/label")
    USER_LAST_NAME = (By.ID, "last_name")
    USER_FIRST_NAME = (By.ID, "first_name")
    USER_MIDDLE_NAME = (By.ID, "sur_name")
    USER_PHONE = (By.ID, "phone")
    USER_EMAIL = (By.ID, "email")
    USER_CURATOR = (By.XPATH, "//div[@id='curator']//div[contains(@class,'select__result_wrap')]")
    USER_CURATOR_SUGGESTIONS = (By.XPATH, "//div[@id = 'curator']//label")
    NO_SALES_MANAGER_CHECKBOX = (By.XPATH, "//input[@id = 'agreementMember']/following-sibling::span")
    EMAIL_NOTIFICATION_CHECKBOX = (By.XPATH, "//input[@id = 'notificationMember']/following-sibling::span")
    ACCEPT_PRIVACY_CHECKBOX = (By.XPATH, "//input[@id = 'privacy']/following-sibling::span")
    REG_SUBMIT_BUTTON = (By.XPATH, "//div[contains(@class, 'tab-modal__content_button')]/button")

    def __init__(self, driver, wait) -> None:
        self.driver = driver
        self.wait = wait

    def _is_inn_suggestions_list_closed(self):
        try:
            return self.wait.until(EC.invisibility_of_element_located(self.COMPANY_INN_SUGGESTIONS_LIST))
        except TimeoutException:
            return False

    def _is_segment_suggestions_list_closed(self):
        try:
            return self.wait.until(EC.invisibility_of_element_located(self.COMPANY_SEGMENT_SUGGESTIONS))
        except TimeoutException:
            return False

    def _is_curator_suggestions_list_closed(self):
        try:
            return self.wait.until(EC.invisibility_of_element_located(self.USER_CURATOR_SUGGESTIONS))
        except TimeoutException:
            return False

    def wait_until_modal_is_visible(self):
        return self.wait.until(EC.visibility_of_element_located(self.MODAL_WEB_ELEMENT))

    def select_company_inn(self, company_inn: str):
        company_inn_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.COMPANY_INN))
        company_inn_field.send_keys(company_inn)
        company_suggestion: WebElement = self.wait.until(EC.element_to_be_clickable(self.COMPANY_INN_SUGGESTION))
        company_suggestion.click()
        assert self._is_inn_suggestions_list_closed(), "INN suggestions list did not close after selection"

    def check_same_address_checkbox(self):
        same_address_checkbox: WebElement = self.wait.until(EC.element_to_be_clickable(self.SAME_ADDRESS_CHECKBOX))
        same_address_checkbox.click()

    def select_company_segment(self, segment: str):
        company_segment_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.COMPANY_SEGMENT))
        company_segment_field.click()
        company_segment_suggestions_list: list[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self.COMPANY_SEGMENT_SUGGESTIONS))
        for segment_option in company_segment_suggestions_list:
            if segment_option.get_attribute("value") == segment:
                segment_option.click()
                break
        assert self._is_segment_suggestions_list_closed(), "Segment suggestions list did not close after selection"

    def set_last_name(self, last_name):
        last_name_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_LAST_NAME))
        last_name_field.send_keys(last_name)

    def set_first_name(self, first_name):
        first_name_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_FIRST_NAME))
        first_name_field.send_keys(first_name)

    def set_middle_name(self, middle_name):
        middle_name_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_MIDDLE_NAME))
        middle_name_field.send_keys(middle_name)

    def set_phone(self, phone):
        phone_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_PHONE))
        phone_field.send_keys(phone)

    def set_email(self, email):
        email_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_EMAIL))
        email_field.send_keys(email)

    def select_company_curator(self, curator: str):
        curator_field: WebElement = self.wait.until(EC.element_to_be_clickable(self.USER_CURATOR))
        curator_field.click()
        curator_suggestions_list: list[WebElement] = self.wait.until(
            EC.presence_of_all_elements_located(self.USER_CURATOR_SUGGESTIONS))
        for curator_option in curator_suggestions_list:
            if curator_option.get_attribute("value") == curator:
                curator_option.click()
                break
        assert self._is_curator_suggestions_list_closed(), "Curator suggestions list did not close after selection"

    def check_no_sales_manager_checkbox(self):
        no_sales_manager_checkbox: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.NO_SALES_MANAGER_CHECKBOX))
        no_sales_manager_checkbox.click()

    def check_email_notification_checkbox(self):
        email_notification_checkbox: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.EMAIL_NOTIFICATION_CHECKBOX))
        email_notification_checkbox.click()

    def check_accept_privacy_checkbox(self):
        accept_privacy_checkbox: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.ACCEPT_PRIVACY_CHECKBOX))
        accept_privacy_checkbox.click()

    def submit_registration(self):
        button: WebElement = self.wait.until(EC.element_to_be_clickable(self.REG_SUBMIT_BUTTON))
        button.click()
