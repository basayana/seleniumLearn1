import time

from selenium.webdriver.common.by import By

from pages.basePage import basePage


class AddEmp(basePage):
    def __init__(self, driver):
        super().__init__(driver)
    _PIM_SEARCH = (By.XPATH, "//a//span[normalize-space()='PIM']")
    _EMP_ADD_LINK = (By.XPATH, "//a[normalize-space()='Add Employee']")
    _FIRST_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='First Name']")
    _MIDDLE_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Middle Name']")
    _LAST_NAME_TEXTBOX = (By.XPATH, "//input[@placeholder='Last Name']")
    _SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    _SAVD_CONFIRMATION_MESSAGE = (By.XPATH, "//p[normalize-space()='Successfully Saved']")

    def add_user(self):
        self.wait_and_click(self._PIM_SEARCH)
        self.wait_and_click(self._EMP_ADD_LINK)

        self.wait_and_click(self._FIRST_NAME_TEXTBOX, timeout=20)
        self.driver.find_element(*self._FIRST_NAME_TEXTBOX).send_keys("Fname1")
        self.driver.find_element(*self._MIDDLE_NAME_TEXTBOX).send_keys("Mname1")
        self.driver.find_element(*self._LAST_NAME_TEXTBOX).send_keys("Lname1")
        self.driver.find_element(*self._SUBMIT_BUTTON).click()
        self.wait_for_element(self._SAVD_CONFIRMATION_MESSAGE)

    _EMP_LIST_LINK = (By.XPATH, "//a[normalize-space()='Employee List']")
    _EMP_NAME_TEXTBOX = (By.XPATH, "//label[normalize-space()='Employee Name']/ancestor::div[@class='oxd-input-group oxd-input-field-bottom-space']//input")
    _SEARCH_BUTTON = (By.XPATH, "//button[normalize-space()='Search']")
    _SELECT_ALL_CHECKBOX = (By.XPATH, "(//span[contains(@class, 'oxd-checkbox-input')])[1]")
    _DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='Delete Selected']")
    _CONFIRM_DELETE_BUTTON = (By.XPATH, "//button[normalize-space()='Yes, Delete']")
    _CONFIRM_DELETE_MESSAGE = (By.XPATH, "//p[normalize-space()='Successfully Deleted']")
    def delete_emp(self):
        self.wait_and_click(self._EMP_LIST_LINK)
        self.wait_for_element(self._EMP_NAME_TEXTBOX)
        self.driver.find_element(*self._EMP_NAME_TEXTBOX).send_keys("Fname1 Mname1 Lname1")
        self.driver.find_element(*self._SEARCH_BUTTON).click()
        self.wait_and_click(self._SELECT_ALL_CHECKBOX)
        self.wait_and_click(self._DELETE_BUTTON)
        self.wait_and_click(self._CONFIRM_DELETE_BUTTON)
        self.wait_for_element(self._CONFIRM_DELETE_MESSAGE)
