from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver=webdriver.Chrome()
driver.get('http://automationexercise.com')
driver.maximize_window()
wait=WebDriverWait(driver,10)
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
dismiss_ads(driver)
action=ActionChains(driver)
verify=wait.until(EC.visibility_of_element_located((By.XPATH,"//ul[@class='nav navbar-nav']//child::a[1][@style='color: orange;']")))
if verify.is_enabled:
    print("You are in the Home Page")
else:
    print("You are not in the Home Page")

click1=wait.until(EC.element_to_be_clickable((By.XPATH,"//ul[@class='nav navbar-nav']//descendant::a[2]")))
click1.click()
dismiss_ads(driver)
print("you are in product page")
product=driver.find_element(By.XPATH,"//div[@id='cartModal']//following-sibling::div[@class='col-sm-4'][1]")
addtocart=driver.find_element(By.XPATH,"//div[@class='overlay-content']//child::a[@data-product-id='1']")
action.scroll_to_element(product)
action.move_to_element(product).click(addtocart).perform()
print("clicked Add to cart button")
verify2=driver.find_element(By.XPATH,"//div[@class='modal-content']")
if verify2.is_displayed:
    print("Product added to the cart")
else:
    print("Product not added to the cart")
cart=wait.until(EC.visibility_of_element_located((By.XPATH,"//*[text()='View Cart']")))
cart.click()
print("Page Directed to Cart")





