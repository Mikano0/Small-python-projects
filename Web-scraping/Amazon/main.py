import requests
from bs4 import BeautifulSoup
import smtplib
from dotenv import load_dotenv
import os
load_dotenv()

URL = "https://appbrewery.github.io/instant_pot/"
# URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
BUY_PRICE = 100

email_user = os.environ.get("EMAIL_USER")
email_pass = os.environ.get("EMAIL_PASS")
to_email = os.environ.get("MY_EMAIL")

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,nl;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
}

response = requests.get(URL, headers = header)
response.raise_for_status()
web_page = (response.text)

soup = BeautifulSoup(web_page, "html.parser")
print(soup)

with open("Day 47/amazon.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

price_whole = soup.find("span", class_="a-price-whole").getText()
price_fraction = soup.find("span", class_="a-price-fraction").getText()

price_str= f"${price_whole}{price_fraction}"

price_float = float(price_str.replace("$", ""))
print(price_float)

title = soup.find(id="productTitle").getText().strip()
print(title)


if price_float < BUY_PRICE:
    message = f"{title}is now on sale for {price_float}"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email_user, password= email_pass)
        connection.sendmail(
            from_addr= email_user,
            to_addrs= to_email,
            msg = f"Subject: Amazon Price Drop\n\n {message}\n {URL}".encode("utf-8")
        )
        print("message sending")