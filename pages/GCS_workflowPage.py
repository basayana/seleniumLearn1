from selenium.webdriver.common.by import By

from pages.basePage import basePage


class WorkflowPage(basePage):
    _REFRESH_BUTTON = (By.XPATH , "//div[@class='ag-floating-filter-button']//button[@aria-label='Open Filter Menu']")
    def __init__(self, driver):
        super().__init__(driver)
    def click_refresh_button(self):
        self.wait_and_click(self._REFRESH_BUTTON)
