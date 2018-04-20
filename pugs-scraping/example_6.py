
import os
import tempfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

# make a temporary download directory
downloadDir = tempfile.mkdtemp()

# and set up chrome to use it
prefs = { 'download.default_directory' : downloadDir }
chromeOptions = webdriver.ChromeOptions()
chromeOptions.add_experimental_option("prefs",prefs)

# kick off a chrome
driver = webdriver.Chrome(options=chromeOptions)

# back to our url
url = 'https://cdr.ffiec.gov/public/PWS/DownloadBulkData.aspx'
driver.get(url)

# fill out the forms and buttons
productForm = driver.find_element_by_xpath("//select[contains(@name,'ctl00$MainContentHolder$ListBox1')]")
formSelect = Select(productForm)
formSelect.select_by_visible_text('Call Reports -- Single Period')
radioButton = driver.find_element_by_id('XBRLRadiobutton')
radioButton.click()

# find the download button
button = driver.find_element_by_name('ctl00$MainContentHolder$TabStrip1$Download_0')

# get listing of files in the download directory
startFiles = os.listdir(downloadDir)

# kick of the download
button.click()

# loop looking for a finished file
found = False
while not found:
    print('searching...')
    sleep(1)
    
    # what files do we have now
    newFiles = os.listdir(downloadDir)
    for f in newFiles:
        # any new files ending in .zip?
        if f not in startFiles and f[-4:] == '.zip':
            found = f
            print('found!')

# wait a bit for demo reasons
sleep(15)
driver.quit()