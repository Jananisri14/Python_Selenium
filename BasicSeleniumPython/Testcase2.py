from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('http://automationexercise.com')
driver.maximize_window()
driver.find_element(By.XPATH,)