import time

from pytest_bdd import scenarios, given, then

from utils.scenario_util import scenario_login, scenario_admin_search
scenarios('../features/HRM_login.feature')


@then('select user role ESS')
def select_user_role_ess(driver):
    scenario_admin_search(driver)