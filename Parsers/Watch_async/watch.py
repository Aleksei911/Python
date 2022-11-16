import json
import requests
from bs4 import BeautifulSoup

url = 'https://swisstime.by/catalog/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}


def get_all_pages():
    r = requests.get(url=url, headers=headers).text
    soup = BeautifulSoup(r, 'lxml')
    pages_count = int(soup.find('li', class_='pagination-item pages col-06').find_all('a')[-2].text)

    return pages_count


def collect_data(pages_count):

    data = []

    for page in range(1, pages_count):
        page_url = f'https://swisstime.by/catalog/?PAGEN_1={page}'

        r = requests.get(url=page_url, headers=headers).text
        soup = BeautifulSoup(r, 'lxml')
        items_cards = soup.find('ul', class_='catalog catalog-cut-list flex').find_all('a', class_='st-card__link')

        for item in items_cards:
            link = 'https://swisstime.by' + item.get('href')
            brand = item.find('div', class_='st-card__brand').text
            model = item.find('div', class_='st-card__model').text
            price = item.find('div', class_='st-card__price').text
            credit = item.find('div', class_='st-card__credit').text.strip()[:-36] + '/мес.'
            stock = item.find('div', class_='st-card__stock').text.strip()

            data.append(
                {
                    'link': link,
                    'brand': brand,
                    'model': model,
                    'price': price,
                    'credit': credit,
                    'stock': stock
                }
            )

        print(f'[INFO] Обработана страница {page}')

    with open('data.json', 'a', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def main():
    pages_count = get_all_pages()
    collect_data(pages_count)


if __name__ == '__main__':
    main()
