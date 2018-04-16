
import requests
from bs4 import BeautifulSoup
import datetime

url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'

page = requests.get(url)

soup = BeautifulSoup(page.text,'lxml')
for span in soup.find_all(id="UpdatedTextCDR"):
    print(span.text)
    
    # it's python...
    spanList = [[int(i) for i in span.text.split(' ')[2].split('/')][j] for j in [2,0,1]]
    dt = datetime.datetime(spanList[0],spanList[1],spanList[2])
    print(dt.isoformat())
