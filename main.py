from bs4 import BeautifulSoup
import requests
import smtplib

# using requests
url = "https://www.amazon.com/dp/B007WQ9YNO/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
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
my_email = "pythoncode61xd@gmail.com"
if price < 40:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password="viyxkqqbdzjlfwfm")
        connection.sendmail(from_addr=my_email, to_addrs="frhndar@gmail.com",
                            msg=f"Subject:Amazon price alert!\n\n {product_title} is now ${price},\n {url} ")
