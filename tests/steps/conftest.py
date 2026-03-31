# conftest.py
import pytest
from pytest_bdd import given
from utils.scenario_util import scenario_login
@given('login to HRM application')
def open_browser(driver, config):
    scenario_login(driver, config)
