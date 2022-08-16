import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

driver = webdriver.Chrome(executable_path="C:\Development\chromedriver.exe")

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)
leng = driver.find_element(By.ID, "langSelect-PT-BR")
leng.click()
time.sleep(10)

button = driver.find_element(By.ID, "bigCookie")

# Max bot time = 5 min and time to check upgrades each 5 sec.
timeout_tools = time.time() + 5
max_time = time.time() +5*60
while time.time() < max_time:
    if time.time() > timeout_tools:
        # Upgrade the tools.
        try:
            driver.find_element(By.ID, "upgrade0").click()
        except ElementNotInteractableException:
            pass
        except StaleElementReferenceException:
            pass
        except NoSuchElementException:
            pass
        # Buy new tools.
        products = driver.find_elements(By.CSS_SELECTOR, "div.unlocked.enabled")
        prod_len = len(products)-1
        products[prod_len].click()
        products = []
        timeout_tools = time.time() + 5
    button.click()

clicks_per_second = driver.find_element(By.XPATH, "//*[@id='cookiesPerSecond']").text
print(f"Cookies {clicks_per_second}")
driver.quit()