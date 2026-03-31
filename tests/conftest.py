import pickle
import json
import os

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.options import Options
import configparser

COOKIES_FILE = "session/cookies.pkl"
LOCAL_STORAGE_FILE = "session/local_storage.json"
SESSION_STORAGE_FILE = "session/session_storage.json"

def pytest_bdd_before_scenario(request, feature, scenario):
    print(f"Starting scenario: {scenario.name}")

def pytest_bdd_before_step(request, feature, scenario, step, step_func):
    print(f"Executing step: {step.name}")

# Add a command-line option for browser selection
def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to use for tests: chrome or firefox (default: chrome)"
    )
    parser.addoption(
        "--environment",
        action="store",
        default="qa",
        help="send the environment name to run the tests in that environment (default: qa)"
    )

@pytest.fixture(scope="session", autouse=True)
def config(request):
    env = request.config.getoption("--environment")
    print(f"Setting up test environment for the entire test session in {env} environment", flush=True)
    # Perform any necessary setup for the environment here
    config_file = f"properties/{env}.properties"
    config = configparser.ConfigParser()
    config.read(config_file)
    yield config
    print("Tearing down test environment for the entire test session", flush=True)
    # Perform any necessary teardown here

@pytest.fixture(scope="session", autouse=True)
def base_url(config):
    return config.get("DEFAULT", "base_url")


@pytest.fixture(scope="session", autouse=True)
def driver(request):
    options = Options()
    # options.add_argument(r"user-data-dir=C:\Users\0143440\AppData\Local\Google\Chrome\User Data")
    # options.add_argument("--profile-directory=Default")
    options.add_argument("--start-maximized")
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
    elif browser == "edge":
        service = Service(EdgeChromiumDriverManager().install())
        driver = webdriver.Edge(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    print(f"Setting up test environment for the entire test session using {browser}", flush=True)
    yield driver
    print("Tearing down test environment for the entire test session", flush=True)

    # # Save cookies
    # os.makedirs("session", exist_ok=True)
    # pickle.dump(driver.get_cookies(), open(COOKIES_FILE, "wb"))
    #
    # # Save localStorage
    # local_storage = driver.execute_script(
    #     "var ls = {}; for (var i = 0; i < localStorage.length; i++) { "
    #     "var key = localStorage.key(i); ls[key] = localStorage.getItem(key); } return ls;"
    # )
    # json.dump(local_storage or {}, open(LOCAL_STORAGE_FILE, "w"))
    #
    # # Save sessionStorage
    # session_storage = driver.execute_script(
    #     "var ss = {}; for (var i = 0; i < sessionStorage.length; i++) { "
    #     "var key = sessionStorage.key(i); ss[key] = sessionStorage.getItem(key); } return ss;"
    # )
    # json.dump(session_storage or {}, open(SESSION_STORAGE_FILE, "w"))
    #
    # print("Session (cookies, localStorage, sessionStorage) saved successfully", flush=True)
    driver.quit()