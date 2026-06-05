from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('http://automationexercise.com')
driver.maximize_window()
def dismiss_ads(driver):
    try:
        driver.execute_script("""
            var iframes = document.querySelectorAll('iframe');
            for (var i = 0; i < iframes.length; i++) {
                var src = iframes[i].src || '';
                var id  = iframes[i].id  || '';
                if (
                    src.includes('doubleclick') ||
                    src.includes('googleads')   ||
                    src.includes('googlesyndication') ||
                    id.includes('aswift')       ||
                    id.includes('google_ads')
                ) {
                    iframes[i].remove();
                }
            }
        """)
        print("Ads dismissed")
    except Exception as e:
        print(f"Ad dismissal skipped: {e}")
verification=driver.find_element(By.XPATH,'//i[@class="fa fa-home"]//ancestor::a')
if verification.is_displayed:
    print("You are in Home Page")
else:
    print("You are not navigated to home page")

driver.find_element(By.XPATH,"//i[@class='fa fa-list']//parent::a[@href='/test_cases']").click()
print("Home navigate to Test cases Page")
verify2=driver.find_element(By.XPATH,'//b[text()="Test Cases"]')
if verify2.is_displayed:
    print("You are in testcase page")
else:
     print("You are not in testcase page")
driver.close()


