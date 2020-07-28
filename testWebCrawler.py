import sys
import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("prefs", { "profile.default_content_setting_values.notifications": 2})
desired_cap = chrome_options.to_capabilities()
desired_cap.update({
  'browser_version': '75.0',
  'os': 'Windows',
  'os_version': '10'})
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH,desired_capabilities=desired_cap);

driver.get("https://www.facebook.com/messages/t/")

print(driver.title)
email = driver.find_element_by_id("email")
email.send_keys("email/phone")
password = driver.find_element_by_id("pass")
password.send_keys("password")
password.send_keys(Keys.RETURN)
driver.implicitly_wait(7)
heartEmojiList = driver.find_elements_by_class_name('_5j_u')
print(heartEmojiList)