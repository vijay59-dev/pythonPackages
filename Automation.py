from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
# driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.get("https://testautomationpractice.blogspot.com/")

maleRdBtnLbl = driver.find_element(By.XPATH, "//*[@id='q26']/table/tbody/tr[1]/td/label")
maleRdBtnLbl.click()

tuesChkBoxLbl = driver.find_element(By.XPATH, "//*[@id='q15']/table/tbody/tr[3]/td/label")
tuesChkBoxLbl.click()

ddlTimeToContact = driver.find_element(By.ID, "RESULT_RadioButton-9")
slct = Select(ddlTimeToContact)

# ddlTimeToContact.click()
slct.select_by_value("Radio-0")
# slct.select_by_index(2)
# slct.select_by_visible_text("Evening")

uploadBtn = driver.find_element(By.ID, "RESULT_FileUpload-10")
uploadBtn.send_keys("C:\\Users\\iyad\\OneDrive\\Desktop\\canada_flag.jfif")

time.sleep(5)

time.sleep(10)