from pages.basePage import basePage
from selenium.webdriver.common.by import By

class OrangeHRM(basePage):
    def __init__(self, driver):
        super().__init__(driver)
    _USER_NAME_TEXTBOX = (By.CSS_SELECTOR, "input[placeholder='Username']")
    _PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "input[placeholder='Password']")
    _LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    def fill_signin_submit(self, config, userid, password):
        self.driver.get(config.get("DEFAULT", "base_url_hrm"))
        self.wait_for_element(self._USER_NAME_TEXTBOX)
        self.driver.find_element(*self._USER_NAME_TEXTBOX).send_keys(userid)
        self.driver.find_element(*self._PASSWORD_TEXTBOX).send_keys(password)
        self.driver.find_element(*self._LOGIN_BUTTON).click()