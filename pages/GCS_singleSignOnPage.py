from pages.basePage import basePage
from selenium.webdriver.common.by import By



class SingleSignOnPage(basePage):

    _USER_ID_TEXTBOX = (By.ID, "username")
    _PASSWORD_TEXTBOX = (By.ID, "password")
    _SIGN_ON_BUTTON = (By.ID, "signOnButton")
    def __init__(self, driver):
        super().__init__(driver)

    def fill_signin_submit(self):
        self.wait_for_element(self._USER_ID_TEXTBOX)
        self.driver.find_element(*self._USER_ID_TEXTBOX).send_keys("0143440")
        self.driver.find_element(*self._PASSWORD_TEXTBOX).send_keys("Ddddd44444$$$$$")
        self.driver.find_element(*self._SIGN_ON_BUTTON).click()


