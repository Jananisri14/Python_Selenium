import pytest
from selenium import webdriver
#1.
@pytest.fixture()
def test_setup_and_teardown(request):
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://tutorialsninja.com/demo/")
    request.cls.driver=driver
    yield
    driver.quit()
#2.
# @pytest.fixture(params=['chrome','firefox','edge'])
# def test_setup_and_teardown(request):
#     if request.param=='chrome':
#         driver=webdriver.Chrome()
#     elif request.param=='firefox':
#         driver=webdriver.Firefox()
#     elif request.param=='edge':
#         driver=webdriver.Edge()
#     driver.maximize_window()
#     driver.get("https://tutorialsninja.com/demo/")
#     request.cls.driver=driver
#     yield
#     driver.quit()  