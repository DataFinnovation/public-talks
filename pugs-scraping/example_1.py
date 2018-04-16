
import lxml.etree
from lxml import html
import requests

url = 'http://homepc:4040/~jonreiter/pugs_talk/example1.html'

page = requests.get(url)

tree = lxml.etree.fromstring(page.content)

theXPath = '//strong/text()'
resultList = tree.xpath(theXPath)
print(resultList[0])

# discarded because they arent valid!
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
url = 'https://www.sec.gov/Archives/edgar/daily-index/'
url = 'http://www.twse.com.tw/en/page/trading/exchange/MI_INDEX.html'
url = 'http://download.companieshouse.gov.uk/en_accountsdata.htmls'
