
import requests
from bs4 import BeautifulSoup
import datetime

# target location
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'

# get it
page = requests.get(url)

# feed beautifulsoup
soup = BeautifulSoup(page.text,'lxml')

# check everthing with an id of UpdatedTextCDF
for span in soup.find_all(id="UpdatedTextCDR"):
    # print out the text content
    print(span.text)
    
    # we can manipulate that text content in python using great built-ins
    spanList = [[int(i) for i in span.text.split(' ')[2].split('/')][j] for j in [2,0,1]]
    
    # and then convert into other types and process however we want
    dt = datetime.datetime(spanList[0],spanList[1],spanList[2])
    print(dt.isoformat())
