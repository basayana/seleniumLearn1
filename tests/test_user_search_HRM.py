
from utils.scenario_util import scenario_admin_search, scenario_login


def test_login_hrm(driver, config):
    scenario_admin_search(driver)
