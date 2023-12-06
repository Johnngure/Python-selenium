from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chromedriver = "/chromedriver"
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import webDriverwait
from selenium.webdriver.support import expected_conditions as EC
import time

option = webdriver.ChromeOptions()

option.binary_location = '/Application/Brave Browser.App/content/linux/Brave Browser'

s = Service(chromedriver)

driver = webdriver.Chrome()

driver.get("https://google.com")

webDrivewait(driver, 5).untill(
    EC.presence_of_element_located(By.CLASS_NAME,"gLFyf")
)

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("Ngure technologies" + Keys.ENTER)


time.sleep(20)

driver.quit()