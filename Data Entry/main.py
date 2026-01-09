from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from selenium.webdriver.common.by import By
import time

URL = "https://appbrewery.github.io/Zillow-Clone/"
FORMS = "https://docs.google.com/forms/d/e/1FAIpQLSe53SId6wh8rW4ER7xEuV7ggC_-y0J93VuwiHAvXnVVRa9ELA/viewform?usp=dialog"



links = []
costs = []
addresses = []

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}




response = requests.get(URL, headers= header)
response.raise_for_status()
web_page = (response.text)

soup = BeautifulSoup(web_page, "html.parser")
# print(soup)

all_links = soup.find_all("a", class_="property-card-link")
for link in all_links:
    links.append(link["href"])

print(links)

all_cost = soup.find_all("span", class_="PropertyCardWrapper__StyledPriceLine")
for cost in all_cost:
    money = cost.getText().strip()
    junk = ["/mo", "+", " ", "1bd", "1 bd"]
    for j in junk:
        money = money.replace(j, "")
    costs.append(money)
print(costs)
# the same as the code above but easier to understand
# for cost in all_cost:
#     money = cost.getText().strip()
#     money = money.replace("/mo", "") 
#     money = money.replace("+", "") 
#     money = money.replace("1 bd", "") 
#     money = money.replace("1bd", "") 
#     costs.append(money)

address_links = soup.find_all("a", class_="StyledPropertyCardDataArea-anchor")
for address_tag in address_links:
    address_text = address_tag.getText().strip()
    junk = ["|", "\n"]
    for j in junk:
        address_text = address_text.replace(j, "")
        
    addresses.append(address_text)
print(addresses)

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options)


for n in range(len(links)):
    driver.get(FORMS)
    time.sleep(2)
    
    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    cost = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')

    address.send_keys(addresses[n])
    cost.send_keys(costs[n])
    link.send_keys(links[n])
    submit.click()



time.sleep(200)
