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

import numpy as np
import json
import datetime
from datetime import datetime
from datetime import timedelta
from sqlalchemy import create_engine
import pymysql


# Access Chrome web driver
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(web_url)

# timer
driver.implicitly_wait(3*60*60)
real_start_time = time.perf_counter()

# LOGIN PAGE
username_box = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/form/div[1]/div/input")))
password_box = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/form/div[2]/div/input")))
username_box.send_keys(username)
password_box.send_keys(password)

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

# Query target phone number data form database
everyday_username = ""
everyday_password = ""

everyday_sql_engine = create_engine('postgresql://{monkeyeveryday_username}:{monkeyeveryday_password}@35.187.233.216/everyday')

with everyday_sql_engine.connect() as dbConnection:
    df_target = pd.read_sql('''
        select 
        phone ,
        id ,
        first_name ,
        last_name ,
        created_at 
        from 
        everyday.public."user" u 
        where u.payment_type ='TOP_UP' and created_at <= '2022-04-07'
        order by created_at 
    ''', dbConnection)

with everyday_sql_engine.connect() as dbConnection:
    df_prev_payment_history = pd.read_sql(f'''
            select 
            u.phone ,
            ph.package_id ,
            u.first_name ,
            u.last_name ,
            u.id ,
            ph.created_at ,
            ph.channel 
            from everyday.public.payment_history ph 
            inner join
            everyday.public."user" u 
            on u.id = ph.user_id 
            where package_id = '{package_id}'
            order by ph.created_at asc
            ''', dbConnection)

phone_from_prev_database = df_prev_payment_history['phone'].to_list()
updated_phone_number = phone_from_prev_database
phone_number_list = df_target['phone'].to_list()
phone_number_list.remove('')

# remove the duplicated phone number
updated_phone_number.remove('')

start_index = len(updated_phone_number)
total = len(phone_number_list)
for i in range(start_index, total, 1):
    start_time = time.perf_counter()
    phone_number = phone_number_list[i]

    # search mobile phone number
    phone_box = driver.find_element(by=By.XPATH, value="/html/body/div/main/div[2]/div/div[2]/div[2]/div[1]/div[3]/div[1]/div/div/input")
    phone_box.clear()
    time.sleep(0.5)
    phone_box.send_keys(phone_number)
    time.sleep(2)

    # check phone number(in case of duplicated phone number)
    while True:
        check_phone_number = driver.find_element(
            by=By.XPATH, value="/html/body/div/main/div[2]/div/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr/td[1]/p")
        if check_phone_number.text == phone_number:
            break

    # click 'money' button
    money_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[2]/div/div/div/table/tbody/tr/td[8]/div/div[1]")))
    money_button.click()
    time.sleep(0.5)

    # select branch
    branch_dropdown_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/div/div/button")))
    branch_dropdown_button.click()
    time.sleep(0.7)
    # select_branch_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[1]/div/div/div[2]/ul/li[1]")))
    select_branch_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='" + branch_name + "']")))
    select_branch_button.click()
    time.sleep(0.5)

    # select package
    package_dropdown_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[2]/div/div")))
    package_dropdown_button.click()
    time.sleep(0.7)
    # select_package_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div[2]/ul/li[2]")))
    select_package_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.presence_of_element_located((By.XPATH, "//p[text()='" + package_name + "']")))
    select_package_button.click()
    time.sleep(0.5)

    # add text reference
    reference_box = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable(
        (By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[3]/div/div/input")))
    reference_box.send_keys('add3daysfor:' + phone_number)
    time.sleep(0.5)

    # update payment
    update_button = WebDriverWait(driver, 1000, ignored_exceptions=ignored_exceptions).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/main/div[2]/div/div[2]/div[2]/div[4]/div/div/div[4]/button[2]")))
    update_button.click()
    time.sleep(1)

    # update updated list
    updated_phone_number.append(phone_number)
    df = pd.DataFrame({'phone number': updated_phone_number})
    df.to_csv(""+str(i+1)+".csv")

    # print the process info
    end_time = time.perf_counter()
    print("AtTime " + str(round(end_time-real_start_time, 2)) + " : Progress " + "%.2f" % ((i+1)/total*100) + '% : QueryNumber ' +
          str(i+1) + ' - SuccessfullyUpdated ' + phone_number + " : TimeUsed " + str(round(end_time-start_time, 2)))

    # check from database
    time.sleep(1)
    with everyday_sql_engine.connect() as dbConnection:
        df_payment_history = pd.read_sql(f'''
            select 
            u.phone ,
            ph.package_id ,
            u.first_name ,
            u.last_name ,
            u.id ,
            ph.created_at ,
            ph.channel 
            from everyday.public.payment_history ph 
            inner join
            everyday.public."user" u 
            on u.id = ph.user_id 
            where package_id = '{package_id}'
            order by ph.created_at asc
            ''', dbConnection)

    phone_from_database = df_payment_history['phone'].to_list()
    df_payment_history.to_csv(
        ""+str(i+1)+".csv")
    phone_from_database.remove('')
    # compare updated database data
    if(phone_from_database == updated_phone_number):
        print("Status: Updated CMS matched with Updated database")
    else:
        print("WARNING!!!: UPDATED DOES NOT MATCH WITH DATABASE")
        break

try:
    print("Exiting... [" + driver.current_url + "]")
    driver.quit()
except:
    print("Chrome is not reachable...")

print("Done!")
