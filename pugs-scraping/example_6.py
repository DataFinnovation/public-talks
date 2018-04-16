
import os
import tempfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

chromeOptions = webdriver.ChromeOptions()

downloadDir = tempfile.mkdtemp()
prefs = { 'download.default_directory' : downloadDir }
chromeOptions.add_experimental_option("prefs",prefs)
driver = webdriver.Chrome(options=chromeOptions)

# grab that big file
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

productForm = driver.find_element_by_xpath("//select[contains(@name,'ctl00$MainContentHolder$ListBox1')]")
formSelect = Select(productForm)
formSelect.select_by_visible_text('Call Reports -- Single Period')

radioButton = driver.find_element_by_id('XBRLRadiobutton')
radioButton.click()

button = driver.find_element_by_name('ctl00$MainContentHolder$TabStrip1$Download_0')

startFiles = os.listdir(downloadDir)

button.click()
found = False
while not found:
    print('searching...')
    sleep(1)
    newFiles = os.listdir(downloadDir)
    for f in newFiles:
        if f not in startFiles and f[-4:] == '.zip':
            found = f
            print('found!')

sleep(5)
