from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import webDriverwait
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.deb")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookiecliker/")

# https://orteil.dashnet.org/cookiecliker/

cookie_id = "bigCookie"

webDrivewait(driver, 5).untill(
    EC.presence_of_element_located((By.XPATH,"//*[contains(text(), 'English')]"))
)

language = driver.find_element(By.XPATH,"//*[contains(text(), 'English')]")
language.click()

webDrivewait(driver, 5).untill(
    EC.presence_of_element_located((By.ID, cookie_id))
)

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()