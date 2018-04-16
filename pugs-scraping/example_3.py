
import requests
from bs4 import BeautifulSoup

url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
for aElement in soup.find_all('a'):
    print(aElement.get('href'))
