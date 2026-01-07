from selenium import webdriver
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
from requests_oauthlib import OAuth1
import requests
import os
import time

load_dotenv()

PROMISED_UP = # Your promised upload speed
PROMISED_DOWN = # Your promised download speed
MY_EMAIL = os.environ.get("EMAIL_USER")
MY_PASS = os.environ.get("EMAIL_PASS")
INTERNET_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://api.x.com/2/tweets"

# --- X Auth ---
API_KEY = os.getenv("X_API_KEY")
API_SECRET = os.getenv("X_API_SECRET")
ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("X_TOKEN_SECRET")
auth = OAuth1(API_KEY,API_SECRET,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)




class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get(INTERNET_URL)
        time.sleep(3)
        self.cookies_btn = self.driver.find_element(By.ID, value="onetrust-accept-btn-handler")
        self.cookies_btn.click()
        self.start_btn = self.driver.find_element(By.CSS_SELECTOR, value=".start-text")
        self.start_btn.click()
        time.sleep(60)
        try:
            download_speed = self.driver.find_element(By.CSS_SELECTOR, value=".download-speed").text.strip()
            upload_speed = self.driver.find_element(By.CSS_SELECTOR, value=".upload-speed").text.strip()
            self.down = float(download_speed)
            self.up = float(upload_speed)
        except ValueError:
            pass
        print(self.down)
        print(self.up)
    
        
    def tweet_at_provider(self):    
        payload = {
            "text": f"Hey ISP! Why is my internet speed {self.down}/ {self.up}"
                    f"When i am paying for {PROMISED_DOWN}/ {PROMISED_UP}?"
        }
        response = requests.post(TWITTER_URL, json= payload, auth=auth)
        print(response.json())

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()

if bot.up < PROMISED_UP and bot.down < PROMISED_DOWN:
    bot.tweet_at_provider()
bot.tweet_at_provider()
time.sleep(200)
