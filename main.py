from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chromedriver = "/chromedriver"
import time

option = webdriver.ChromeOptions()

option.binary_location = '/Application/Brave Browser.App/content/linux/Brave Browser'

s = Service(chromedriver)

driver = webdriver.chrome(Services=s, option=option)

driver.get("http://google.com")

time.sleep(10)

driver.quit()