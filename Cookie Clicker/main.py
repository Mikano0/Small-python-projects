from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

game_on = True
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(3)

try:
    language = driver.find_element(By.ID, value="langSelect-EN")
    language.click()
    time.sleep(2)
except NoSuchElementException:
    print("Language not found")

last_check = time.time()
cookie = driver.find_element(By.ID, value="bigCookie")
five_min = time.time() + 60*5

while game_on:
    cookie.click()
    if time.time() - last_check > 5:
        try:
            last_check = time.time()
            upgrades = driver.find_elements(By.CSS_SELECTOR, value=".product.unlocked.enabled")
            max_price = 0
            best_upgrade = None
            for upgrade in upgrades:
                try:
                    price_text = upgrade.find_element(By.CLASS_NAME, value="price").text
                    price = int(price_text.replace(",", ""))
                    if price > max_price:
                        max_price = price
                        best_upgrade = upgrade
                except (NoSuchElementException, ValueError):
                    continue
                
            if best_upgrade:
                best_upgrade.click()
        except (NoSuchElementException, ValueError):
            print(" Couldnt find cookie count or upgrades")
    
    if time.time() > five_min:
        try:
            cookies_per_second = driver.find_element(By.ID, value="cookiesPerSecond").text
            print(f"Your final cookies per second were {cookies_per_second}")
        except NoSuchElementException:
            print("Couldnt get your final cookies per second")
        game_on = False

