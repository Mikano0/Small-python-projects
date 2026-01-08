from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time

load_dotenv()


MY_EMAIL = os.environ.get("EMAIL_USER")
MY_PASS = os.environ.get("EMAIL_PASS")
SIMILAIR_ACCOUNT = "chefsteps"
INSTA_URL = "https://www.instagram.com/"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)

    def login(self):
        """Logs in to instagram"""
        self.driver.get(INSTA_URL)
        cookies_btn = self.wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Allow')]")))
        cookies_btn.click()
        username_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
        username_input.send_keys(MY_EMAIL)
        password_input = self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input[name='password']")))
        password_input.send_keys(MY_PASS)
        login_btn = self.wait.until(ec.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        login_btn.click()
        try:
            save_login = self.wait.until(ec.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Not Now')]")))
            save_login.click()
        except:
            print("Save login popup not shown")


    def find_followers(self):
        """Goes to the mentioned instagram account and clicks on their followers tab and scrolls 10 times, this XPATHs may change depending on instagrams anti bot feature"""
        self.driver.get(f"https://www.instagram.com/{SIMILAIR_ACCOUNT}/")
        follower_btn = self.wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(@href, '/followers/')]")))
        follower_btn.click()
        
        for _ in range(10):
            scroll = self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
            
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(5)
    
    def follow(self):
        """" Looks inside followers div for a button that has the text Follow, and if true clicks on it"""
        scroll_box = self.wait.until(ec.presence_of_element_located((By.XPATH, "/html/body/div[3]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]")))
        all_buttons = scroll_box.find_elements(By.XPATH, "//button[.//div[text()='Follow']]")
        for button in all_buttons:
            try: 
                    button.click()
                    time.sleep(1)
            except Exception as e:
                print("Could not click a button", e)





bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()




time.sleep(200)
