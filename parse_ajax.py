import requests
from bs4 import BeautifulSoup
import csv
import time


HEADERS = {
    'Host': 'mail.ru',
    'Pragma': 'no-cache',
    'Referer': 'https://mail.ru/',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="90", "Google Chrome";v="90"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/90.0.4430.212 Safari/537.36',
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_pages_count(html):
    soup = BeautifulSoup(html, 'html.parser')
    pagination_to = soup.find('div', class_='nums')
    if pagination_to:
        pagination_to = soup.find('div', class_='nums')
        pagination = pagination_to.find_all('a')
        return int(pagination[-1].get_text())
    else:
        return 1


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.find_all('a')

    catalog = []
    for item in items:
        item = str(item)
        a = item.find("svelte-1kcqj27")
        if a != -1:
            continue
        print(item)

        catalog.append({

        })
    return catalog


def save_file(items, path):
    with open(path, 'w', encoding='utf8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow([])
        for item in items:
            writer.writerow([])


def parse():
    for URL in [

        'https://mail.ru/',

    ]:

        html = get_html(URL)
        if html.status_code == 200:
            catalog = []
            pages_count = get_pages_count(html.text)
            for page in range(1, pages_count + 1):
                print(f'Парсинг страницы {page} {pages_count} {URL}...')
                html = get_html(URL, params={'PAGEN_1': page})
                catalog.extend(get_content(html.text))
                time.sleep(1)
            FILE = 'parseResult' + '.csv'
            save_file(catalog, FILE)

            print(f'Получено {len(catalog)} пакетов')
        else:
            print('Error')


if __name__ == '__main__':
    parse()
