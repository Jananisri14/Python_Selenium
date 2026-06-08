import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
@pytest.mark.parametrize("input_browser",['chrome','firefox'])
@pytest.mark.parametrize("input_url",['https://www.flipkart.com/','https://www.amazon.com/'])
def test_google(input_browser,input_url):
    if input_browser=='chrome':
        driver=webdriver.Chrome()
    if input_browser=='firefox':
        driver=webdriver.Firefox()
    driver.maximize_window()
    driver.get(input_url)
    print(driver.title)
    time.sleep(5)
    driver.close()