from selenium import webdriver
from selenium.webdriver.common.by import By
import config
import time

browser =  webdriver.Chrome()
browser.maximize_window()
browser.get("https://github.com")
signin_link = browser.find_element(By.LINK_TEXT, "Sign in")
signin_link.click()

time.sleep(2)
username_box = browser.find_element(By.ID, "login_field")
username_box.send_keys(config.username)
password_box = browser.find_element(By.ID, "password")
password_box.send_keys(config.password)
password_box.submit()

# profile_link = browser.find_element(By.CLASS_NAME, "user-profile-link")
# link_label = profile_link.get_attribute("innerHTML")
# assert "Jogira" in link_label

assert "Jogira" in browser.page_source
print("Success.")
input()
