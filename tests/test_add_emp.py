import time

from utils.scenario_util import scenario_login, delete_emp_scenario, add_emp_scenario


def test_add_emp(driver, config):
    scenario_login(driver, config)
    add_emp_scenario(driver)
    delete_emp_scenario(driver)
