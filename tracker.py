from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from datetime import datetime
import csv

url = "https://shopee.sg/HYDRAULIC-MONITOR-MOUNTING-ARM-NB-F80-LCD-SCREEN-DESK-TABLE-VESA-MOUNT-STAND-360-ADJUSTABLE-ROTATION-i.13842071.2689454006"
headers = headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36" }
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080")

driver = webdriver.Chrome("C:\\Users\\kanis\\Documents\\Legit Stuff\\NUS\\YSI SEA\\Java Extras\\chromedriver_win32\\chromedriver.exe", options=chrome_options)

driver.get(url)

timeout = 3 # seconds
try:
    myElem = WebDriverWait(driver, timeout).until(expected_conditions.presence_of_element_located((By.XPATH, "//span[contains(text(), 'VESA MOUNT')]")))
except TimeoutException:
    print ("Timeout exceeded!")

title_name = driver.find_element_by_xpath("//span[contains(text(), 'VESA MOUNT')]")
product = driver.find_element_by_xpath("//button[contains(text(), 'F80')]")
product.click()
price = driver.find_element_by_xpath("//div[@class='_3e_UQT']")
time_now = datetime.now()
dt_string = time_now.strftime("%d/%m/%Y %H:%M:%S")

price_list = [dt_string, title_name.text, price.text]

with open('./price_history.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(price_list)

driver.quit()