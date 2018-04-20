
import requests
from bs4 import BeautifulSoup
import lxml.etree

# target location
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'

# get it
page = requests.get(url)

# this will throw cause the content doesn't parse
tree = lxml.etree.fromstring(page.content)
