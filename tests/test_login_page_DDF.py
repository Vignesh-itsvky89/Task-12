from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest
import sys
import os
from selenium import webdriver
from datetime import date
import time

# Add the parent directory to the path if amazon_login_page.py is in the parent directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.Login.HRM_login_page import LoginPage
from utilities import ExcelUtils
from pages.Menu.HRM_Menu_options import Menu_options
# from HRM_login_page import browser

@pytest.fixture
def browser():
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options)
    # driver.maximize_window()
    # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    chromedriver_path = r"D:\Automation study\Python Programming\Requirement\chromedriver.exe"
    if not os.path.exists(chromedriver_path):
        raise FileNotFoundError(f"ChromeDriver not found at path: {chromedriver_path}")

    os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    service = Service(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    time.sleep(6)
    driver.maximize_window()
    driver.quit()

def pytest_configure(config):
    config.option.htmlpath = '/path/to/report.html'

def test_login_02(browser):
    login_page = LoginPage(browser)
    login_page1 = Menu_options(browser)
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    path = r"D:\Automation study\Python Programming\Python class file\pythonProjectSelenium_0405\Task-12\testdata\OrangeLoginData.xlsx"
    rows = ExcelUtils.getRowCount(path,'Sheet1')
    for row in range(2,rows+1):
        username = ExcelUtils.readData(path,'Sheet1', row,2)
        password = ExcelUtils.readData(path,'Sheet1', row, columnno=3)
        current_day = date.today()
        time1 = time.localtime()
        current_time = time.strftime("%H:%M:%S", time1)
        tester = "Vignesh"
        login_page.setUserName(username)
        login_page.setPassword(password)
        login_page.clickLogin()
        if browser.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
            print("test_login_02 is passed")
            ExcelUtils.writeData(path, 'Sheet1',row, 4, "Pass")
            ExcelUtils.writeData(path, 'Sheet1', row, 1, "test_login_02")
            ExcelUtils.writeData(path, 'Sheet1', row, 5, current_day)
            ExcelUtils.writeData(path, 'Sheet1', row, 6, current_time)
            ExcelUtils.writeData(path, 'Sheet1', row, 7, tester)
            login_page.select_logout()
        else:
            # assert login_page.invalid_credentials() == "Invalid credentials"
            print("test_login_02 is failed due to invalid password in excel")
            ExcelUtils.writeData(path, 'Sheet1', row, 4, "Fail")
            ExcelUtils.writeData(path, 'Sheet1', row, 1, "test_login_02")
            ExcelUtils.writeData(path, 'Sheet1', row, 5, current_day)
            ExcelUtils.writeData(path, 'Sheet1', row, 6, current_time)
            ExcelUtils.writeData(path, 'Sheet1', row, 7, tester)









