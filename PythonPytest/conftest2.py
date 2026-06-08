import pytest
from selenium.webdriver.common.by import By
@pytest.mark.usefixtures("test_setup_and_teardown")
class TestSearch:
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