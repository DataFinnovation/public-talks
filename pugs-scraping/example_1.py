
import lxml.etree
import requests

# what page do we care about
url = 'https://raw.githubusercontent.com/DataFinnovation/public-talks/master/pugs-scraping/example1.html'

# get the page
page = requests.get(url)

# parse the content
tree = lxml.etree.fromstring(page.content)

# what element do we care about
theXPath = '//strong/text()'

# grab it
resultList = tree.xpath(theXPath)

# and print it out
print(resultList[0])
