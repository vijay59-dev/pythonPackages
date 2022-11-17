import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://facebook.com")

username = driver.find_element(By.CLASS_NAME, "inputtext")
username.send_keys("iyad.koteich")


time.sleep(5)