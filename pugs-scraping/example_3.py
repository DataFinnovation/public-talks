
import requests
from bs4 import BeautifulSoup

# target location
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'

# get it
page = requests.get(url)

# feed beautifulsoup
soup = BeautifulSoup(page.text,'lxml')

# look over all a elements
for aElement in soup.find_all('a'):
    # and print out the target
    print(aElement.get('href'))
    