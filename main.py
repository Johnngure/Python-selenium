from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chromedriver = "/chromedriver"
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

option = webdriver.ChromeOptions()

option.binary_location = '/Application/Brave Browser.App/content/linux/Brave Browser'

s = Service(chromedriver)

driver = webdriver.Chrome()

driver.get("https://google.com")

input_element = driver.find_element(By.CLASS_NAME,"gLFyf")
input_element.send_keys("Ngure technologies" + Keys.ENTER)

time.sleep(20)

driver.quit()