import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
wait=WebDriverWait(driver,10)
driver.get("https://www.leafground.com/")
driver.find_element(By.XPATH,"//i[@class='pi pi-server layout-menuitem-icon']").click()
driver.find_element(By.XPATH,"//span[text()='Dropdown']").click()
element=driver.find_element(By.XPATH,"//select[@class='ui-selectonemenu']")
dropdown=Select(element)
time.sleep(10)
dropdown.select_by_visible_text("Selenium")
selected_text = dropdown.first_selected_option.text
print("Selected Text using select_by_visible_text:", selected_text)
dropdown.select_by_index(2)
selected_text = dropdown.first_selected_option.text
print("Selected Text using select_by_index:", selected_text)
element2=driver.find_element(By.XPATH,"//button[@type='button']").click()

