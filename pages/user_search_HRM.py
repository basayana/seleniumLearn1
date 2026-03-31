import time

from selenium.webdriver.support.select import Select

from pages.basePage import basePage
from selenium.webdriver.common.by import By

class UserSearchHRM(basePage):
    def __init__(self, driver):
        super().__init__(driver)
    _ADMIN_SEARCH = (By.XPATH, "//a//span[normalize-space()='Admin']")
    _USER_DROPDOWN = (By.XPATH, "//label[normalize-space()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//div[@class='oxd-select-text-input']")
    _ESS_DROPDOWN  = (By.XPATH, "//label[normalize-space()='User Role']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//span[normalize-space()='ESS']")
    def select_admin_user_type(self):
        self.wait_and_click(self._ADMIN_SEARCH)
        self.wait_and_click(self._USER_DROPDOWN)
        self.wait_and_click(self._ESS_DROPDOWN)
        time.sleep(10)