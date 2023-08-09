import urllib3
from bs4 import BeautifulSoup as soup
import urllib.parse
import random
import time
import os

with open('racks.txt', 'r') as f:
    for line in f:
        line = line.strip()
        encoded_line = urllib.parse.quote(line)
        my_url = ('https://www.google.com/search?q=' + encoded_line + '+connectparts')

        http = urllib3.PoolManager()
        r = http.request('GET', my_url)
        page_html = r.data

        page_soup = soup(page_html, "html.parser")

        links = page_soup.find_all('a')

        for link in links:
            href = link.get('href')
            if 'https://www.connectparts.com.br/' in href:
                href = href.split('https://www.connectparts.com.br/')[1]
                href = 'https://www.connectparts.com.br/' + href
                href = href.split('&')[0]
                with open('links.txt', 'a') as f:
                    f.write(href + '\n')
                break
        time.sleep(random.randint(1, 5))

with open ('links.txt', 'r') as f:
    for line in f:
        line = line.strip()

        http = urllib3.PoolManager()
        r = http.request('GET', line)
        page_html = r.data

        page_soup = soup(page_html, 'html.parser')
        containers = page_soup.find('div', {'class':'informacoes-produto descricao-produto'}).text

        try:
            with open('products.csv', 'a', encoding='utf-8') as f:
                f.write(containers + '\n\n')
        except:
            print('Error')
        time.sleep(random.randint(1, 5))
os.remove('links.txt')