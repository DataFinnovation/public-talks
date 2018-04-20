
import lxml.etree
import requests

# target location
url = 'https://github.com/DataFinnovation/public-talks/blob/master/pugs-scraping/example2.html'

# get the page
page = requests.get(url)

# parse it
tree = lxml.etree.fromstring(page.content)

# what elements we care about
theXPath = '//a[text()="link"]/@href'

# grab all of them
resultList = tree.xpath(theXPath)

# now grab one of those links
page2 = requests.get(resultList[0])

# and dump the headers for this next link
print(page2.headers)
