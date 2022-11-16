import json
from bs4 import BeautifulSoup
import asyncio
import aiohttp

url = 'https://swisstime.by/catalog/'
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
}

watch_data = []


async def get_page_data(session, page):
    page_url = f'https://swisstime.by/catalog/?PAGEN_1={page}'

    async with session.get(url=page_url, headers=headers) as response:
        response_text = await response.text()

        soup = BeautifulSoup(response_text, 'lxml')
        items_cards = soup.find('ul', class_='catalog catalog-cut-list flex').find_all('a', class_='st-card__link')

        for item in items_cards:
            link = 'https://swisstime.by' + item.get('href')
            brand = item.find('div', class_='st-card__brand').text
            model = item.find('div', class_='st-card__model').text
            price = item.find('div', class_='st-card__price').text
            credit = item.find('div', class_='st-card__credit').text.strip()[:-36] + '/мес.'
            stock = item.find('div', class_='st-card__stock').text.strip()

            watch_data.append(
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


async def main_data():
    async with aiohttp.ClientSession() as session:
        resp = await session.get(url=url, headers=headers)
        soup = BeautifulSoup(await resp.text(), 'lxml')
        pages_count = int(soup.find('li', class_='pagination-item pages col-06').find_all('a')[-2].text)

        tasks = []

        for page in range(1, pages_count + 1):
            task = asyncio.create_task(get_page_data(session, page))
            tasks.append(task)

        await asyncio.wait(tasks)


def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_data())

    with open('data.json', 'a', encoding='utf-8') as file:
        json.dump(watch_data, file, indent=4, ensure_ascii=False)


if __name__ == '__main__':
    main()
