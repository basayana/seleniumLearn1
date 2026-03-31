from pytest_bdd import scenarios, given, then
from utils.scenario_util import add_emp_scenario, delete_emp_scenario

scenarios('../features/HRM_Add_Emps.feature')


@given('add employee')
def add_emp(driver):
    add_emp_scenario(driver)

@then('delete employee')
def delete_emp(driver):
    delete_emp_scenario(driver)