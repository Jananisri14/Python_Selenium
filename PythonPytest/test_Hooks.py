import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
def setup_function(function):
    global driver
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://tutorialsninja.com/demo/")
def teardown_function(function):
    driver.quit()
def test_valid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("HP")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        assert self.driver.find_element(By.XPATH,"//*[text()='HP LP3065']").is_displayed()
def test_invalid_product(self):
        self.driver.find_element(By.NAME, "search").send_keys("Honda")
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_res = "There is no product that matches the search criteria."
        actual_res = self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
        assert actual_res == expected_res
def test_no_product(self):
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-default btn-lg']").click()
        expected_res = "There is no product that matches the search criteria."
        actual_res = self.driver.find_element(By.XPATH,"//p[text()='There is no product that matches the search criteria.']").text
        assert actual_res == expected_res