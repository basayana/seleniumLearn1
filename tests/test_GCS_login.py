import time
from webdriver_manager.chrome import ChromeDriverManager

from pages.GCS_signinPage import SignInPage
from pages.GCS_singleSignOnPage import SingleSignOnPage
from pages.GCS_workflowPage import WorkflowPage
from utils.pyaitoit_util import handle_pingid


def test_login(driver, base_url):

    print('Base URL: {}'.format(base_url))
    driver.get(base_url)
    # time.sleep(10)
    signin_page = SignInPage(driver)
    singleSignOn_page = SingleSignOnPage(driver)
    workflow_page = WorkflowPage(driver)
    signin_page.click_signin_link()
    assert driver.find_element(*signin_page._SIGN_IN_BUTTON).is_displayed()
    # time.sleep(5)
    signin_page.fill_signin_submit()

    singleSignOn_page.fill_signin_submit()
    handle_pingid()
    driver.get('https://contentconsole-qa.int.thomsonreuters.com/content-workflow/workflows/5756/completed-executions')
    time.sleep(20)
    workflow_page.click_refresh_button()
    time.sleep(20)

def test_chrome_options():
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium import webdriver

    options = Options()
    options.add_argument(r"user-data-dir=C:\Users\0143440\AppData\Local\Google\Chrome\User Data")
    options.add_argument("--profile-directory=Default")
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.get('https://contentconsole-qa.int.thomsonreuters.com/content-workflow/workflows/5756/completed-executions')
    time.sleep(20)