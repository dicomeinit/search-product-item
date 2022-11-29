import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


URL = "https://jysk.ua/noviy-rik-ta-rizdvo/cvichniki/likhtari"

PARAMETERS = {

}

response = requests.get(URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")

images = soup.findAll('img')
print(len(images))
images_link = []
item_name = []
for image in images:
    # Print image source
    images_link.append(image['src'])
    # print(image['src'])
    # Print alternate text
    item_name.append(image['alt'])
    # print(image['alt'])
# print(images_link)
# print(len(item_name))

all_name_items = soup.select(".product-teaser-body-top")
# print(all_name_items)
# print(all_link_elements)
all_name = []
for name in all_name_items:
    all_name.append(name.get_text())
# print(all_name)

all_prices = []
all_prices_items = soup.select(".product-price-value")
for price in all_prices_items:
    all_prices.append(price.get_text()[:-1])
# print(all_prices)

all_links_items = soup.select(".product-teaser-image-link")

images = soup.find_all('img')
books = soup.find_all(
        'a', attrs={'class':
                'product-teaser-image-link'})
# for book in books:
#     print(type(book))


a_tags = soup.find_all('img', src=True) # 👉️ Find all <a> tags that have a href attr

im = []
# 👇 Loop over the results
for tag in a_tags:
    print(type(tag))
    im.append(tag['src'])


images = soup.find_all('img')
images_link = []
for image in images:
    print(image.get("data-src"))
    images_link.append(image.get("data-src"))

print(images_link)
new_list = []
for i in images_link:
    print(type(i))
    if i == None:
        pass
    elif i[:5] == "https":
        new_list.append(i)

        # if i.startswith("/"):
        #     images_link.pop(i)
print(new_list)
# print(books)
a = 'https://cdn3.jysk.com/getimage/wd2.teaser/166520'
print(a[:5])
# for img in images:
#     if img.has_attr('src'):
#
#         print(img['src'])

# for link in all_link_elements:
#     print(link.get("data-src"))
#
# import scrapy
#
#
# class LightSpider(scrapy.Spider):
#     name = "lights"
#     start_url = [
#         "https://jysk.ua/noviy-rik-ta-rizdvo/cvichniki/likhtari"
#     ]
#
#     def parse_item(self, response, **kwargs):
#         price = item.
