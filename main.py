# please read the instruction provided in readme to avoid any errors
from bs4 import BeautifulSoup
import requests
import smtplib

# using requests
url = "url of your product"
headers = {
    "User-Agent": "you will get this from http://myhttpheader.com/",
    "Accept-Language": "you will get this from http://myhttpheader.com/"
}
response = requests.get(url=url, headers=headers)
webpage = response.text
# making soup
soup = BeautifulSoup(webpage, "html.parser")

#  price of the product
product = soup.find(name="span", class_="a-price-whole")
product_title = soup.find(id="productTitle").get_text()
price = float(product.get_text())


# sending mail when the price is below  threshold
my_email = "your email"
if price < 40:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="your google app password")
        connection.sendmail(from_addr=my_email, to_addrs="the email on which you want the update",
                            msg=f"Subject:Amazon price alert!\n\n {product_title} is now ${price},\n {url} ")
