from pages.basePage import basePage
from selenium.webdriver.common.by import By
class SignInPage(basePage):

    _SIGN_IN_LINK = (By.XPATH, "//a[@class='landing-sign-in-link']")
    _SIGN_IN_BUTTON = (By.XPATH, "//button[normalize-space()='Sign in']")
    _EMAIL_FIELD = (By.ID, "username")
    def __init__(self, driver):
        super().__init__(driver)

    def click_signin_link(self):
        self.wait_and_click(self._SIGN_IN_LINK)
    def fill_signin_submit(self):
        self.driver.find_element(*self._EMAIL_FIELD).send_keys("anantha.sayana@thomsonreuters.com")
        self.driver.find_element(*self._SIGN_IN_BUTTON).click()
