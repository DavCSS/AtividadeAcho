#https://the-internet.herokuapp.com/login

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
import time



driver_path = "C:/Users/Jeane Peres/Documents/Gecko/geckodriver.exe"
service = Service(driver_path)
driver = webdriver.Firefox(service=service)

driver.get("https://the-internet.herokuapp.com/login")

usernameBox = driver.find_element(By.ID, "username")
passBox = driver.find_element(By.ID, "password")
submitBtn = driver.find_element(By.XPATH, "//button[@class='radius' and @type='submit']")


time.sleep(1)

usernameBox.send_keys("tomsmith")
time.sleep(.3)
passBox.send_keys("SuperSecretPassword!")
time.sleep(.2)
submitBtn.click()
time.sleep(1)

successMsg = driver.find_element(By.XPATH, "//div[contains(text(), 'You logged into a secure area!')]")


if successMsg.is_displayed():
    print("Deu certo eba")
else:
    print("Ops nao deu")


time.sleep(1)



driver.quit()

