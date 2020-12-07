from bs4 import BeautifulSoup
import requests
source = requests.get('https://web.njit.edu/~tjm67/parsetest.html').text

soup = BeautifulSoup(source, 'lxml')

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()
