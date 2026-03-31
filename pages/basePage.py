from selenium.common import StaleElementReferenceException
from retry import retry
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
DEFAULT_TIMEOUT = 10
SHORT_TIMEOUT = 5
LONG_TIMEOUT = 20
class basePage():
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        return self.driver.find_element(*loc)

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

    def wait_and_click(self, loc, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(loc))
        self.driver.find_element(*loc).click()

    def input_text(self, text, *loc):
        self.find_element(*loc).send_keys(text)

    @retry(StaleElementReferenceException, tries=3, delay=3)
    def wait_for_element(self, loc, timeout=DEFAULT_TIMEOUT):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(EC.element_to_be_clickable(loc))
