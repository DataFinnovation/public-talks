
import lxml.etree
from lxml import html
import requests

url = 'http://homepc:4040/~jonreiter/pugs_talk/example1.html'

page = requests.get(url)

tree = lxml.etree.fromstring(page.content)

theXPath = '//a[text()="link"]/@href'
resultList = tree.xpath(theXPath)

page2 = requests.get(resultList[0])
print(page2.text)
