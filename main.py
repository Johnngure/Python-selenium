from selenium import webdriver
from selenium.webdriver.chrome.service import Service
chromedriver = "/chromedriver"
import time

option = webdriver.ChromeOptions()

option.binary_location = '/Application/Brave Browser.App/content/linux/Brave Browser'

s = Service(chromedriver)

driver = webdriver.Chrome(Service=Service)

driver.get("https://google.com")

time.sleep(10)

driver.quit()