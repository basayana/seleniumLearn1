import time

from pages.signin_HRM import OrangeHRM
from pages.user_search_HRM import UserSearchHRM
from utils.excel_util import get_credentials_from_excel


def scenario_login(driver, config):
    creds = get_credentials_from_excel('tests/testdata/HRM.xlsx', 'Login')[0]# Get first row
    userid = creds['userid']
    password = creds['password']
    signin_page = OrangeHRM(driver)
    signin_page.fill_signin_submit(config, userid, password)
    print('Login successful with user: {}'.format(userid))
    time.sleep(10)

def scenario_admin_search(driver):
    admin_page = UserSearchHRM(driver)
    admin_page.select_admin_user_type()