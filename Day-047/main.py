from bs4 import BeautifulSoup
import requests
import smtplib

url = 'https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6'

MY_EMAIL= ''
MY_PASSWORD =''

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=header)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
sale_price_WN = soup.find(name='span', class_='a-price-whole')
sale_price_dec = soup.find(name='span', class_='a-price-fraction')
product_title = soup.find(name='span', id='productTitle').getText()

product_price = f'{sale_price_WN.getText()}{sale_price_dec.getText()}'

BUY_PRICE = 100
print(product_price, product_title)
if float(product_price) < BUY_PRICE:
    message = f"{product_title} is on sale for {product_price}!"
    
with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL, 
                        to_addrs=MY_EMAIL, 
                        msg=f'Subject:Amazon Price Drop Alert!\n\n{message}\n{url}'.encode('utf-8')
    )


