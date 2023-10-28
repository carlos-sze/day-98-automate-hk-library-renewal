from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import time

MY_ACCOUNT = 'YOUR ACCOUNT NUMBER'
PASSWORD = 'YOUR ACCOUNT PASSWORD'

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.hkpl.gov.hk/en/index.html")

# Sign in
time.sleep(5)
user_field = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[6]/div[1]/div[1]/div[2]/div/div[1]/form/input[3]")
user_field.send_keys(MY_ACCOUNT)
password_field = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div[6]/div[1]/div[1]/div[2]/div/div[1]/form/input[5]")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)


# select all items and renew
time.sleep(3)
select_all_button = driver.find_element(by=By.CLASS_NAME, value="button.selectAll")
select_all_button.click()
renew_button = driver.find_element(by=By.CLASS_NAME, value="button.renew")
renew_button.click()
