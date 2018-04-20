
import lxml.etree
from lxml import html
import requests

import os
import tempfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

url = 'https://raw.githubusercontent.com/DataFinnovation/public-talks/master/pugs-scraping/example1.html'

page = requests.get(url)

tree = lxml.etree.fromstring(page.content)

theXPath = '//strong/text()'
resultList = tree.xpath(theXPath)
print('FROM THE FIRST DEMO: '+resultList[0])

print('NOW WE CAN FIRE UP CHROME')
driver = webdriver.Chrome()

url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

dateField = driver.find_element_by_id('UpdatedTextCDR')
print('and grab the date field: '+dateField.text)

print('now a quick sleep....')
sleep(5)
print('lets review browsers briefly')
url = 'http://homepc:4040/~jonreiter/pugs_talk/talk.pdf#page=12'
driver.get(url)
sleep(5)

driver.quit()

print('and now in firefox')
firefoxOptions = Options()
driver = webdriver.Firefox(options=firefoxOptions)
url2 = 'http://homepc:4040/~jonreiter/pugs_talk/talk.pdf#page=13'
driver.get(url2)

print('sleep a bit more')
sleep(10)
driver.quit()
print('and done')
