from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class MainPage(BasePage):
    REGISTRATION_BUTTON = (By.XPATH, "//div[@class = 'banner__button']//button")
    COOKIES_BANNER = (By.CLASS_NAME, "cookies__banner")
    ACCEPT_COOKIES_BUTTON = (By.CLASS_NAME, "cookies__banner_button")

    def __init__(self, driver):
        super().__init__(driver)

    def accept_cookies_if_present(self):
        try:
            accept_cookies_button: WebElement = self.wait.until(
                EC.visibility_of_element_located(self.ACCEPT_COOKIES_BUTTON))
            accept_cookies_button.click()
            self.wait.until(EC.invisibility_of_element_located(self.COOKIES_BANNER))
        except TimeoutException:
            return

    def click_registration_button(self):
        button: WebElement = self.wait.until(EC.element_to_be_clickable(self.REGISTRATION_BUTTON))
        button.click()
