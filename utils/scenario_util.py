import time

from pages.addEmp import AddEmp
from pages.my_info_page import MyInfoPage
from pages.signin_HRM import OrangeHRM
from pages.user_search_HRM import UserSearchHRM
from utils.excel_util import get_credentials_from_excel, get_employee_details_from_excel


def scenario_login(driver, config):
    creds = get_credentials_from_excel('tests/testdata/HRM.xlsx', 'Login')[0]# Get first row
    userid = creds['userid']
    password = creds['password']
    signin_page = OrangeHRM(driver)
    signin_page.fill_signin_submit(config, userid, password)
    print('Login successful with user: {}'.format(userid))

def scenario_admin_search(driver):
    admin_page = UserSearchHRM(driver)
    admin_page.select_admin_user_type()
    assert driver.find_element(*admin_page._ADMIN_ROLE).is_displayed()

def add_emp_scenario(driver):
    add_emp_page = AddEmp(driver)
    emp_details = get_employee_details_from_excel('tests/testdata/HRM.xlsx', 'emp' )[0]  # Get first employee
    firstname = emp_details['firstname']
    middlename = emp_details['middlename']
    lastname = emp_details['lastname']
    add_emp_page.add_user(firstname, middlename, lastname)

def delete_emp_scenario(driver):
    add_emp_page = AddEmp(driver)
    emp_details = get_employee_details_from_excel('tests/testdata/HRM.xlsx', 'emp')[0]  # Get first employee
    firstname = emp_details['firstname']
    middlename = emp_details['middlename']
    lastname = emp_details['lastname']
    add_emp_page.delete_emp(firstname, middlename, lastname)

def save_myInfo(driver):
    myInfo_page = MyInfoPage(driver)
    emp_details = get_employee_details_from_excel('tests/testdata/HRM.xlsx', 'myInfo')[0]  # Get first employee
    firstname = emp_details['firstname']
    middlename = emp_details['middlename']
    lastname = emp_details['lastname']
    myInfo_page.update_myInfo(firstname, middlename, lastname)
    assert driver.find_element(*myInfo_page._SAVE_CONFIRMATION_MESSAGE).is_displayed()