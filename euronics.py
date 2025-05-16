import requests
import bs4
import xlsxwriter
import re


main_url = 'https://www.euronics.lv/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

data = [['Nosaukums', 'Сena EUR']]

def get_soup(url):
    res = requests.get(url, headers=headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')

iphone_page = get_soup(main_url + 'telefoni/viedtalruni/visi-viedtalruni/apple?f=CgVwcmljZSIFCEUQjx0wAw&p=1')
iphones = iphone_page.find_all('article', class_='product-card')


for item in iphones:
    # nolasa nosaukumu
    title_tag = item.find('span', class_='product-card__title')
    title = title_tag.get_text(strip=True) if title_tag else 'Nosaukums nav atrasts'

    # nolasa cenu
    price_tag = item.find('div', class_='price')
    if price_tag:
        parts = list(price_tag.stripped_strings)
        raw_price = ''.join(parts)
        prices_found = re.findall(r'\d+[.,]?\d*', raw_price)

        if prices_found:
            price = prices_found[-1].replace(',', '.').strip()
        else:
            price = 'nav'
    else:
        price = 'nav'

    data.append([title, price])

# Ieraksta excel failā
with xlsxwriter.Workbook('Euronics.xlsx') as workbook:
    worksheet = workbook.add_worksheet()
    for row_num, row_data in enumerate(data):
        worksheet.write_row(row_num, 0, row_data)
