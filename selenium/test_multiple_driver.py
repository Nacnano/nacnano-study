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
ignored_exceptions=(NoSuchElementException,StaleElementReferenceException,)

web_url = "https://www.mytcas.com/universities"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument('headless')
driver1 = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver1.get(web_url)
driver1.implicitly_wait(3*60*60)

driver=[None] * 100
for i in range(0,2,1):
    driver[i] = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver[i].get(web_url)
    time.sleep(2)
    driver[i].quit()


driver1.quit()