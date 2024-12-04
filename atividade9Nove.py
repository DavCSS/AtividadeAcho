#https://www.selenium.dev/

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.service import Service
import time


driver_path = "C:/Users/Jeane Peres/Documents/Gecko/geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://www.selenium.dev/")

alert = Alert(driver)
alert.dismiss()

time.sleep(1)



driver.quit()

