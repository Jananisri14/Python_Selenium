import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.google.co.in")
print(driver.title)
element=driver.find_element(By.NAME,value="q")
if element.is_enabled:
    print("It is Enabled")
else:
    print("It is not Enabled")
element.send_keys("Selenium")
element.send_keys(Keys.ENTER)
time.sleep(5)
driver.close()