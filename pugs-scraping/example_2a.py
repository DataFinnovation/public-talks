
import lxml.etree
import requests

# target location
url = 'https://raw.githubusercontent.com/DataFinnovation/public-talks/master/pugs-scraping/example3.html'

# get the page
page = requests.get(url)

# parse it
tree = lxml.etree.fromstring(page.content)

# what elements we care about
theXPath = '//td[@class="name" and text() = "Apple"]'
thePriceXPath = '../td[@class="price"]/text()'
theColorXPath = '../td[@class="color"]/text()'

# get the apple element
appleEle = tree.xpath(theXPath)[0]

# find price and color relative to apple
price = appleEle.xpath(thePriceXPath)[0]
color = appleEle.xpath(theColorXPath)[0]

# now grab one of those links
print("price is: " + price)
print("color is: " + color)

