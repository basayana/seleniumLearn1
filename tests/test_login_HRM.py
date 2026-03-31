import time

from pages.signin_HRM import OrangeHRM
from utils.excel_util import get_credentials_from_excel
from utils.scenario_util import scenario_login


def test_login_hrm(driver, config):
    scenario_login(driver, config)
