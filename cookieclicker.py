from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import webDriverwait
from selenium.webdriver.common.by import  By
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.dmg")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookiecliker/")

# https://orteil.dashnet.org/cookiecliker/

cookie_id = "bigCookie"
cookie_id = "cookies"
product_price_prefix = "productprice"
product_prefix = "product"

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
while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookie_id).text.split(" ")[0]
    cookies_count = int(cookies_count(",", ""))
    print(cookies_count)

for i in range (4):
    product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",", "")
    
    if not product_price.isdigit():
        continue
    
    product_price = int(product_price.replace(",", ""))
    
    if cookies_count >= product_price:
        product = driver.find_element(By.ID, product_price_prefix + str(i))
        product.click()
        break
    