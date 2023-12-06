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

cookie = driver.find_element(By.ID, cookie_id)
cookie.click()