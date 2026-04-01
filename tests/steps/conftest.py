# conftest.py
import pytest
from pytest_bdd import given
from utils.scenario_util import scenario_login
@given('login to HRM application')
def open_browser(driver, config):
    scenario_login(driver, config)

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    print(f"Executing step: {step.name}")

def pytest_bdd_after_scenario(request, feature, scenario):
    print(f"Completed step: {scenario.name}")
