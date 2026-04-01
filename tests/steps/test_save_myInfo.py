import time

from pytest_bdd import scenarios, given, then

from utils.scenario_util import save_myInfo
scenarios('../features/HRM_Save_MyInfo.feature')


@then('Save My Info')
def save_my_info(driver):
    save_myInfo(driver)
