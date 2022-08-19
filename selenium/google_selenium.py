from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome("C:/Users/chotp/Documents/chromedriver.exe")
options = webdriver.ChromeOptions()
driver.get('https://www.google.com')
driver.implicitly_wait(100)

search_box = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
search_button = driver.find_element(by=By.NAME,value="btnK")

search_box.send_keys("Selenium")
search_button.click()

print(driver.current_url)
print(driver.title)
print(driver.find_element(by=By.NAME, value="q").get_attribute("value"))

driver.quit()