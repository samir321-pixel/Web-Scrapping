import csv
from bs4 import BeautifulSoup
import requests



def genrate_CSV():
    url = "https://www.croma.com/televisions-accessories/led-tvs/4k-ultra-hd-tvs/c/999"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    results = soup.find_all('div', {'class': 'product-info'})
    data = []

    for index, item in enumerate(results):
        title = item.find('h3', {'class': 'product-title plp-prod-title'}).text.strip()
        brand = title.split()[0]
        mrp = item.find('span', {'class': 'amount'}).text.strip().replace(',', '')
        old_price = item.find('span', {'class': 'old-price'}).text.strip().replace(',', '')
        # product_url = item.find('a', {'class': 'product-title plp-prod-title'}).get('href')
        # image_url = item.find('img', {'class': 'product-img plp-card-thumbnail'}).get('src').strip()
        # print(image_url)
        data.append({
            'Title': title,
            'Brand': brand,
            'MRP': mrp,
            'Old price': old_price,
            # 'Count of Ratings': rating_count,
            # 'Count of Reviews': review_count,
            # 'Average Rating Score': rating_score,
            # 'Product URL': product_url,
            # 'Image URL': image_url,
            'Listing position': index + 1
        })

    if len(data) > 0:
        print('check me')
        with open('croma_products.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            writer.writeheader()
            for d in data:
                writer.writerow(d)
        writer.writeheader()
        for d in data:
            writer.writerow(d)
    else:
        print('this')


genrate_CSV()
