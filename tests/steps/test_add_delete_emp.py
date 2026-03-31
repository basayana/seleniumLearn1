from pytest_bdd import scenarios, given, then
from utils.scenario_util import add_emp_scenario, delete_emp_scenario, scenario_login

scenarios('../features/HRM_Add_Emps.feature')

@given('login to HRM application')
def open_browser(driver, config):
    scenario_login(driver, config)

@given('add employee')
def add_emp(driver):
    add_emp_scenario(driver)

@then('delete employee')
def delete_emp(driver):
    delete_emp_scenario(driver)