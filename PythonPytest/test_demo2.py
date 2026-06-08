import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@pytest.mark.parametrize("search_item",[("selenium"),("Pytest"),("Locators")])
def test_google(search_item):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")
    element=driver.find_element(By.NAME,value="q")
    element.send_keys(search_item)
    element.send_keys(Keys.ENTER)
