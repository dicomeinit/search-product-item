import requests
from bs4 import BeautifulSoup
import pandas as pd
import json


URL = "https://jysk.ua/noviy-rik-ta-rizdvo/cvichniki/likhtari"


response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Scrape name for product

all_name_items = soup.select(".product-teaser-body-top")
product_name = []
for name in all_name_items:
    product_name.append(name.get_text())

print(product_name)
print(len(product_name))

# Scrape price for product
all_prices_items = soup.select(".product-price-value")
product_price = []
for price in all_prices_items:
    product_price.append(price.get_text()[:-1])

print(product_price)
print(len(product_price))


# Scrape image link for product

all_images = soup.find_all('img')
images_link = []
for image in all_images:
    images_link.append(image.get("data-src"))

product_images = []
for i in images_link:
    if i == None:
        pass
    elif i[:5] == "https":
        product_images.append(i)

print(product_images)
print(len(product_images))

d = {'Name': product_name,'Price': product_price, 'Image': product_images}
df = pd.DataFrame(d, columns=['Name','Price','Image'])
print(df)
result = df.to_json(orient="records")
parsed = json.loads(result)
json.dumps(parsed, indent=4)


list_dict = []

for index, row in list(df.iterrows()):
    list_dict.append(dict(row))

# with open("output.json", 'w') as f:
#     f.write("\n".join(str(item) for item in list_dict))

with open("output.csv", 'w') as f:
    f.write("\n".join(str(item) for item in list_dict))