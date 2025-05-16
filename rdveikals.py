import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
import requests
import bs4
import xlsxwriter


main_url = 'https://www.rdveikals.lv/'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'}

data = [['Nosaukums', 'Cena EUR']]

def get_soup(url):
    res = requests.get(url, headers=headers)
    return bs4.BeautifulSoup(res.text, 'html.parser')
    
# nolasa nosaukumus un cenas katrā lapā
iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/1/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/2/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/3/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/4/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/5/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/6/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/7/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])

iphone_page = get_soup(main_url+'categories/lv/388/sort/5/filter/0_0_74_0/page/8/Mobilie-telefoni.html')
iphones = iphone_page.findAll('div', class_='product__info')
for item in iphones:
    title = item.find('h3', class_='product__title').a.get_text(separator=' ', strip=True)
    price = item.find('p', class_='price').find(text=True).strip()
    data.append([title, price])
    
# ieraksta datus excel failā
with xlsxwriter.Workbook('rdveikalss.xlsx') as workbook:
    worksheet = workbook.add_worksheet()

    for row_num, info in enumerate(data):
        worksheet.write_row(row_num, 0, info)

