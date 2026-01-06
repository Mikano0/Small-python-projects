from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import os
import time
from dotenv import load_dotenv

load_dotenv()

MY_EMAIL = os.environ.get("EMAIL_USER")
MY_PASS = os.environ.get("EMAIL_PASS")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/login")

wait = WebDriverWait(driver, 5)

# This is only needed if your browser doesnt automatically remember you and sign you in which should only be the first time 
# email_input = wait.until(ec.element_to_be_clickable((By.ID, "username")))
# email_input.send_keys(MY_EMAIL)
# pass_input = wait.until(ec.element_to_be_clickable((By.ID, "password")))
# pass_input.send_keys(MY_PASS)

time.sleep(2)

search_bar = driver.find_element(By.CSS_SELECTOR, value=".basic-input")
search_bar.send_keys("Python Developer") <- # can change this depending on what job u want to search for
search_bar.send_keys(Keys.ENTER)

try:
    see_all = wait.until(ec.presence_of_element_located((By.XPATH, "//a[contains(@href, 'origin=BLENDED_SEARCH_RESULT_NAVIGATION_SEE_ALL')]")))
    see_all.click()
    time.sleep(3)
except:
    print("No See all jobs found, continueing search")

job_list_container = driver.find_element(By.CLASS_NAME, "scaffold-layout__list")

job_cards = driver.find_elements(By.CSS_SELECTOR, "div.job-card-container")
print(f"Found {len(job_cards)} jobs")

for job in job_cards:
    try:
        link_el = job.find_element(By.CSS_SELECTOR, value="a.job-card-container__link")
        title = link_el.text
        link = link_el.get_attribute("href")
        company = job.find_element(By.CLASS_NAME, "artdeco-entity-lockup__subtitle").text
        print(f"{title},{company},\n{link}")
        print("\n")
    except:
        continue


time.sleep(300)
