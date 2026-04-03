from selenium.webdriver.common.by import By
from pages.basePage import basePage


class MyInfoPage(basePage):
    def __init__(self, driver):
        super().__init__(driver)
    _MY_INFO_LINK = (By.XPATH, "//a//span[normalize-space()='My Info']")
    _FIRST_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='First Name']")
    _MIDDLE_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Middle Name']")
    _LAST_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Last Name']")
    _SAVE_BUTTON = (By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]")
    _SAVE_CONFIRMATION_MESSAGE = (By.XPATH, "//p[normalize-space()='Successfully Updated']")
    _SPINNER_IMAGE = (By.XPATH, "//div[@class='oxd-loading-spinner-container']")

    def update_myInfo(self, firstname, middlename, lastname):
        self.wait_and_click(self._MY_INFO_LINK)
        self.wait_for_spinner(self._SPINNER_IMAGE)
        self.wait_for_element(self._FIRST_NAME_TEXTBOX)
        self.enter_text_in_textbox(self._FIRST_NAME_TEXTBOX, firstname)
        self.enter_text_in_textbox(self._MIDDLE_NAME_TEXTBOX, middlename)
        self.enter_text_in_textbox(self._LAST_NAME_TEXTBOX, lastname)
        self.driver.find_element(*self._SAVE_BUTTON).click()
        self.wait_for_element(self._SAVE_CONFIRMATION_MESSAGE)