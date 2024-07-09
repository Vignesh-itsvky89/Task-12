from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
class LoginPage:
    textbox_username_id = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input'
    textbox_password_id = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input'
    button_login_id = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    Invalid_login_credentials = '/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'
    select_logout_dropdown = '//i[@class="oxd-icon bi-caret-down-fill oxd-userdropdown-icon"]'
    logout = 'Logout'
    # drpdwn_logout_id = "welcome"
    # link_logout_xpath = "//*[@id='welcome-menu']/ul/li[3]/a"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        username1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.textbox_username_id)))
        username1.click()
        username1.send_keys(username)

    def setPassword(self, password):
        password1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.textbox_password_id)))
        password1.click()
        password1.send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_id).click()

    def invalid_credentials(self):
        Invalid_login_credentials = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Invalid_login_credentials)))
        print(Invalid_login_credentials.text)

    def select_logout(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.select_logout_dropdown))).click()
        logout1 = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, self.logout)))
        actions = ActionChains(self.driver)  # initialize ActionChain object
        actions.move_to_element(logout1)
        actions.click(logout1)
        actions.perform()


class forgot_login:
    forgot_password ='p[class = "oxd-text oxd-text--p orangehrm-login-forgot-header"]'
    username = 'input[class= "oxd-input oxd-input--active"]'
    reset_password  = 'button[class="oxd-button oxd-button--large oxd-button--secondary orangehrm-forgot-password-button orangehrm-forgot-password-button--reset"]'
    reset_password_popup = 'h6[class="oxd-text oxd-text--h6 orangehrm-forgot-password-title"]'

    def __init__(self, driver):
        self.driver = driver

    def select_forgot_password(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.forgot_password))).click()

    def send_username(self, uname):
        username = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.username)))
        username.click()
        username.send_keys(uname)

    def select_reset_password(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.reset_password))).click()

    def validate_reset_password_popup(self):
        reset_password_popup = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.reset_password_popup)))
        print(reset_password_popup.text)

class PIM:
    pim = '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a'
    add_Employee = '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/a'
    first_name ='/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input'
    mid_name = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input'
    last_name = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input'
    emp_id = '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
    save_employee =  'button[class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    emp_added = '/html/body/div/div[2]'
    Employee_List = 'a.oxd-topbar-body-nav-tab-item'
    Employee_Id = '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
    search = 'button[class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    edit = 'i[class="oxd-icon bi-pencil-fill"]'
    Driving_license = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input'
    license_Expiry = '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/input'
    save = 'button[class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]'
    epm_edited = '/html/body/div/div[2]'
    delete = 'i[class="oxd-icon bi-trash"]'
    select_window_delete ='button[class="oxd-button oxd-button--medium oxd-button--label-danger orangehrm-button-margin"]'
    epm_deleted = '/html/body/div/div[2]'
    # epm_deleted = 'div[class = "oxd-toast-container oxd-toast-container--bottom"]'

    def __init__(self, driver):
        self.driver = driver

    def select_PIM(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.pim))).click()

    def select_Add_Employee(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.add_Employee))).click()

    def set_first_name(self, fname):
        fname1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))
        fname1.click()
        fname1.send_keys(fname)

    def set_mid_name(self, mname):
        mname1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.mid_name)))
        mname1.click()
        mname1.send_keys(mname)

    def set_last_name(self, lname):
        lname1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))
        lname1.click()
        lname1.send_keys(lname)

    def set_emp_id(self, emp_id):
        emp_id1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.emp_id)))
        emp_id1.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        emp_id1.send_keys(emp_id)

    def select_save_employee(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.save_employee))).click()

    def emp_added_success(self):
        epm_added = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.emp_added)))
        a = epm_added.text
        return a

    def select_Employee_List(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.Employee_List))).click()

    def set_Employee_Id(self, emp_id):
        Employee_Id = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,self.Employee_Id)))
        Employee_Id.click()
        Employee_Id.send_keys(emp_id)

    def select_search(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.search))).click()

    def select_edit(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.edit))).click()

    def set_Driving_license(self, D_No):
        Driving_license1 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.Driving_license)))
        Driving_license1.click()
        Driving_license1.send_keys(D_No)

    def set_license_Expiry(self, date):
        license_Expiry = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH,self.license_Expiry)))
        license_Expiry.click()
        license_Expiry.send_keys(date)

    def select_save(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.save))).click()

    def emp_edited_success(self):
        epm_edited = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.epm_edited)))
        a = epm_edited.text
        return a

    def select_delete(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.delete))).click()

    def select_wndow_delete(self):
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,self.select_window_delete))).click()

    def emp_deleted_success(self):
        epm_deleted = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.epm_deleted)))
        print(epm_deleted.text)