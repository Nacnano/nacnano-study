import time
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get('')

driver.implicitly_wait(3*60*60)

# LOGIN PAGE
username_box = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/form/div[1]/div/input")))
password_box = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/form/div[2]/div/input")))
username_box.send_keys("admin")
password_box.send_keys("password")

login_enter_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/form/button")))
login_enter_button.click()


# HOME PAGE
home_button = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div/div[1]/div[1]/button")
home_button.click()
users_dropdown_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/main/div[2]/div/div[1]/div[2]/ul/li[11]")))
users_dropdown_button.click()
student_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/div/main/div[2]/div/div[1]/div[2]/ul/li[11]/ul/li[1]")))
student_button.click()


### STUDENT MANAGEMENT PAGE ###
ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
updated_phone_number = []
phone_number_list = []
total = len(phone_number_list)

for i in range(0, total, 1):
    start_time = time.perf_counter()
    phone_number = phone_number_list[i]

    # search mobile phone number
    phone_box = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/input")
    phone_box.clear()
    time.sleep(0.3)
    phone_box.send_keys(phone_number)
    time.sleep(1)

    # click 'money' button
    money_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr/td[8]/div/div[1]")))
    money_button.click()
    time.sleep(0.5)

    # select branch
    branch_dropdown_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/div/div/button")))
    branch_dropdown_button.click()
    time.sleep(0.6)
    # select_branch_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/div/div/div[2]/ul/li[1]")))
    select_branch_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='มังกี้สาขา1']")))
    select_branch_button.click()
    time.sleep(0.5)

    # select package
    package_dropdown_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[2]/div/div")))
    package_dropdown_button.click()
    time.sleep(0.6)
    # select_package_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div[2]/ul/li[2]")))
    select_package_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='แพ็กเกจ 1 วัน']")))
    select_package_button.click()
    time.sleep(0.5)

    # add text reference
    reference_box = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[3]/div/div/input")))
    reference_box.send_keys('add3daysfor:' + phone_number)
    time.sleep(0.5)

    # update payment
    reference_box = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[4]/button[2]")))
    reference_box.click()
    time.sleep(0.5)

    updated_phone_number.append(phone_number)
    df = pd.DataFrame({'phone number': updated_phone_number})
    df.to_csv("C:/Users/chotp/Documents/Chotpisit/Codes/MonkeyEveryday-Trainee/add3days_bot/updated_data/updated_from_cms/updated_phone_number_"+str(i+1)+".csv")
    time.sleep(1)

    end_time = time.perf_counter()
    print("AtTime " + str(end_time) + ": Progress " + "%.2f" % ((i+1)/total*100) + '% : QueryNumber ' +
          str(i+1) + ' - SuccessfullyUpdated ' + phone_number + " : TimeUsed " + str(round(end_time-start_time, 2)))

print("Done Updating!")

try:
    print("Exiting... [" + driver.current_url + "]")
    driver.quit()
except:
    print("Chrome is not reachable...")

print("All Done!")
