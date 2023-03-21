import requests
import lxml
from bs4 import BeautifulSoup


account_sid = "ACcfdf8357819f3f7052d7c0920939cd6f"
auth_token ="e2e32b3783c5a359e14ee70bab666df4"

url = "https://www.amazon.de/-/en/Collagen-Capsules-Hydrolysate-Laboratory-WeightWorld/dp/B079C336Y3/?_encoding=UTF8&pd_rd_w=DPXzE&content-id=amzn1.sym.8463cbd9-7666-4930-9308-5fb6659e4c3e&pf_rd_p=8463cbd9-7666-4930-9308-5fb6659e4c3e&pf_rd_r=84V2C9K1XS4FYWS8DV16&pd_rd_wg=5hhsW&pd_rd_r=4751ec1e-228d-461d-a816-d304c7832464&ref_=pd_gw_bmx_gp_kc75kbcn"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","Accept-Language": "en-DE,en;q=0.9,de-DE;q=0.8,de-BE;q=0.7,de;q=0.6,en-GB;q=0.5,en-US;q=0.4"}
response = requests.get(url, headers = header)
web_page = response.text
soup = BeautifulSoup(web_page,"lxml")
pricem = soup.find(id = "sns-base-price").getText().strip()
price = pricem.replace('\n','').strip()
print(type(price))
print(price)
price_without_currency = price.split(" ")[-1].replace('€','').replace(")"," ")
print("str= " + price_without_currency)
#float_price = float(k)



